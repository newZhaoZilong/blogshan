from django.test import TestCase

# Create your tests here.
import re

from datetime import datetime,timedelta,timezone
# from markdown.extensions.toc import TocExtension
import markdown
from blog.mytoc import TocExtension
from django.utils.text import slugify
with open('body.txt',mode='r',encoding='utf-8') as body_str:
    # print(body_str.read())
    body_txt = body_str.read()



md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
    TocExtension(baselevel = '3'),
        ])

md.convert(body_txt)
print(md.toc)