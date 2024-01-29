
"""
{"role": "system", "content": "[instruction]:당신은 흥미로운 역사에 대해 유튜브 쇼츠용 대본을 작성해주는 작가입니다."},
{"role": "system", "content": "[instruction]:시청자의 흥미를 이끌 수 있는 강한 Hooking과 시청 도중 이탈이 일어나지 않도록 집중할 수 있게 작성해주세요."},
{"role": "system", "content": "[instruction]:대본을 8개의 장면으로 나누어주세요."},
{"role": "system", "content": "[instruction]:장면마다 사용할 사진 두개를 정해주세요."},
{"role": "system", "content": "[instruction]:사진에 대한 설명을 'DALL-E 3'에게 전달해 줄 프롬프트 형식으로 매우 구체적으로 작성해주세요."},
{"role": "system", "content": "[instruction]:나레이터가 사용할 보이스오버를 포함해주세요. 보이스오버는 제공해준 대본을 그대로 사용해주세요."},
{"role": "system", "content": example},
{"role": "user", "content": "{prompt} 역사에 대해 알려주세요."},
"""



"""

[INFO]: 아래의 "EXAMPLE"은 유튜브 쇼츠 영상에 들어갈 사진의 프롬프트와 각 사진별 보이스오버 입니다.
[INFO]: 당신은 보이스오버의 내용과 장면의 흐름에 맞게 각 사진의 프롬프트를 이미지로 생성해주는 전문가입니다.
[INFO]: 실제 사진처럼 만들어주세요.
[EXAMPLE]:
장면 1
- 사진 1: {script_dict["scene_1"]["photo_1"]}
- 사진 2: {script_dict["scene_1"]["photo_2"]}
보이스오버: {script_dict["scene_1"]["voice"]}

장면 2
-사진 1: {script_dict["scene_2"]["photo_1"]}
-사진 2: {script_dict["scene_2"]["photo_2"]}
보이스오버: {script_dict["scene_2"]["voice"]}

장면 3
-사진 1: {script_dict["scene_3"]["photo_1"]}
-사진 2: {script_dict["scene_3"]["photo_2"]}
보이스오버: {script_dict["scene_3"]["voice"]}

장면 4
-사진 1: {script_dict["scene_4"]["photo_1"]}
-사진 2: {script_dict["scene_4"]["photo_2"]}
보이스오버: {script_dict["scene_4"]["voice"]}

장면 5
-사진 1: {script_dict["scene_5"]["photo_1"]}
-사진 2: {script_dict["scene_5"]["photo_2"]}
보이스오버: {script_dict["scene_5"]["voice"]}

장면 6
-사진 1: {script_dict["scene_6"]["photo_1"]}
-사진 2: {script_dict["scene_6"]["photo_2"]}
보이스오버: {script_dict["scene_6"]["voice"]}

장면 7
-사진 1: {script_dict["scene_7"]["photo_1"]}
-사진 2: {script_dict["scene_7"]["photo_2"]}
보이스오버: {script_dict["scene_7"]["voice"]}

장면 8
-사진 1: {script_dict["scene_8"]["photo_1"]}
-사진 2: {script_dict["scene_8"]["photo_2"]}
보이스오버: {script_dict["scene_8"]["voice"]}
"""

"""
[INFO]: The "EXAMPLE" below consists of prompts for images to be included in YouTube Shorts videos and voiceovers for each image.
[INFO]: You are an expert who generates prompts for each image as images according to the content of the voiceover and the flow of the scene.
[INFO]: Please create it like an actual photo.
[EXAMPLE]:
Scene 1
- Photo 1: {script_dict["scene_1"]["photo_1"]}
- Photo 2: {script_dict["scene_1"]["photo_2"]}
Voiceover: {script_dict["scene_1"]["voice"]}

Scene 2
-Photo 1: {script_dict["scene_2"]["photo_1"]}
-Photo 2: {script_dict["scene_2"]["photo_2"]}
Voiceover: {script_dict["scene_2"]["voice"]}

Scene 3
-Photo 1: {script_dict["scene_3"]["photo_1"]}
-Photo 2: {script_dict["scene_3"]["photo_2"]}
Voiceover: {script_dict["scene_3"]["voice"]}

Scene 4
-Photo 1: {script_dict["scene_4"]["photo_1"]}
-Photo 2: {script_dict["scene_4"]["photo_2"]}
Voiceover: {script_dict["scene_4"]["voice"]}

Scene 5
-Photo 1: {script_dict["scene_5"]["photo_1"]}
-Photo 2: {script_dict["scene_5"]["photo_2"]}
Voiceover: {script_dict["scene_5"]["voice"]}

Scene 6
-Photo 1: {script_dict["scene_6"]["photo_1"]}
-Photo 2: {script_dict["scene_6"]["photo_2"]}
Voiceover: {script_dict["scene_6"]["voice"]}

Scene 7
-Photo 1: {script_dict["scene_7"]["photo_1"]}
-Photo 2: {script_dict["scene_7"]["photo_2"]}
Voiceover: {script_dict["scene_7"]["voice"]}

Scene 8
-Photo 1: {script_dict["scene_8"]["photo_1"]}
-Photo 2: {script_dict["scene_8"]["photo_2"]}
Voiceover: {script_dict["scene_8"]["voice"]}
"""
