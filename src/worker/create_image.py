from openai import OpenAI

"""
model (‘dall-e-2’ or ‘dall-e-3’): 모델 선택. default: dall-e-2

style (‘natural’ or ‘vivid’): vivid: hyper-real and dramatic images, 
                              natural: causes the model to produce more natural, less hyper-real looking images.
                              Defaults to ‘vivid’.

quality (‘standard’ or ‘hd’): The quality of the image that will be generated. ‘hd’ creates images with finer details and greater consistency across the image. Defaults to ‘standard’.

prompt (str): A text description of the desired image(s). The maximum length is 1000 characters. Required field.

n (int): The number of images to generate. Must be between 1 and 10. Defaults to 1. For dall-e-3, only n=1 is supported.

size (...): The size of the generated images. Must be one of 256x256, 512x512, or 1024x1024 for DALL·E-2 models. Must be one of 1024x1024, 1792x1024, or 1024x1792 for DALL·E-3 models.

response_format ('url' or 'b64_json'): The format in which the generated images are returned. Must be one of "url" or "b64_json". Defaults to "url".

user (str): A unique identifier representing your end-user, which will help OpenAI to monitor and detect abuse. Learn more.
"""


def generate_image(prompt: str):

    client = OpenAI(api_key="")

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        response_format="url",
        quality="standard",
        n=1,
    )

    # image_url = response.data[0].b64_json
    image_url = response.data[0].url

    print(image_url)

    return image_url
