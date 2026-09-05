# 🧠 Context-Aware Desktop AI Assistant

A Windows desktop AI assistant that understands what the user is currently doing on their computer and provides relevant assistance based on the current screen context.

The goal of this project is to move beyond traditional AI assistants where users have to manually take screenshots, copy text, or explain their situation. Instead, the assistant should be able to capture and understand relevant screen context when the user asks for help.

---

## 🚀 Project Vision

The long-term goal is to build an intelligent desktop assistant that can understand the user's current workflow across applications such as:

* VS Code
* Web browsers
* Terminal
* PDF readers
* PowerPoint
* Other desktop applications

For example:

> If a user encounters a Python error in VS Code, they should be able to trigger the assistant, ask **"What's wrong here?"**, and receive an explanation based on the content currently visible on their screen.

### Core Concept

```text
Screen
   ↓
Capture
   ↓
Context Extraction
   ↓
Context Understanding
   ↓
Relevant Context Selection
   ↓
AI Model
   ↓
Response
```

The **Context Engine** will eventually become the core component responsible for understanding and selecting the most relevant information from the user's current environment.

---

## 🎯 Current Goal

The project is being developed incrementally using a milestone-based approach.

We are intentionally **not building the entire system at once**.

Each milestone is implemented, tested, and verified before moving to the next one.

---

## ✅ Milestones

### Milestone 1 — Screen Capture ✅

* Capture the primary monitor
* Save the captured screen as a PNG
* Verify that screen capture works successfully
* Establish the initial Python project environment

### Milestone 2 — Basic Visual Analysis ✅

* Extract useful information from the captured screen
* Explore OCR and visual understanding
* Prepare screen context for AI processing

### Milestone 3 — Question Answering ✅

* Define an AI provider abstraction
* Use Gemini to answer questions about structured screen context
* Keep provider-specific API code isolated from screen analysis

### Milestone 4 — Global Hotkey + Desktop UI ⏳

* Add a global keyboard shortcut
* Build a simple desktop assistant interface
* Connect the hotkey to context capture and questioning

### Milestone 5 — Context Engine ⏳

* Understand screen context
* Select relevant information
* Reduce unnecessary data sent to the AI model
* Build the core context-processing pipeline

### Future Milestones

* Application awareness
* Short-term and long-term memory
* Voice interaction
* Computer control with user confirmation
* Proactive assistance

---

## 🛠️ Technology Stack

### Current

* **Python**
* **mss** — screen capture
* **Pillow** — image loading and metadata
* **pytesseract** — OCR integration
* **google-genai** — Gemini API integration
* **unittest** — testing
* **Python virtual environment**

### Planned

* **PySide6** — desktop UI
* **PaddleOCR** or another OCR solution for future OCR improvements
* **Vision-capable AI model**
* **Global hotkey library**
* **SQLite** — future memory storage

---

## 🔐 Privacy

Screen context can contain sensitive information, so privacy is an important part of the project.

Planned privacy features include:

* Pause screen monitoring
* Exclude specific applications or windows
* Avoid unnecessary screenshot storage
* Temporary context expiration
* Clear context manually
* Visible indication when screen context is being analyzed

The project will prioritize collecting only the context that is necessary to answer the user's question.

---

## 📁 Current Project Structure

```text
context-aware-ai/
│
├── .venv/
│
├── capture_screen.py
│
├── screen_analyzer.py
│
├── test_screen_analyzer.py
│
├── screenshots/
│
├── tests/
│   └── ...
│
├── .gitignore
│
└── requirements.txt
```

The project structure will evolve as new milestones are implemented.

---

## 🧪 Development Philosophy

This project follows a simple development rule:

> **Build → Test → Verify → Improve → Next Milestone**

We avoid unnecessary complexity and focus on proving each capability before expanding the system.

Major architectural decisions will be made before implementation rather than introducing unnecessary complexity early.

---

## 🌟 Why This Project?

Traditional AI assistants usually require users to provide context manually.

This project explores a different interaction model:

```text
Traditional AI:
User → Explain Context → AI → Response

Context-Aware AI:
User → Ask Question → AI understands current context → Response
```

The goal is to make AI assistance feel more naturally integrated into the user's desktop workflow.

---

## 📌 Project Status

**Current Status: Milestones 2 and 3 Complete ✅**

Screen capture, OCR-based visual analysis, and Gemini question answering have been implemented and successfully tested.

More capabilities will be added step-by-step.

---

## 👨‍💻 Development

This project is being developed as an experimental learning project focused on:

* AI engineering
* Computer vision
* Desktop application development
* Context-aware systems
* Human-AI interaction
* Software architecture

---

## 📜 License

This project is currently intended for educational and experimental purposes.


## Milestone 2: Basic Visual Analysis

Install the Python dependencies from `requirements.txt`. OCR also requires the
separate Tesseract OCR application on Windows. Install a trusted Windows build
of Tesseract, then make sure `tesseract.exe` is on `PATH` (or configure
`pytesseract.pytesseract.tesseract_cmd` in `screen_analyzer.py`).

Tesseract receives the captured PNG and returns recognized words, confidence
scores, and bounding boxes. The Python code turns those results into JSON
screen context.

Capture only:

```text
python capture_screen.py
```

Capture and analyze with OCR:

```text
python capture_screen.py --analyze
```

Analyze an existing screenshot directly:

```text
python screen_analyzer.py screenshots/screenshot.png
```

Run the Milestone 2 tests:

```text
python -m unittest test_screen_analyzer.py
```

## Milestone 3: Gemini Question Answering

Install the dependencies from `requirements.txt`, then set the Gemini API key
in the environment before using `GeminiProvider`:

```powershell
$env:GEMINI_API_KEY = "your-api-key"
```

The provider accepts the structured dictionary returned by
`screen_analyzer.analyze_screen` and a user question. It returns Gemini's text
answer through the provider interface without coupling screen analysis to a
specific AI service.

Run all tests with:

```text
python -m unittest
```
