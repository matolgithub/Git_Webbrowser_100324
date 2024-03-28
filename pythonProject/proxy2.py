import random

# from proxy_requests import ProxyRequests
# from fake_headers import Headers
# import requests
# # from selenium import webdriver
# from seleniumwire import webdriver
# from urllib.error import URLError
# import time
# import datetime
# from proxy_info import proxy_login, proxy_password
#
# url_list = ["https://kvartiravkaluge.ru/", "https://kvartiravkaluge.ru/#home", "https://kvartiravkaluge.ru/#onas",
#             "https://kvartiravkaluge.ru/#buyrealty", "https://kvartiravkaluge.ru/#sellrealty",
#             "https://kvartiravkaluge.ru/#novostroyki", "https://kvartiravkaluge.ru/#vtorichka",
#             "https://kvartiravkaluge.ru/#komnaty", "https://domvkaluge.ru/", "https://domvkaluge.ru/#buyhouse",
#             "https://domvkaluge.ru/#sellhouse", "https://domvkaluge.ru/#services", "https://domvkaluge.ru/#credit",
#             "https://domvkaluge.ru/#presentation", "https://uchastok40.ru/", "https://uchastok40.ru/#home",
#             "https://uchastok40.ru/#kalugaarea", "https://uchastok40.ru/#buyarea", "https://uchastok40.ru/#websites",
#             "https://uchastok40.ru/#contacts", "https://kvartiravdubae.ru/", "https://kvartiravdubae.ru/#dubai",
#             "https://kvartiravdubae.ru/#news", "https://kvartiravdubae.ru/#buyflat",
#             "https://kvartiravdubae.ru/#sellflat", "https://kvartiravdubae.ru/#contacts",
#             "https://prodazhanedvizhimosti.ru/", "https://prodazhanedvizhimosti.ru/#about",
#             "https://prodazhanedvizhimosti.ru/#news", "https://prodazhanedvizhimosti.ru/#sell",
#             "https://prodazhanedvizhimosti.ru/#articles", "https://prodazhanedvizhimosti.ru/#contacts"]
#
# options = {
#     'proxy': {
#         'http': f'http://{proxy_login}:{proxy_password}@193.233.62.99:9265',
#         'https': f'https://{proxy_login}:{proxy_password}@193.233.62.99:9265',
#         'no_proxy': 'localhost,127.0.0.1'
#     }
# }
#
# proxies = {
#     "https": f"http://{proxy_login}:{proxy_password}@193.233.62.99:9265",
# }
#
#
# def main():
#     start = time.time()
#     driver = webdriver.Chrome(seleniumwire_options=options)
#     circle = 1
#     while circle <= 1:
#         print(f"--------------Circle number {circle}----------------------")
#         for url in url_list:
#             num = 1
#             r = ProxyRequests(url)
#             list_ip = r.sockets
#             for ip in list_ip:
#                 try:
#                     header = Headers().generate()
#                     driver.get(url=url)
#                     response = requests.get(url=url, headers=header, proxies=proxies)
#                     print(f"{num}.---- IP:{ip}. Web: {url} ----- Status code: {response.status_code}-------{header}")
#                     num += 1
#                 except URLError as error:
#                     print(error.reason)
#                 finally:
#                     continue
#         circle += 1
#     driver.quit()
#     end = time.time()
#     total_time = datetime.timedelta(seconds=(end - start))
#     print(f"Total time: {total_time}")
#
#
# if __name__ == "__main__":
#     main()


from proxy_requests import ProxyRequests
from fake_headers import Headers
import requests
from seleniumwire import webdriver
from urllib.error import URLError
import time
import datetime

url_list = ["https://kvartiravkaluge.ru/", "https://kvartiravkaluge.ru/#home", "https://kvartiravkaluge.ru/#onas",
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

options = {
    'proxy': {
        'http': f'http://cxMca4:bJD0P6@193.233.62.99:9265',
        'https': f'https://cxMca4:bJD0P6@193.233.62.99:9265',
        'no_proxy': 'localhost,127.0.0.1'
    }
}

proxies = {
    "https": f"http://cxMca4:bJD0P6@193.233.62.99:9265",
}


def main():
    start = time.time()
    driver = webdriver.Chrome(seleniumwire_options=options)
    circle = 1
    while circle <= 1:
        print(f"--------------Circle number {circle}----------------------")
        for url in url_list:
            num = 1
            r = ProxyRequests(url)
            list_ip = r.sockets
            for ip in list_ip:
                try:
                    header = Headers().generate()
                    driver.get(url=url)
                    response = requests.get(url=url, headers=header, proxies=proxies)
                    print(f"{num}.---- IP:{ip}. Web: {url} ----- Status code: {response.status_code}-------{header}")
                    num += 1
                except URLError as error:
                    print(error.reason)
                finally:
                    continue
        circle += 1
    driver.quit()
    end = time.time()
    total_time = datetime.timedelta(seconds=(end - start))
    print(f"Total time: {total_time}")


if __name__ == "__main__":
    main()