@echo off
where py >nul 2>nul
if %ERRORLEVEL%==0 (
  py -3 "%~dp0harness.py" %*
) else (
  python "%~dp0harness.py" %*
)
exit /b %ERRORLEVEL%
