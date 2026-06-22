# LinkedIn Auto Applier

A robust automation tool designed to streamline job applications on LinkedIn. It programmatically queries for specified roles, fills application questionnaires, leverages LLMs to customize/answer application screening questions, and manages application history via a web dashboard.

---

## 🚀 Key Features

- **Automated Searching**: Queries for target roles in specified geographic locations using custom search intervals.
- **Form Auto-Filling**: Answers common screening questions (contact details, work rights, compensation expectations, experience).
- **Stealth Mode**: Uses undetected-chromedriver to minimize detection by automated scraping prevention.
- **Web Dashboard**: Displays logs and tracks the history of successful and skipped applications.
- **Custom Filtering**: Configurable filters to skip roles matching specific negative keywords or exceeding experience limits.

---

## 🛠️ Installation

### 1. Prerequisites
- **Python**: Ensure Python 3.10+ is installed on your system and added to your environment `PATH`.
- **Google Chrome**: Ensure the latest stable version of Google Chrome is installed.

### 2. Dependency Setup
Open your terminal/command prompt and run:
```bash
pip install undetected-chromedriver pyautogui setuptools openai flask-cors flask
```

### 3. Local Installation
1. Download this repository to a directory of your choice.
2. If you are on Windows, you can optionally run `setup/windows-setup.bat` to verify your environment.
3. On macOS/Linux, verify Google Chrome pathing or execute using standard Python 3.10.

---

## ⚙️ Configuration

Configure the application by modifying the settings files under the `config/` directory:

1. **`personal.py`**: Set your personal contact information (first name, last name, phone, address details, and demographics).
2. **`screening.py`**: Configure parameters like years of experience, visa requirements, default resume path, and cover letter templates.
3. **`search_filter.py`**: Define your search queries, location target, and filters (blacklist keywords, experience levels, etc.).
4. **`auth.py`**: Configure optional login credentials and AI configurations (OpenAI, DeepSeek, or Gemini model integration details).
5. **`app_settings.py`**: Adjust runtime preferences like safe mode, click intervals, stealth mode, and background running.

---

## 🖥️ Usage

1. Run the main bot executable:
   ```bash
   python3 main.py
   ```
2. To launch the Web Dashboard and view your application history:
   ```bash
   python3 server.py
   ```
   Open `http://localhost:5000` in your web browser.

---

## ⚖️ License

Copyright (c) 2026 Aditya Kumar

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🐧 Contact
- **LinkedIn** : https://www.linkedin.com/in/aditya-kumar-552232259/
- **Email**    : aditya12186@gmail.com