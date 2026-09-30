@echo off

title FitBuddy AI

echo ========================================
echo          FITBUDDY AI
echo ========================================
echo.

cd /d "%~dp0"

if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
)

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo.
echo Installing required packages...
python -m pip install -r requirements.txt

echo.
echo Starting FitBuddy...
echo.
echo Open your browser at:
echo http://127.0.0.1:8000
echo.
echo Press CTRL+C to stop the server.
echo.

start http://127.0.0.1:8000

python -m uvicorn app.main:app --reload

pause