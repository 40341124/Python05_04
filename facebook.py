# coding:utf-8 
import requests

import json
import jieba
import re

#token有期限，因此日後要在存取必須修改
TOKEN = 'EAACEdEose0cBAHL3L9VuQ82UMqNWeKaNPiJA0lZAebPBLZCoVexsS23kxQAZBWWrHQhIz6PqAwJTv0RQAMUhKJfCuAYr0qpWn6mmKZCKQiPtY9iPZCEK61Abjm1CbeiKvPdakBIbjo2vAjdY0uyPplRLbBWZCKSgZByIIjLGasWEAZDZD'
#http://www.epochconverter.com/(設定為結至2015年底的全部文章)
res = requests.get("https://graph.facebook.com/me/posts?limit=100&since=1356969600&access_token="+TOKEN)
print(res.text)
