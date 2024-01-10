import os
import requests
import climage  
from os import unlink
from bardapi import Bard
import random
os.environ['_BARD_API_KEY'] = "Bard API Key (Read my readme.md file to get api key for free)"

message = input("Enter Bard Prompt: ")

answer = Bard().get_answer(str(message))


print(answer['content'])

image_links = answer.get('links', [])
if image_links:
    for i, image_link in enumerate(image_links):
        print("\033[1;3;30m", end="")
        print(f"Image Link {i+1}:", "\033[0m", end="")
        print("\033[1;3;30m", end="")
        print(image_link, "\033[0m")


        response = requests.get(image_link)
        if response.status_code == 200:

            random_filename = f"temp_{random.randint(1, 10000)}.png"


            with open(random_filename, "wb") as temp_file:
                temp_file.write(response.content)


            image_ansi = climage.convert(random_filename,
                                          is_truecolor=True,
                                          is_8color=False,
                                          is_256color=False,
                                          is_unicode=True,
                                          width=80)


            print(image_ansi)

            unlink(random_filename)
else:
    print("No image links found.")


other_links = answer.get('links', [])[1:4]
if other_links:
    print("\033[1;3;30m", end="")
    print("Other Links:", "\033[0m", end="")
    for link in other_links:
        print("\033[1;3;30m", end="")
        print(link, "\033[0m")


programming_language = answer.get('programming_language', None)
print("Programming Language:", programming_language)
