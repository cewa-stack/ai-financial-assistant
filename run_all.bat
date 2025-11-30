@echo off
cd /d d:\ai_bots\ai_financial_assistant

echo Starting API on port 8000...
start "API Server" python api/main.py

timeout /t 3 /nobreak

echo Starting Dashboard on port 8501...
set STREAMLIT_SERVER_HEADLESS=true
start "Dashboard" python -m streamlit run app/streamlit_app.py

echo.
echo ==============================
echo API: http://localhost:8000
echo Dashboard: http://localhost:8501
echo ==============================
echo Press any key to close all windows
pause
taskkill /F /IM python.exe
