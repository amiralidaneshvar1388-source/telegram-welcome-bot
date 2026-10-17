@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo === Installing Python packages ===
py -m pip install --upgrade pip
if errorlevel 1 (
  echo Could not run Python. Install Python 3.11 or newer from https://www.python.org/downloads/windows/
  echo During installation, enable "Add Python to PATH".
  pause
  exit /b 1
)
py -m pip install -r requirements.txt
if errorlevel 1 (
  echo Package installation failed. Check your internet connection and Python installation.
  pause
  exit /b 1
)
if not exist .env (
  copy .env.example .env >nul
  echo Created .env. Open it and add your Telegram bot token.
)
echo.
echo Installation finished. Open .env and add your token, then run run.bat.
pause
