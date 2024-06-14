import os
import shutil
import requests
import sys
import subprocess
import urllib3


def check_network_connection():
    print("网络检测中...", end='')
    try:
        http = urllib3.PoolManager()
        response1 = http.request('GET', 'https://baidu.com')
        if response1.status != 200:
            print("ok")
            print("初始化...\n")
            return False
        else:
            print("ok")
            return True

    except Exception as e:
        print("ok")
        print("网络超时或无网络")


def check_network():
    if not check_network_connection():
        input("\n按任意键退出...")
        sys.exit()


check_network()
# 检测悟空更新,移除旧版文件,更新程序,启动程序
import lanzou
import wkfz

download_url = lanzou.href
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/116.0.0.0",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
}
if not os.path.exists(".\\wkfz"):
    os.mkdir(".\\wkfz")
folder_path = os.path.join(os.getcwd(), "wkfz")
files = os.listdir(folder_path)
repeat = 'no'
filename = ''
print("正在检测更新...", end='')
for file in files:
    filename = file[file.find('-') + 1:file.rfind('.')]
print("ok")
if filename == '':
    filename = "暂未安装"
print("\n当前版本：", filename)
print("官网版本：", wkfz.wk_v, "\n")

for file in files:
    if "wkfz-{}".format(wkfz.wk_v) in file:
        repeat = 'yes'
        print("已经是最新了...")

if repeat == 'no':
    if filename != "暂未安装":
        print('正在清理旧版程序...', end='')
    shutil.rmtree(".\\wkfz")
    os.mkdir(".\\wkfz")
    if filename != "暂未安装":
        print(" ok\n")
    print('更新中，请稍等...', end='')

    try:
        response = requests.get(url=download_url, headers=headers)
        response.raise_for_status()
        with open(".\\wkfz\\wkfz-{}.exe".format(wkfz.wk_v), "wb") as f:
            f.write(response.content)
            print(" ok")
    except requests.exceptions.RequestException as e:
        print(" error")
        print("\n下载链接获取错误导致下载或更新失败，请等待修复\n\n", str(e))
        input("\n按下任意键退出...")
        sys.exit()

print('\n玩的开心...')
command = '.\\wkfz\\wkfz-{}.exe'.format(wkfz.wk_v)

try:
    subprocess.Popen(command, shell=True, creationflags=subprocess.CREATE_NO_WINDOW, stdout=subprocess.DEVNULL,
                     stderr=subprocess.DEVNULL)
except OSError:
    pass

sys.exit()
