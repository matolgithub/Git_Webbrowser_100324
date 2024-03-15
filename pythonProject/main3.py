import time

import requests
from fake_useragent import UserAgent
from ipaddress import IPv4Network
import random
from pprint import pprint
from selenium import webdriver
import datetime


def main():
    ip_http = "110.17.3.65"
    port_http = "3128"
    ip_https = "65.21.188.18"
    port_https = "8080"
    url = "https://uchastok40.ru/"
    proxies = {
        "http": f"http://{ip_http}:{port_http}",  # change the real proxy
        # "https": f"https://{ip_https}:{port_https}"  # change the real proxy
    }
    # ip = random.choice([str(ip) for ip in IPv4Network("192.0.2.0/23")])
    ua = UserAgent()
    header = {
        "User-Agent": ua.random
    }
    driver = webdriver.Chrome()
    driver.get(url=url)
    print(f"Link:{url}---IP:{ip_http}------{datetime.datetime.now()}")
    # print(ip_http, ip_https)
    # pprint(ua)
    # pprint(header)
    time.sleep(10)
    response = requests.get(url=url, headers=header, proxies=proxies)
    pprint(response.status_code)
    # pprint(response.text)
    time.sleep(30)
    driver.quit()


if __name__ == "__main__":
    main()
