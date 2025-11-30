@echo off
echo Killing any existing processes on ports 8000 and 8501...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8000') do taskkill /PID %%a /F /T 2>nul
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8501') do taskkill /PID %%a /F /T 2>nul

timeout /t 1 /nobreak

echo.
echo Starting services...
start /B python run_services.py

timeout /t 4 /nobreak
echo.
echo Starting ngrok tunnels...
echo.

ngrok start --all

echo.
echo Tunnels started! Share these URLs with your friend:
echo https://dashboard.ngrok.com/status
pause
