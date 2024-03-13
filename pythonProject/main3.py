import time

import requests
from fake_useragent import UserAgent
from ipaddress import IPv4Network
import random
from pprint import pprint
from selenium import webdriver


def main():
    url = "https://uchastok40.ru/"
    proxies = {
        "http": "http://127.0.0.1:8000",  # change the real proxy
        "https": "https://127.09.0.10:8080"  # change the real proxy
    }
    ip = random.choice([str(ip) for ip in IPv4Network("192.0.2.0/23")])
    ua = UserAgent()
    header = {
        "User-Agent": ua.random
    }
    pprint(ip)
    # pprint(ua)
    # pprint(header)
    response = requests.get(url=url, headers=header, proxies=proxies)
    pprint(response.status_code)
    # pprint(response.text)
    time.sleep(5)


if __name__ == "__main__":
    main()
