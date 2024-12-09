# PDF Interaction App

This Streamlit-based web application allows users to interact with PDF documents, ask questions about their content, and get responses in multiple languages. The application also features text-to-speech functionality for generated responses.

## Features

- Upload multiple PDF files.
- Ask questions about the content of the uploaded PDFs.
- Generate responses using a Language Model (LLM).
- Text-to-speech feature for generated responses.
- Multi-language support for responses.
- Customizable word limit for responses.

## Technologies Used

- **Python**: Core programming language.
- **Streamlit**: For building the web app interface.
- **LangChain**: For handling LLM functionalities.
- **GROQ API**: Used for LLM initialization.
- **Google Text-to-Speech**: For audio generation.
- **dotenv**: For managing environment variables.
- **Custom Utility Modules**:
  - `utils/general_utils`: For loading CSS.
  - `utils/langchain_utils`: For LLM initialization and response generation.
  - `utils/audio_utils`: For text-to-speech functionality.
  - `preprocessing`: For processing uploaded PDF files.

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
