# import requests
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# from fake_headers import Headers
# from fake_useragent import UserAgent
# from bs4 import BeautifulSoup
#
# import urllib.request
# from urllib.error import URLError
# from warnings import filterwarnings, warn
#
# filterwarnings("ignore", category=InsecureRequestWarning)
#
# headers = Headers(headers=True).generate()
# ua = UserAgent().random
#
#
# def get_page(url, headers=None, params=None):
#     try:
#         response = requests.get(url, verify=False, headers=headers, params=params)
#         if response.status_code == 200:
#             return response.text
#     except URLError as e:
#         print(e.reason)
#     finally:
#         return None
#
#
# proxies = {
#     "http": "http://user:pass@127.0.0.1:8888", "https": "https://user:pass@127.0.0.1:8889"
# }
# headers = {
#     "User - Agent": f"{ua}"
# }
# for url in ["https://google.com", "https://yandex.ru"]:
#     get_page(url, headers=headers, params=None, proxies=proxies)
