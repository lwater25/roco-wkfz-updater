import requests
from bs4 import BeautifulSoup
import re
# 解析悟空官网，得出每周更新的蓝奏云链接
url = "http://www.5kfz.com/"

response = requests.get(url)

content = response.content.decode("utf-8")

soup = BeautifulSoup(content, "html.parser")

scripts = soup.find_all("script")
ps = soup.find_all("p")
download_rul = ''
wk_v = ''
for script in scripts:
    if "lanzou" in script.text:
        download_rul = script.text
for p in ps:
    if "当前版本" in p.text:
        wk_v = p.text
matches1 = re.findall(r"ver (.*) [|] 更", wk_v)
matches2 = re.findall(r'''domain [+] '(.*)" target''', download_rul)

result = ''
for match in matches2:
    result = match

for match in matches1:
    wk_v = match
lanzou_url = "https://pan.lanzoue.com" + '/tp' + result

# print("理论直链："+lanzou_url)
