## Multiple Tasks like Q&A, Summerization, Text-Image Using Gemini Models

Here's a breakdown of the tasks performed in each file:

### `app.py`
This file sets up a Streamlit web application that interacts with the **Gemini Pro model** to generate responses based on text input.

1. **Environment Setup**: Loads environment variables using `load_dotenv()`, including the API key for Gemini.
2. **Model Configuration**: Configures the Gemini model using the API key and initializes the `gemini-pro` model.
3. **Response Function**:
   - Defines `get_gemini_response(question)`, which uses the `gemini-pro` model to generate responses based on a text question.
4. **Streamlit Application**:
   - Sets up a basic Streamlit app with a page title and a header.
   - Provides a text input box for users to enter their questions and a submit button.
   - Upon clicking submit, the app calls `get_gemini_response()` to get a response from the Gemini model and displays the response below.

### `vision.py`
This file builds on `app.py` by adding image input functionality to interact with the **Gemini 1.5 flash model** using both text and image prompts.

1. **Environment Setup**: Similar to `app.py`, it loads environment variables and sets up the API key.
2. **Model Configuration**: Configures the `gemini-1.5-flash` model, a variant capable of processing both text and image inputs.
3. **Response Function**:
   - Defines `get_gemini_response(input, image)`, which takes a text prompt (`input`) and an optional image. If text is provided, it generates content based on both the text and image; otherwise, it uses just the image.
4. **Streamlit Application**:
   - Sets up a basic interface with options for text input and image upload.
   - Adds an image uploader using `st.file_uploader`, allowing users to upload images (JPEG/PNG).
   - Displays the uploaded image if one is provided and offers a submit button to get the Gemini model's response based on the text and image inputs.
   - Shows the response from the model upon submission.
