import os
import shutil
import speech_recognition as sr
from moviepy.editor import VideoFileClip
from concurrent.futures import ThreadPoolExecutor

def count_word_in_chunk(chunk_path, word):
    word_count = 0
    recognizer = sr.Recognizer()

    with sr.AudioFile(chunk_path) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_sphinx(audio_data)
        word_count += text.lower().count(word.lower())
    except sr.UnknownValueError:
        pass

    return word_count

def count_word(video_path, word):
    word_count = 0
    temp_dir = "temp_audio_chunks"
    os.makedirs(temp_dir, exist_ok=True)

    video = VideoFileClip(video_path)
    audio = video.audio

    chunk_duration = 10
    chunk_paths = []

    for chunk_start in range(0, int(audio.duration), chunk_duration):
        audio_chunk = audio.subclip(chunk_start, min(chunk_start + chunk_duration, audio.duration))
        temp_audio_path = os.path.join(temp_dir, f"temp_audio_{chunk_start}.wav")
        audio_chunk.write_audiofile(temp_audio_path)
        chunk_paths.append(temp_audio_path)

    with ThreadPoolExecutor(max_workers=os.cpu_count() * 2) as executor:
        word_counts = executor.map(lambda x: count_word_in_chunk(x, word), chunk_paths)
        word_count = sum(word_counts)

    audio.close()
    video.close()
    shutil.rmtree(temp_dir)

    return word_count

if __name__ == "__main__":
    video_path = "Videos/video.mp4"
    word = input("Enter the word you want to count: ")
    word_count = count_word(video_path, word)
    print(f"Total '{word}' count:", word_count)