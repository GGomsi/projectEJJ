import sys
import os
import requests
from create_script import script_to_txt
from create_json import txt_to_json
from create_image import generate_image
from const import PATH_SCRIPT


if len(sys.argv) > 2:
    input_prompt = " ".join(sys.argv[1:])
else:
    input_prompt = sys.argv[1]

# path_folder = "./script/2024-01-21/"
path_folder = script_to_txt(prompt=input_prompt)

script_dict = txt_to_json(path_folder=path_folder, prompt=input_prompt)

for scene in script_dict:
    dall_e_prompt = f"""
    [INFO]: The "EXAMPLE" below consists of prompts for images to be included in YouTube Shorts videos and voiceovers for each image.
    [INFO]: You are an expert who generates image prompts for photos in accordance with the content of the voiceover and the flow of the scene.
    [INFO]: Please create it like an actual photo.
    [EXAMPLE]:
    Scene 1
    Theme: Introduction to the character {input_prompt}.
    - Photo 1: {script_dict[scene]["photo_1"]}
    Voiceover: {script_dict[scene]["voice"]}
    """
    url = generate_image(prompt=dall_e_prompt)
    save_path = os.path.join(path_folder, f"{sys.argv[1]}_{scene}.jpg")
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(save_path, "wb") as file:
            file.write(response.content)
        print("이미지 저장 완료")
    except:
        print(f"{scene} 이미지 저장 실패")

print("photo_1 저장 완료")

for scene in script_dict:
    dall_e_prompt = f"""
    [INFO]: The "EXAMPLE" below consists of prompts for images to be included in YouTube Shorts videos and voiceovers for each image.
    [INFO]: You are an expert who generates image prompts for photos in accordance with the content of the voiceover and the flow of the scene.
    [INFO]: Please create it like an actual photo.
    [EXAMPLE]:
    Scene 1
    Theme: Introduction to the character {input_prompt}.
    - Photo 1: {script_dict[scene]["photo_2"]}
    Voiceover: {script_dict[scene]["voice"]}
    """
    url = generate_image(prompt=dall_e_prompt)
    save_path = os.path.join(path_folder, f"{sys.argv[1]}_{scene}_2.jpg")
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(save_path, "wb") as file:
            file.write(response.content)
        print("이미지 저장 완료")
    except:
        print(f"{scene} 이미지 저장 실패")

print("photo_2 저장 완료")
