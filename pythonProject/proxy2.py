from proxy_requests import ProxyRequests
from fake_headers import Headers
import requests
from selenium import webdriver
from urllib.error import URLError
import random
import time
import datetime
from proxy_info import proxy_login, proxy_password

url_list = ["https://kvartiravkaluge.ru/", "https://domvkaluge.ru/", "https://uchastok40.ru/",
            "https://kvartiravdubae.ru/", "https://prodazhanedvizhimosti.ru/"]


def main():
    start = time.time()
    driver = webdriver.Chrome()
    num = 1
    url = random.choice(url_list)
    r = ProxyRequests(url)
    list_ip = r.sockets
    for ip in list_ip:
        try:
            header = Headers().generate()
            proxies = {
                "http": f"http://{proxy_login}:{proxy_password}@193.233.62.99:9265"
            }
            driver.get(url=url)
            response = requests.get(url=url, headers=header, proxies=proxies)
            print(f"{num}.---- IP:{ip}. Web: {url} ----- Status code: {response.status_code}-------{header}")
            num += 1
        except URLError as error:
            print(error.reason)
    driver.quit()
    end = time.time()
    total_time = datetime.timedelta(seconds=(end - start))
    print(f"Total time: {total_time}")


if __name__ == "__main__":
    main()
