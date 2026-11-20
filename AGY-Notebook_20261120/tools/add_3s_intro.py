import os
import sys
import subprocess

def add_3s_silent_intro(input_file, output_file=None):
    if not os.path.exists(input_file):
        print(f"錯誤：找不到檔案 {input_file}")
        return False
    
    if output_file is None:
        base, ext = os.path.splitext(input_file)
        output_file = f"{base}_3秒片頭{ext}"
        
    print(f"正在為 {os.path.basename(input_file)} 加入 3 秒無聲片頭...")
    cmd = [
        'ffmpeg', '-y',
        '-i', input_file,
        '-filter_complex', '[0:v]tpad=start_duration=3:start_mode=clone[v];[0:a]adelay=3000|3000[a]',
        '-map', '[v]', '-map', '[a]',
        '-c:v', 'libx264', '-crf', '18', '-preset', 'veryfast',
        output_file
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"成功產出：{output_file}")
        return True
    else:
        print(f"處理失敗：\n{res.stderr[-500:]}")
        return False

if __name__ == '__main__':
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = r'D:\AGY-Notebook\三MV\01-計算工具與電腦誕生.mp4'
    add_3s_silent_intro(target)
