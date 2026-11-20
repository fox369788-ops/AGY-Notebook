@echo off
chcp 65001 >nul
echo ============================================================
echo   NotebookLM MP4 一鍵加入 3 秒無聲片頭工具 (FFmpeg)
echo ============================================================
echo.

if "%~1"=="" (
    echo [提示] 請直接將要處理的 MP4 影片檔案「拖曳」放到此批次檔圖示上！
    echo 或處理目錄下的 01-計算工具與電腦誕生.mp4...
    if exist "%~dp001-計算工具與電腦誕生.mp4" (
        set "TARGET=%~dp001-計算工具與電腦誕生.mp4"
        goto :PROCESS
    )
    pause
    exit /b
)

set "TARGET=%~1"

:PROCESS
set "OUTNAME=%~dpn1_3秒片頭.mp4"
if "%~1"=="" set "OUTNAME=%~dp001-計算工具與電腦誕生_3秒片頭.mp4"

echo 正在處理影片: "%TARGET%"
echo 輸出目標檔名: "%OUTNAME%"
echo.
echo 處理中，請稍候（凍結第一格畫面 3 秒，並靜音 3 秒）...

ffmpeg -y -i "%TARGET%" -filter_complex "[0:v]tpad=start_duration=3:start_mode=clone[v];[0:a]adelay=3000|3000[a]" -map "[v]" -map "[a]" -c:v libx264 -crf 18 -preset veryfast "%OUTNAME%"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ============================================================
    echo [成功] 已成功加入 3 秒無聲片頭！
    echo 產出檔案：%OUTNAME%
    echo ============================================================
) else (
    echo.
    echo [錯誤] 處理失敗，請確認已安裝 FFmpeg。
)

pause
