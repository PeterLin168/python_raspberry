import private
import requests
url = f'https://maker.ifttt.com/trigger/button_press1/with/key/{private.ifttt}?value1=31&value2=51'
print(private.ifttt)
#print(url)
r = requests.get(url)
if r.status_code == 200:
    print("發生成功")