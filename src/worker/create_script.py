import os
from openai import OpenAI
from create_folder import create_folder_with_today
from const import EXAMPLE, GPT_4

def script_to_txt(model_name: str = GPT_4, prompt: str = None) -> str:
    client = OpenAI(api_key="")

    folder_path = create_folder_with_today()

    example = EXAMPLE
    print("prompt: ", prompt)
    response = client.chat.completions.create(
        model= model_name,
        messages=[
            {"role": "system", "content": "[instruction]:당신은 인물의 재미있는 일화를 유튜브 쇼츠용 대본으로 작성해주는 전문가입니다."},
            {"role": "system", "content": "[instruction]:시청자의 흥미를 이끌 수 있는 강한 Hooking과 시청 도중 이탈이 일어나지 않도록 집중할 수 있게 작성해주세요."},
            {"role": "system", "content": "[instruction]:대본을 8개의 장면으로 나누어주세요."},
            {"role": "system", "content": "[instruction]:장면마다 사용할 사진 두개를 정해주세요."},
            {"role": "system", "content": "[instruction]:사진에 대한 설명을 'DALL-E 3'에게 전달해 줄 프롬프트 형식으로 매우 구체적으로 작성해주세요."},
            {"role": "system", "content": "[instruction]:나레이터가 사용할 보이스오버를 포함해주세요. 보이스오버는 제공해준 대본을 그대로 사용해주세요."},
            {"role": "system", "content": example},
            {"role": "user", "content": f"'{prompt}'이라는 인물에 대한 유명한 일화 하나를 소개 해주세요."},
        ]
    )

    str_to_text = response.choices[0].message.content

    prompt = prompt.replace(" ","")
    file_path = os.path.join(folder_path, f"{prompt}.txt")

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(str_to_text)

    print(f"스크립트가 {file_path} 경로에 성공적으로 저장되었습니다.")

    return folder_path