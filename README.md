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

## Project Structure (Logical Flow)

- **Brain of the Doctor**  
  Handles medical reasoning and decision-making logic.

- **Voice of the Patient**  
  Captures and processes the user's voice input.

- **Voice of the Doctor**  
  Converts AI-generated responses into spoken output.

- **Gradio Interface**  
  Provides a web-based UI to interact with the system.

---

## Running the Project

Follow the steps below to run the application locally.

### Step 1: Activate the Virtual Environment
```bash
activate voicebot
