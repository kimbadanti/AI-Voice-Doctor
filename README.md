# AI Medical Voice Bot – First Aid Assistant

An AI-powered medical voice assistant that provides **first-aid guidance using image and voice inputs**.  
The system responds **only in voice**, making it suitable for hands-free usage during emergency situations.

This project demonstrates a practical use of AI in healthcare assistance, focusing on **early-stage medical support** rather than diagnosis.

---

## Project Idea

During medical emergencies or accidents, people often panic and are unsure about the immediate steps to take.  
This project addresses that problem by acting as a **first-aid medical assistant**, which analyzes the user's condition using AI and provides voice-based guidance.

The goal of the project is to show how AI can be used responsibly to assist users until professional medical help becomes available.

---

## How the Project Works

1. The user uploads an image related to the medical issue.
2. The user records a voice message describing the problem.
3. The system analyzes the image and voice input using AI models.
4. First-aid instructions are generated based on the context.
5. The response is converted into speech and played back to the user.

The entire interaction is designed to be simple, fast, and accessible.

---

## Project Structure

- **Brain of the Doctor**  
  Handles medical reasoning and decision-making logic.

- **Voice of the Patient**  
  Captures and processes the user's voice input.

- **Voice of the Doctor**  
  Converts AI-generated responses into spoken output.

- **Gradio Interface**  
  Provides a web-based interface for user interaction.

---

## Tech Stack

- **Language:** Python 3.11  
- **UI Framework:** Gradio  
- **Audio Processing:** FFmpeg, PortAudio  
- **AI Capabilities:**  
  - Speech-to-Text  
  - Text-to-Speech  
  - Image-based reasoning  

---

## Running the Project

Follow the steps below to run the application locally.

### Step 1: Activate the Virtual Environment
```bash
activate voicebot
````

### Step 2: Start the Application

```bash
python gradio_app.py
```

Once the application starts, Gradio will generate a local URL in the terminal.
Open that URL in your browser to interact with the AI Medical Voice Bot.

---

## Demo Video

A demo video showing the complete workflow of the project is available at:

```
[Add your demo video link here]
```


## Use Cases

* First-aid assistance during emergencies
* Situations with delayed medical support
* Hands-free medical guidance
* Remote or rural environments

---

## Disclaimer

This project is intended for **first-aid guidance only**.
It does not provide medical diagnoses and should not replace professional medical advice.

---

