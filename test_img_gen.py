# v1 : ne fonctionne pas

# from pyimagine import Arta
# from pyimagine.constants import Style

# # Initialize Imagine
# arta = Arta()
# arta.signupNewUser()

# # Generate from inspiration
# inspired_image = arta.infer(prompt="Create something amazing!", style=Style.REALISTIC_2)

# # Prompt from image
# original_image = open('image.jpg', 'rb').read()
# prompt_image = arta.image2text(original_image, language_code='en')

# prompt_image.save('ia_test.png')

# # And more...


# v2 = pareil, Eden AI c'est nul

# import json
# import requests

# headers = {"Authorisation":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYjM3YTY1N2UtYWRlMS00ZWViLThmMjEtOGQ0NDY3NzJjN2M3IiwidHlwZSI6ImFwaV90b2tlbiJ9.AOZRvMQcnLJ800YrgVtCiyJNVRfotU4js0wlwYOvalM" }

# url = "https://api.edenai.run/v2/image/generation"
# payload = {"providers" : "openai,stabilityai","text": "photograph on an squirrel on mars planet", "resolution" : "512x512"}

# response = requests.post(url, json = payload, headers=headers)
# result = json.loads(response.text)
# print(result)

# make sure you're logged in with `huggingface-cli login`
from torch import autocast
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained(
	"CompVis/stable-diffusion-v1-4", 
	use_auth_token=True
).to("cuda")

prompt = "a photo of an astronaut riding a horse on mars"
with autocast("cuda"):
    image = pipe(prompt)["sample"][0]  
    
image.save("astronaut_rides_horse.png")