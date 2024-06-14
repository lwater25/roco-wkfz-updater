import wkfz
import requests
from bs4 import BeautifulSoup
import re

# 根据得出的蓝奏云链接推出蓝奏云直链
lanzou_url = wkfz.lanzou_url
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                  "Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/116.0.0.0"
}
body = ''
response = requests.get(url=lanzou_url, headers=headers)
content = response.content.decode("utf-8")
soup = BeautifulSoup(content, "html.parser")
scripts = soup.find_all("script")
for script in scripts:
    if "submit.href = " in script.text:
        body = script.text
matches1 = re.findall(r"submit.href =  (.*)", body)
result = ''
for match in matches1:
    result = match
str1, str2 = result.split(" + ")
matches2 = re.findall(r"{} = '(.*)';".format(str1), body)
for match in matches2:
    str1 = match
matches3 = re.findall(r"{} = '(.*)';".format(str2), body)
for match in matches3:
    str2 = match
href = str1 + str2
# print("理论蓝奏链接："+href)
