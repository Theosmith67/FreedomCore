# Copilot Instructions for the Flask App Project

## Project Overview
This project is a Flask-based application designed to support a modular architecture. The codebase is organized into distinct components for handling routes, models, templates, and static assets. Additionally, the `freedom_core` package provides core functionalities such as mood analysis, response generation, and interaction logging.

### Key Directories and Files
- **`app.py`**: The entry point for the Flask application.
- **`01_config/settings.py`**: Contains configuration settings for the application.
- **`02_models/`**: Defines the data models used in the application.
- **`03_routes/`**: Contains route definitions and the main application logic.
- **`04_templates/`**: Stores HTML templates for rendering views.
- **`05_static/`**: Holds static assets like CSS, JavaScript, and images.
- **`freedom_core/`**: Implements core logic for the bot, including mood analysis, persona management, and logging.

## Core Components
### `freedom_core`
This package provides the core logic for the bot. Key modules include:
- **`core.py`**: Handles response generation.
- **`mood_engine.py`**: Analyzes the mood of user input.
- **`memory.py`**: Logs user interactions.
- **`persona_profile.py`**: Manages persona-specific behavior.

### Routes
Routes are defined in `03_routes/routes.py`. The `main.py` file in the same directory may serve as the central hub for initializing and registering routes.

### Templates and Static Files
HTML templates are stored in `04_templates/`, while static assets like CSS and JavaScript are in `05_static/`.

## Developer Workflows
### Setting Up the Environment
1. Activate the virtual environment:
   ```powershell
