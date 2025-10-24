

from dotenv import load_dotenv
load_dotenv()
import os
import gradio as gr

from brain_of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_patient import record_audio, transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_gtts

# --- System Prompt (No change) ---
system_prompt="""You have to act as a professional doctor, i know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""

# --- Corrected Processing Function ---
def process_inputs(audio_filepath, image_filepath):
    # Set the fixed output file path for the doctor's response
    output_audio_path = "doctor_response.mp3" # Use a clearer name

    # 1. Transcribe the patient's voice
    speech_to_text_output = transcribe_with_groq(
        GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
        audio_filepath=audio_filepath,
        stt_model="whisper-large-v3"
    )

    # 2. Get the doctor's text response
    full_query = system_prompt + speech_to_text_output
    
    if image_filepath:
        # Assuming encode_image and analyze_image_with_query work correctly
        encoded_img = encode_image(image_filepath)
        doctor_response = analyze_image_with_query(
            query=full_query, 
            encoded_image=encoded_img, 
            model="meta-llama/llama-4-scout-17b-16e-instruct"
        ) 
    else:
        # If no image, analyze based only on voice. 
        # (You might want a different model or flow here, but we'll stick to text-only analysis for now)
        # Note: You should update analyze_image_with_query or create a text-only function.
        # For simplicity, we'll use a placeholder or modify the query/model.
        # If the model requires an image, this will fail. For now, let's return a message.
        if speech_to_text_output.strip() == "":
            doctor_response = "Please provide an image or speak your symptoms."
        else:
            # Placeholder for text-only response (assuming LLM is smart enough to handle a None/Empty image)
            # Since the prompt is image-focused, we must adjust.
            doctor_response = "Please upload an image for me to provide a diagnosis."


    # 3. Generate the doctor's audio response and save it to the fixed path
    # NOTE: text_to_speech_with_gtts MUST return the output_audio_path ("doctor_response.mp3")
    # or just the function saves the file and we return the path later.
    text_to_speech_with_gtts(input_text=doctor_response, output_filepath=output_audio_path)
    
    # 4. Return the three output values in order
    return speech_to_text_output, doctor_response, output_audio_path


# --- Corrected Interface Definition ---
# Create the interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath", label="Patient's Voice"),
        gr.Image(type="filepath", label="Image for Diagnosis (e.g., rash, injury)")
    ],
    outputs=[
        gr.Textbox(label="1. Patient's Spoken Symptoms (Transcription)"),
        gr.Textbox(label="2. Doctor's Text Diagnosis"),
        gr.Audio(label="3. Doctor's Audio Response", type="filepath") # Type is already filepath, but for clarity
    ],
    title="AI Doctor with Vision and Voice"
)

if __name__ == "__main__":
    iface.launch(debug=True)