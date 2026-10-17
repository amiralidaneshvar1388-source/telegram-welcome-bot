@echo off
chcp 65001 >nul
cd /d "%~dp0"
if not exist .env (
  echo Missing .env file. Run install.bat first, then add your bot token to .env.
  pause
  exit /b 1
)
py bot.py
if errorlevel 1 (
  echo.
  echo The bot stopped because of an error. Read the message above.
  pause
)
