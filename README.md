# Doc OCR Tool

The **Doc OCR Tool** is a web-based application for extracting details from Indonesian KTP (ID cards) and NPWP (taxpayer) documents using Optical Character Recognition (OCR) with OpenAI's GPT-4o API. Users can upload images of KTP or NPWP documents, and the tool will extract and display relevant information in a structured format.

## Features

- **KTP and NPWP Document Processing**: Select between KTP and NPWP document types to extract relevant details.
- **Image Upload**: Supports image upload in JPG, PNG, or similar formats.
- **OCR and Structured Data Extraction**: Uses OpenAI's GPT-4o-mini model to extract and structure text from uploaded images.
- **Dynamic Error Handling**: Displays error messages for unsupported files, connection issues, or unprocessed images.

## Try it yourself
[Website](https://openai-doc-parser.onrender.com/)

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **OCR Processing**: OpenAI's GPT-4o-mini model

## Prerequisites

- Python 3.7 or higher
- [OpenAI API Key](https://platform.openai.com/signup) with access to the GPT-4o-mini model

## Setup and Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/tekina/openai-doc-parser.git
