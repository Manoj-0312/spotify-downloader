import os
from moviepy.editor import AudioFileClip

def convert_folder_mp4_to_mp3(input_folder):
    try:
        # List all files in the input folder
        i = 1
        for filename in os.listdir(input_folder):
            if filename.endswith(".mp4"):
                print(i,end=": ")
                i=i+1
                input_file_path = os.path.join(input_folder, filename)

                # Construct the output MP3 file path
                output_file_path = os.path.join(input_folder, f"{os.path.splitext(filename)[0]}.mp3")

                # Load the video clip
                video_clip = AudioFileClip(input_file_path)

                # Extract audio from the video clip
                audio_clip = video_clip

                # Write the audio to an MP3 file
                audio_clip.write_audiofile(output_file_path, codec='mp3')

                print(f"Conversion from {input_file_path} to {output_file_path} successful.")

                # Delete the original MP4 file
                os.remove(input_file_path)
                print(f"Original file {input_file_path} deleted.")

    except Exception as e:
        print(f"Error: {e}")


