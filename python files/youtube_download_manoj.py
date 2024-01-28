from youtubesearchpython import VideosSearch
from pytube import YouTube
from moviepy.editor import *

def download_audio_by_name(song_name, output_path):
    i=0
    try:
        # Search for the song on YouTube
        videos_search = VideosSearch(song_name, limit = 1)
        results = videos_search.result()
        i=i+1

        # Get the first video URL
        video_url = "https://www.youtube.com/watch?v=" + results['result'][0]['id']

        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the audio stream with the highest quality
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Download the audio
        audio_stream.download(output_path)

        print(f"{i}: Audio for '{song_name}' downloaded successfully to {output_path}")
    except Exception as e:
        print(f"Error: {e}")







