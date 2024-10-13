# app.py

from flask import Flask, render_template, request, send_file
import os
from video_converter import download_video, convert_video_to_audio

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    video_url = request.form['video_url']
    if not video_url:
        return "No URL provided"

    video_path = 'downloaded_video.mp4'
    audio_path = 'audio.mp3'

    # Download and convert
    download_video(video_url, video_path)
    convert_video_to_audio(video_path, audio_path)

    if os.path.exists(video_path):
        os.remove(video_path)

    return send_file(audio_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
