import os
from datetime import datetime
from pytz import timezone
from const import PATH_SCRIPT


def create_folder_with_today() -> str:
    today = str(datetime.now(timezone("Asia/Seoul")))

    folder_path = os.path.join(PATH_SCRIPT, today.split(" ")[0])

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"폴더 {folder_path}가 생성 되었습니다.")
    else:
        print(f"{folder_path}가 이미 존재합니다.")

    return folder_path
