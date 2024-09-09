
# JAT Project

## Overview

The **JAT Project** combines a Python web application with a browser extension to provide an integrated solution for data processing and automation. The project features a browser extension that interacts with user inputs and web content, and a Python-based backend for handling data preprocessing and analysis.

## Streamlining Job Applications from Gmail
This project automates the process of extracting job application information directly from your Gmail account and providing data analysis on it. By connecting to your Gmail account (via the Gmail API), the system automatically retrieves and processes emails related to job applications, allowing you to:

Extract job application details (e.g., company names, dates applied, statuses, etc.).
Perform analysis to track application statuses, deadlines, and responses.
Visualize application trends and success rates over time.
This helps streamline your job application workflow by keeping all relevant data in one place and providing actionable insights to improve your job search strategy.

## Features

### 1. **Web Application (`app.py`)**
- The Python web application provides the main backend logic for the project.
- It handles requests from the browser extension and other external systems, and processes data using Python scripts.

### 2. **Browser Extension**
The browser extension automates and enhances certain web-based workflows. It includes the following components:
- **`background.js`**: Manages background tasks for the extension, like event handling.
- **`popup.html`**: The user interface for the extension.
- **`script.js`**: Provides interactivity for the popup, enabling user interactions with the extension.
- **`quotes.js`**: Handles custom quote generation or related logic.
- **`manifest.json`**: Configuration file that defines the extension’s behavior, permissions, and resources.

### 3. **Data Preprocessing**
- **`preprocessing_types.py`**: This script includes data preprocessing functions to transform raw data into formats ready for analysis.

## Installation

### Prerequisites
- Python 3.x
- Flask (for running the web app)
- A web browser (Chrome or Firefox) for running the extension
- Libraries mentioned in `requirements.txt` (not provided in the project directory, but can be created based on the required dependencies)

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/JAT-main.git
   cd JAT-main
   ```

2. **Install dependencies** (If using Flask or other libraries):
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Web Application**:
   ```bash
   python app.py
   ```

4. **Install the Browser Extension**:
   - Open your web browser and navigate to the Extensions page.
   - Enable "Developer Mode".
   - Load the unpacked extension from the `/extension` folder of this project.

## Usage

### Web Application
1. Start the web application by running:
   ```bash
   python app.py
   ```
2. Access the application at the specified local address (usually `http://127.0.0.1:5000`).

### Browser Extension
1. After installing the extension, you can access it by clicking the extension icon in your browser toolbar.
2. Use the interface provided by `popup.html` to interact with the extension. The extension sends data and requests to the web application for processing.

## File Structure

```bash
JAT-main/
│
├── app.py                 # Main application logic
├── README.md              # Project documentation
├── extension/             # Browser extension files
│   ├── background.js      # Handles background operations for the extension
│   ├── icon.png           # Icon used in the browser toolbar
│   ├── manifest.json      # Extension configuration file
│   ├── popup.html         # Extension UI
│   ├── quotes.js          # Logic for handling quotes or content in the extension
│   └── script.js          # Client-side script for the extension
│
├── gpt_files/             # Python data processing and utilities
│   └── preprocessing_types.py  # Data preprocessing scripts
```

## Contributing

We welcome contributions! If you would like to improve this project, please:
1. Fork the repository.
2. Create a new branch.
3. Submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
