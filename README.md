# Word Counter

This Python script analyzes a video to count the occurrences of a user-specified word spoken in the audio track. It utilizes the SpeechRecognition library with CMUSphinx for speech recognition and MoviePy for video processing.

## Requirements

Ensure you have Python installed. You can install the required libraries by running:

```bash
pip install -r requirements.txt
```

## Usage

1. Place your video file in the same directory as the script.
2. Update the `video_path` variable in the script with the filename of your video.
3. Run the script:

```bash
python main.py
```

The script will prompt you to enter the word you want to count, and then it will output the total count of that word detected in the video's audio.
