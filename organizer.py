import os
import shutil
from pathlib import Path
from datetime import datetime

# ===== 設定 =====
DOWNLOADS_FOLDER = Path.home() / "Downloads"

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "PDFs": [".pdf"],
    "ZIPs": [".zip", ".rar", ".7z"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Documents": [".docx", ".xlsx", ".pptx", ".txt"],
}

# =====分類フォルダ作成 =====
for category in FILE_CATEGORIES.keys():
    (DOWNROADS_FOLDER / category).mkdir(exist_ok = True)

(DOWNROADS_FOLDER / "others").mkdir(exist_ok = True)

def get_category(file_path):
    ext = file_path.suffix.lower()
  
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
          
    return "Others"
  

def move_files(file_path.destination_folder):
    destination = destination_folder / file_path.name

    # 同名ファイル対策
    if destination exists():
        timestamp =
datetime.now().strftime("%Y%M%D_%H%M%S")
        destination = destination_folder /
f"{file_path.stem}_{timestamp}{file_path.suffix}"

    shutil.move(str(file_path), str(destination))
    print(f"Moved: {file_path.name} ->
{destination_folder.name}")


def organize_downloads():
    if not DOWNLOADS.exists():
        print("Downloadsフォルダが見つかりません")
        return

    for item in DOWNLOADS.iterdir():

        # フォルダは無視
        if item.is_dir():
            continue
        category = get_category(item)
        destination_folder = DOWNLORDS_FOLDER / category
        move_file(item.destination_folder)
      

if __name__ == "__main__":
  print("=== downlord Folder Organaizer ===")
  organize_downloads()
  print("整理完了")
            print(f"移動: {file.name} → {folder_name}")

if __name__ == "__main__":
    organize_files()
