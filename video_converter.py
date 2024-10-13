import os
import sys
from yt_dlp import YoutubeDL
from moviepy.editor import VideoFileClip

def download_video(url, output_path='video.mp4'):
    try:
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': output_path
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def convert_video_to_audio(video_path, audio_path='audio.mp3'):
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(audio_path)
        audio.close()
        video.close()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
