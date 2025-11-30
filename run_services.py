#!/usr/bin/env python
import subprocess
import time
import os
import signal
import sys

os.chdir(r'd:\ai_bots\ai_financial_assistant')

api_process = None
streamlit_process = None

def start_api():
    global api_process
    print("Starting API server on port 8000...")
    api_process = subprocess.Popen(
        [sys.executable, 'api/main.py'],
        cwd=r'd:\ai_bots\ai_financial_assistant'
    )
    print(f"API PID: {api_process.pid}")

def start_streamlit():
    global streamlit_process
    print("Starting Streamlit dashboard on port 8501...")
    env = os.environ.copy()
    env['STREAMLIT_SERVER_HEADLESS'] = 'true'
    streamlit_process = subprocess.Popen(
        [sys.executable, '-m', 'streamlit', 'run', 'app/streamlit_app.py'],
        cwd=r'd:\ai_bots\ai_financial_assistant',
        env=env
    )
    print(f"Streamlit PID: {streamlit_process.pid}")

def cleanup(signum, frame):
    print("\nShutting down services...")
    if api_process:
        api_process.terminate()
    if streamlit_process:
        streamlit_process.terminate()
    time.sleep(1)
    sys.exit(0)

signal.signal(signal.SIGINT, cleanup)

try:
    start_api()
    time.sleep(3)
    start_streamlit()
    
    print("\n" + "="*50)
    print("Both services running!")
    print("API: http://localhost:8000")
    print("Dashboard: http://localhost:8501")
    print("Press Ctrl+C to stop")
    print("="*50 + "\n")
    
    while True:
        if api_process and api_process.poll() is not None:
            print("API crashed! Restarting...")
            start_api()
            time.sleep(2)
        
        if streamlit_process and streamlit_process.poll() is not None:
            print("Streamlit crashed! Restarting...")
            start_streamlit()
            time.sleep(2)
        
        time.sleep(5)
        
except Exception as e:
    print(f"Error: {e}")
    cleanup(None, None)
