import json
import os
from const import PATH_SCRIPT_FORMAT

def txt_to_json(path_folder, prompt) -> dict:

    prompt = prompt.replace(" ","")
    path_txt = os.path.join(path_folder, f"{prompt}.txt")
    save_path = os.path.join(path_folder, f"{prompt}.json")

    with open(path_txt, 'r', encoding='utf-8') as txt_file:
        lines = txt_file.readlines()

    with open(PATH_SCRIPT_FORMAT, "r", encoding="utf-8") as json_file:
        script_dict = json.load(json_file)

    filter_lines = [item for item in lines if item and not str(item).isspace()]

    for line in filter_lines:
        if "장면 " in line:
            scene_num = f"scene_{int(line.split()[1][0])}"
        if "- 사진 1" in line:
            script_dict[scene_num]["photo_1"] = line.split(":")[-1].strip()
        elif "- 사진 2" in line:
            script_dict[scene_num]["photo_2"] = line.split(":")[-1].strip()
        elif "보이스오버" in line:
            script_dict[scene_num]["voice"] = line.split(":")[-1].strip()
    
    with open(save_path, "w", encoding= "utf-8") as json_file:
        json.dump(script_dict, json_file, ensure_ascii=False, indent=2)

    print(f"스크립트가 {save_path} 경로에 성공적으로 저장되었습니다.")

    return script_dict