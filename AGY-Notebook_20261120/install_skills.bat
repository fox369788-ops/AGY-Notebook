@echo off
chcp 65001 >nul
echo ============================================================
echo   AGY-Notebook 專案技能一鍵安裝工具 (Antigravity Skills)
echo ============================================================
echo.

python "%~dp0install_skills.py"

echo.
pause
