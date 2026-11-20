import os
import shutil
import sys

def install():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src_skills = os.path.join(script_dir, 'skills')
    
    # Destination in user home
    user_home = os.path.expanduser('~')
    target_skills_dir = os.path.join(user_home, '.gemini', 'config', 'skills')
    os.makedirs(target_skills_dir, exist_ok=True)
    
    skills = [
        'textbook-pdf-splitter',
        'lesson-core-summarizer',
        'chalkboard-slides-planner',
        'notebooklm-video-generator'
    ]
    
    print("=" * 60)
    print("  AGY-Notebook 專案技能一鍵安裝腳本 (Antigravity Skills)")
    print("=" * 60)
    print(f"目標技能目錄: {target_skills_dir}\n")
    
    for s in skills:
        src = os.path.join(src_skills, s)
        dst = os.path.join(target_skills_dir, s)
        if os.path.exists(src):
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
            print(f"  [成功安裝] {s} -> {dst}")
        else:
            print(f"  [錯誤] 來源找不到: {src}")
            
    print("\n" + "=" * 60)
    print("  所有技能已成功安裝至 Antigravity 全域技能庫！")
    print("=" * 60)

if __name__ == '__main__':
    install()
