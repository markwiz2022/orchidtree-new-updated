@echo off
echo Starting local server on http://localhost:8000
echo Close this window to stop the server.
python -m http.server 8000
pause
