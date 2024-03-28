# import random
# import time
# import datetime
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# file_name = "history.txt"
links_name = ["https://kvartiravkaluge.ru/", "https://kvartiravkaluge.ru/#home", "https://kvartiravkaluge.ru/#onas",
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
#
#
# def sleep_func(time_sec):
#     time.sleep(time_sec)
#
#
# def open_link(links_name):
#     driver.get(links_name)
#     result_text = f"open link: {links_name} in {datetime.datetime.now()}"
#     print(result_text[:-7])
#
#
# def close_link():
#     driver.execute_script("window.close();")
#
#
# def main():
#     total = 1
#     start_time = time.time()
#     start = datetime.datetime.now()
#     print(f"Start: {start}."[:-8])
#     for times in range(total):
#         print(f"{times + 1} period!")
#         for link in links_name:
#             open_link(link)
#             sleep_func(time_sec=1)
#             close_link()
#             result_txt = f"close link {link} in {datetime.datetime.now()}"
#             print(result_txt[:-7])
#         if times == total - 1:
#             end = datetime.datetime.now()
#             end_time = time.time()
#             total_time = end_time - start_time
#             process_time = datetime.timedelta(seconds=total_time)
#             print(f"End: {end}."[:-8])
#             print(f"Total process time is: {process_time}."[:-8])
#     sleep_func(time_sec=random.choice([1, 2, 3, 4, 5]))
#
#
# if __name__ == '__main__':
#     main()


# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://kvartiravkaluge.ru/")
# time.sleep(3)
# driver.execute_script("window.close();")

# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.connect(("8.8.8.8", 80))
# print(s.getsockname()[0])
# s.close()

# import http.client
#
# conn = http.client.HTTPConnection("ifconfig.me")
# conn.request("GET", "/ip")
# ip = conn.getresponse().read()
# print(ip)

# import http.client
#
# conn = http.client.HTTPConnection("ifconfig.me")
# conn.request("GET", "/ip")
# ip = conn.getresponse().read()
# print(ip)


from requests import get

ip = get('https://api.ipify.org').content.decode('utf8')
print('My public IP address is: {}'.format(ip))
