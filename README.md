# Textify_Extract

## Introduction

**Textify Extract** is a web application designed to simplify and enhance the process of extracting text from images and documents. Utilizing advanced technologies, our tool provides accurate and efficient text extraction solutions. With a user-friendly interface, Textify Extract allows you to quickly convert images into readable text, making it ideal for processing scanned documents, photos of text, and various other image formats.

## Demonstration / Working of the Website

1. **Home Page**:
   - **Upload Image**: Users can upload images via the home page. The interface is designed to be intuitive, with a prominent upload button.
   - **Background**: The page features a GIF background and a tagline to enhance visual appeal.
![image](https://github.com/user-attachments/assets/063ad298-409e-4946-9b6f-ac002c6ee4de)

![image](https://github.com/user-attachments/assets/a9e51223-fa7e-4915-bf81-93ba1c39b41f)

2. **Uploaded Images Page**:
   - **View Uploaded Images**: After uploading, users are redirected to a page where they can see a list of uploaded images.
   - **Extract Text**: Users can click on an image to extract text from it. The extracted text is displayed alongside the image.

3. **Extracted Text**:
   - **Text Display**: Once text is extracted, it appears in a text area on the right side of the screen, providing a clear view of the extracted content.
![image](https://github.com/user-attachments/assets/151e0c63-2ff9-457e-987e-3a6a43ff5922)


## Flask Application

- **Technology/Framework**: Flask
- **Programming Languages**: Python
- **Database**: SQLite (used to store image metadata and text extraction results)

The Flask backend handles the following:
- **Image Upload**: Manages image uploads and storage.
- **Text Extraction**: Utilizes OCR (Tesseract) to extract text from images.
- **API Endpoints**: Provides endpoints for retrieving images and extracting text.

## React Application

- **Technology/Framework**: React
- **Programming Languages**: JavaScript (ES6)
- **CSS Framework**: Custom CSS for styling
- **Libraries**: Axios (for API calls), React Router DOM (for navigation)

The React frontend includes:
- **Home Page Component**: Allows users to upload images and provides navigation to the upload results page.
- **Upload Success Component**: Displays uploaded images and extracted text. Provides functionality to view extracted text and navigate back to the home page.

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/textify-extract.git
   cd textify-extract
