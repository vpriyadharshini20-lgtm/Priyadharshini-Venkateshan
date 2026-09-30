# FitBuddy — AI Fitness Plan Generator

FitBuddy is a FastAPI web application that generates personalized 7-day
workout plans and nutrition/recovery tips using Google's Gemini AI, stores
users and plans in SQLite, and supports feedback-based plan regeneration.

## Features
- Personalized 7-day workout plan generation
- Goals: weight loss, muscle gain, general wellness
- Intensity levels: beginner, intermediate, advanced
- Gemini AI-powered plan and nutrition tip generation (with automatic
  rule-based fallback if no API key is configured)
- Feedback-based plan updating (regenerates the plan based on user comments)
- SQLite database storage (users + original/updated plans)
- Admin dashboard to view all users
- FastAPI backend + Jinja2 templates
- JSON API with Swagger docs

## Requirements
- Python 3.10+
- A Gemini API key (optional — app works without one via fallback logic)

## Setup Instructions

### 1. Create the project folder structure
Create the `FitBuddy/` folder and all subfolders/files exactly as shown in
the folder structure, pasting in the code provided.

### 2. Create and activate a virtual environment

**Windows (PowerShell):**