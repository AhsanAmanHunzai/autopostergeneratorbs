
from itertools import count
from typing import final
from PIL import Image, ImageFont, ImageDraw 
from flask import Flask,render_template,request


title_font = ImageFont.truetype('Files\Raleway-Bold.ttf', 45)


job_text_url = request.args.get('post')
    
job_text = job_text_url
my_image = Image.open("Files\\1.jpg")
final_title=""
count_char=0
for char in job_text:
    if count_char == 21:
        final_title=final_title+char+'\n '
        count_char=0
        continue
    final_title = final_title + char
    count_char=count_char+1

job_text=final_title
print(final_title)
    


image_editable = ImageDraw.Draw(my_image)
image_editable.text((80,240), job_text, (224, 233, 244), font=title_font,align='center')
my_image.save("static/people_photo/result.jpg")