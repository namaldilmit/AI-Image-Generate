import os
import openai

openai.api_key= ("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")

User_input=input("Enter you want picture here : ")

response = openai.Image.create(
    prompt=User_input,
    n=1,
    size="1024x1024"
)
image_url = response['data'][0]['url']

print(response['data'])
print(image_url)