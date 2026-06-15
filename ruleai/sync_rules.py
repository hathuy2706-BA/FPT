import os
import time
import subprocess
import shutil

SOURCE_FILE = "/Users/hathuy/.gemini/GEMINI.md"
TARGET_DIR = "/Users/hathuy/Documents/FPT-1/ruleai"
TARGET_FILE_RAW = os.path.join(TARGET_DIR, "ruleai")
TARGET_FILE_MD = os.path.join(TARGET_DIR, "ruleai.md")

def get_file_content(path):
    if not os.path.exists(path):
        return ""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return ""

def sync_and_push():
    content = get_file_content(SOURCE_FILE)
    if not content:
        print("Source file is empty or cannot be read.")
        return False
        
    # Ghi file raw
    try:
        with open(TARGET_FILE_RAW, "w", encoding="utf-8") as f:
            f.write(content)
        
        # Ghi file markdown
        md_content = f"# Global Rules\n\n{content}"
        with open(TARGET_FILE_MD, "w", encoding="utf-8") as f:
            f.write(md_content)
            
        print("Rules synced successfully.")
        
        # Push lên GitHub
        os.chdir("/Users/hathuy/Documents/FPT-1")
        subprocess.run(["git", "add", "ruleai/ruleai", "ruleai/ruleai.md"], check=True)
        # Kiểm tra xem có gì thay đổi để commit không
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if status.stdout.strip():
            subprocess.run(["git", "commit", "-m", "docs: auto sync customization rules"], check=True)
            subprocess.run(["git", "push"], check=True)
            print("Pushed changes to GitHub.")
        else:
            print("No changes to commit.")
        return True
    except Exception as e:
        print(f"Error during sync/push: {e}")
        return False

def main():
    print(f"Starting rule sync watcher. Monitoring {SOURCE_FILE}...")
    last_mtime = 0
    if os.path.exists(SOURCE_FILE):
        last_mtime = os.path.getmtime(SOURCE_FILE)
        
    while True:
        try:
            if os.path.exists(SOURCE_FILE):
                current_mtime = os.path.getmtime(SOURCE_FILE)
                if current_mtime != last_mtime:
                    print(f"Detect change in {SOURCE_FILE}. Syncing...")
                    if sync_and_push():
                        last_mtime = current_mtime
            else:
                print(f"Warning: Source file {SOURCE_FILE} does not exist.")
        except Exception as e:
            print(f"Error in watcher loop: {e}")
        time.sleep(5)

if __name__ == "__main__":
    # Đồng bộ lần đầu khi chạy script
    sync_and_push()
    main()
