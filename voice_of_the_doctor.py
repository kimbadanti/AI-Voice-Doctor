
# from dotenv import load_dotenv
# load_dotenv()

# #Step1a: Setup Text to Speech–TTS–model with gTTS
# import os
# from gtts import gTTS

# def text_to_speech_with_gtts_old(input_text, output_filepath):
#     language="en"

#     audioobj= gTTS(
#         text=input_text,
#         lang=language,
#         slow=False
#     )
#     audioobj.save(output_filepath)


# input_text="Hi this is Your Ultimate Doctor AI assistant, testing!"
# #text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")


# #Step2: Use Model for Text output to Voice

# import subprocess
# import platform

# def text_to_speech_with_gtts(input_text, output_filepath):
#     language="en"

#     audioobj= gTTS(
#         text=input_text,
#         lang=language,
#         slow=False
#     )
#     audioobj.save(output_filepath)
#     os_name = platform.system()
#     try:
#         if os_name == "Darwin":  # macOS
#             subprocess.run(['afplay', output_filepath])
#         elif os_name == "Windows":  # Windows
#             subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
#         elif os_name == "Linux":  # Linux
#             subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
#         else:
#             raise OSError("Unsupported operating system")
#     except Exception as e:
#         print(f"An error occurred while trying to play the audio: {e}")


# input_text="Hi this is Your Ultimate Doctor AI assistant, autoplay testing!"
# text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")



from dotenv import load_dotenv
load_dotenv()

#Step1a: Setup Text to Speech–TTS–model with gTTS
import os
import subprocess
import platform
from gtts import gTTS
import logging
from pydub import AudioSegment # <-- New import for conversion

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# You can keep the 'old' function, but we'll focus on the 'new' one

def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"
    
    # 1. Generate MP3 with gTTS
    logging.info(f"Generating audio for text: '{input_text[:50]}...'")
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    logging.info(f"Audio saved as MP3: {output_filepath}")

    os_name = platform.system()
    
    if os_name == "Windows":
        # --- FIX for Windows: Convert MP3 to WAV ---
        
        # 2. Define the temporary WAV file path
        wav_filepath = output_filepath.replace(".mp3", "_temp.wav")
        
        try:
            # 3. Convert MP3 to WAV using pydub/ffmpeg
            logging.info(f"Converting MP3 to WAV for Windows playback...")
            audio_segment = AudioSegment.from_mp3(output_filepath)
            audio_segment.export(wav_filepath, format="wav")
            logging.info(f"WAV file created: {wav_filepath}")

            # 4. Play the WAV file using the corrected PowerShell command
            playback_command = f'(New-Object Media.SoundPlayer "{wav_filepath}").PlaySync();'
            subprocess.run(['powershell', '-c', playback_command], check=True)
            logging.info("Playback successful.")
            
        except Exception as e:
            logging.error(f"Error during Windows audio playback or conversion: {e}")
        finally:
            # 5. Clean up the temporary WAV file
            if os.path.exists(wav_filepath):
                os.remove(wav_filepath)
                logging.info(f"Cleaned up temporary WAV file: {wav_filepath}")
                
    elif os_name == "Darwin":  # macOS (afplay supports MP3)
        try:
            subprocess.run(['afplay', output_filepath], check=True)
            logging.info("Playback successful (macOS).")
        except Exception as e:
            logging.error(f"Error during macOS audio playback: {e}")
            
    elif os_name == "Linux":  # Linux (May require installing mpg123 or ffplay)
         try:
            # Use 'ffplay' for MP3 support, or 'mpg123' if installed
            subprocess.run(['ffplay', '-nodisp', '-autoexit', output_filepath], check=True)
            logging.info("Playback successful (Linux).")
         except Exception as e:
            logging.error(f"Error during Linux audio playback. Try installing 'ffplay' or 'mpg123'. Error: {e}")
            
    else:
        logging.warning(f"Unsupported operating system: {os_name}. Audio saved but not played.")

# --- EXECUTION BLOCK ---
input_text = "Hi this is Your Ultimate Doctor AI assistant, autoplay testing! I am here to help you."
output_filepath = "gtts_testing_autoplay.mp3"

text_to_speech_with_gtts(input_text=input_text, output_filepath=output_filepath)