import socket
import time
import datetime

import requests
import ipaddress
from fake_useragent import UserAgent
import random
from selenium import webdriver

import main

url_list = main.links_name


def headers_ua_maker():
    ua = UserAgent()
    header = {
        "User-Agent": ua.random
    }

    return header


def make_ip_list():
    ip_list = [str(ip) for ip in ipaddress.IPv4Network("192.0.2.0/23")]
    # print(ip_list)

    return ip_list


def connect_new_ip(ip):
    socket.setdefaulttimeout(None)
    connection = str(ipaddress.ip_address(ip)) + "/" + str(255)

    return connection


def main():
    ip_list = make_ip_list()
    random_ip = random.choice(ip_list)
    for link in url_list:
        header = headers_ua_maker()
        connection = connect_new_ip(random_ip)
        # response = requests.get(url=link, headers=header,
        #                         proxies=dict(http='socks5://' + connection, https='socks5://' + connection))
        response = requests.get(url=link)
        if response.status_code != 200:
            random_ip = random.choice(ip_list)
            continue
        driver = webdriver.Chrome()
        driver.get(url=link)
        print(f"Link:{link}---IP:{random_ip}-----Status-operation:{response.status_code}-----{datetime.datetime.now()}")
        time.sleep(1)
        driver.quit()


if __name__ == "__main__":
    main()
