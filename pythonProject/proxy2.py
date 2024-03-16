from proxy_requests import ProxyRequests
from fake_headers import Headers
import requests
# from selenium import webdriver
from seleniumwire import webdriver
from urllib.error import URLError
import time
import datetime
from proxy_info import proxy_login, proxy_password

url_list = ["https://kvartiravkaluge.ru/", "https://domvkaluge.ru/", "https://uchastok40.ru/",
            "https://kvartiravdubae.ru/", "https://prodazhanedvizhimosti.ru/"]

options = {
    'proxy': {
        'http': f'http://{proxy_login}:{proxy_password}@193.233.62.99:9265',
        'https': f'https://{proxy_login}:{proxy_password}@193.233.62.99:9265',
        'no_proxy': 'localhost,127.0.0.1'
    }
}

proxies = {
    "https": f"http://{proxy_login}:{proxy_password}@193.233.62.99:9265",
}


def main():
    start = time.time()
    for _ in range(3):
        driver = webdriver.Chrome(seleniumwire_options=options)
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
    driver.quit()
    end = time.time()
    total_time = datetime.timedelta(seconds=(end - start))
    print(f"Total time: {total_time}")


if __name__ == "__main__":
    main()
