import webbrowser
import time
from requests import get
import random

url = ["https://kvartiravkaluge.ru/", "https://kvartiravkaluge.ru/#home", "https://kvartiravkaluge.ru/#onas",
       "https://kvartiravkaluge.ru/#buyrealty", "https://kvartiravkaluge.ru/#sellrealty",
       "https://kvartiravkaluge.ru/#novostroyki", "https://kvartiravkaluge.ru/#vtorichka",
       "https://kvartiravkaluge.ru/#komnaty", "https://domvkaluge.ru/", "https://domvkaluge.ru/#buyhouse",
       "https://domvkaluge.ru/#sellhouse", "https://domvkaluge.ru/#services", "https://domvkaluge.ru/#credit",
       "https://domvkaluge.ru/#presentation", "https://uchastok40.ru/", "https://uchastok40.ru/#home",
       "https://uchastok40.ru/#kalugaarea", "https://uchastok40.ru/#buyarea", "https://uchastok40.ru/#websites",
       "https://uchastok40.ru/#contacts", "https://kvartiravdubae.ru/", "https://kvartiravdubae.ru/#dubai",
       "https://kvartiravdubae.ru/#news", "https://kvartiravdubae.ru/#buyflat",
       "https://kvartiravdubae.ru/#sellflat", "https://kvartiravdubae.ru/#contacts",
       "https://prodazhanedvizhimosti.ru/", "https://prodazhanedvizhimosti.ru/#about",
       "https://prodazhanedvizhimosti.ru/#news", "https://prodazhanedvizhimosti.ru/#sell",
       "https://prodazhanedvizhimosti.ru/#articles", "https://prodazhanedvizhimosti.ru/#contacts"]
ip = get("https://api.ipify.org").content.decode("utf8")
for item in url:
    time_sleep = random.choice(range(5))
    webbrowser.open(item)
    print(f'IP--- {ip}---- открыто {item}')
    time.sleep(time_sleep)
print("Te end!")
