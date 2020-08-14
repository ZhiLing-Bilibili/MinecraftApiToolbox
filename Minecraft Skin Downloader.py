import urllib.request
import urllib
import json
import base64 as base
import requests


SoftwareData = {"version":"1.1","name":"Minecraft Skin Downloader","creater":"msinfo32_exe","more_info":"This software can only download skin that people uploaded on 'minecraft.net'.","note":"Please connect to the Internet, otherwise an error will appear"}
SoftwareData_zh_cn = {"version":"1.1","name":"Minecraft 皮肤下载器","creater":"msinfo32_exe","more_info":"本软件只能下载用户上传至'Minecraft.net'的皮肤","note":"请连接至互联网，否则会出现报错"}
print(SoftwareData['name'] + "     " + SoftwareData_zh_cn['name'])
print("Version: " + SoftwareData['version'] + "                  版本： " + SoftwareData_zh_cn['version'])
print("By: " + SoftwareData['creater'] + "              制作者： " + SoftwareData_zh_cn['creater'])
print("Warning: " + SoftwareData['note'])
print("警告: " + SoftwareData_zh_cn['note'])
for i in range(6):
    print("")
id = input("国际版ID:")
url = 'https://api.mojang.com/users/profiles/minecraft/' + id
print("正在从MOJANG网站获取用户JSON")
#第一次JSON获取并解析
html = urllib.request.urlopen(url)
print("正在分析JSON")
hjson = json.loads(html.read())
url2 = 'https://sessionserver.mojang.com/session/minecraft/profile/' + hjson['id']
#第二次JSON获取并解析
print("正在从MOJANG获取带有皮肤信息的JSON")
html2 = urllib.request.urlopen(url2)
print("正在分析JSON")
hjson2 = json.loads(html2.read())
properties = hjson2['properties']
url3 = properties[0]['value']
#由于MOJANG的存储特性，在第二份JSON文件中含有被BASE64编码的另一份JSON文件，需要进行BASE64解码
print("正在BASE64解码")
#第三次JSON解析
hjson3 = json.loads(''.join(str(base.b64decode(url3).decode())))
skin_url = hjson3['textures']['SKIN']['url']
print("成功获取皮肤连接：" + skin_url)

#下载皮肤用代码
r=requests.get(skin_url)
urllib.request.urlopen(skin_url)
path = id + ".png"
print("正在下载皮肤文件(文件名:"+id+".png)")
with open(path,"wb") as f:
    f.write(r.content)
f.close()
print("Done! in: " + str(len(r.content)) + " millisecond")