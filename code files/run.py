import subprocess
import sys
import webbrowser
import time
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
VENV_DIR = PROJECT_DIR / ".venv"

if sys.platform == "win32":
    PYTHON = VENV_DIR / "Scripts" / "python.exe"
else:
    PYTHON = VENV_DIR / "bin" / "python"


def run_command(command):
    print(f"\n> {' '.join(map(str, command))}")
    subprocess.check_call(command, cwd=PROJECT_DIR)


def main():
    print("=" * 50)
    print("             FITBUDDY AI")
    print("=" * 50)

    # Create virtual environment
    if not VENV_DIR.exists():
        print("\nCreating virtual environment...")
        subprocess.check_call(
            [sys.executable, "-m", "venv", str(VENV_DIR)],
            cwd=PROJECT_DIR
        )

    # Install dependencies
    print("\nInstalling required packages...")
    run_command([
        str(PYTHON),
        "-m",
        "pip",
        "install",
        "-r",
        "requirements.txt"
    ])

    # Start FastAPI server
    print("\nStarting FitBuddy...")
    print("\nOpen: http://127.0.0.1:8000")
    print("API Docs: http://127.0.0.1:8000/docs")
    print("\nPress CTRL+C to stop the server.\n")

    # Open browser after a short delay
    def open_browser():
        time.sleep(2)
        webbrowser.open("http://127.0.0.1:8000")

    import threading
    threading.Thread(target=open_browser, daemon=True).start()

    subprocess.call([
        str(PYTHON),
        "-m",
        "uvicorn",
        "app.main:app",
        "--reload"
    ], cwd=PROJECT_DIR)


if __name__ == "__main__":
    main()