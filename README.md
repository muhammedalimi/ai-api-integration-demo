Author - Muhammed Alimi

A simple Python project demonstrating how generation settings in the Google Gemini API affect model output.

## Overview

This project explores how parameters like `temperature` and `max_output_tokens` influence response style, variability, and length. It was built as a hands-on API integration exercise to better understand practical AI deployment controls.

## Features

- Google Gemini API integration in Python
- Environment variable support with `python-dotenv`
- Adjustable `temperature`
- Adjustable `max_output_tokens`
- Side-by-side output comparison across different settings

## Tech Stack

- Python
- Google Gemini API
- `google-genai`
- `python-dotenv`

## Project Structure

```text
ai-api-integration-demo/
├── gemini_temperature_demo.py
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md