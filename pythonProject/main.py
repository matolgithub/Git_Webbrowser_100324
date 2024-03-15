import random
import webbrowser
import time
import datetime
from selenium import webdriver
import logging

driver = webdriver.Chrome()
file_name = "history.txt"
links_name = ["https://kvartiravkaluge.ru/", "https://domvkaluge.ru/", "https://uchastok40.ru/",
              "https://kvartiravdubae.ru/", "https://prodazhanedvizhimosti.ru/"]


def write_file(text):
    logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")
    logging.info(text)
    # with open(file_name, "a") as file:
    #     file.write(text)


def sleep_func(time_sec):
    time.sleep(time_sec)


def open_link(links_name):
    # webbrowser.open_new_tab(links_name)
    driver.get(links_name)
    result_text = f"open link: {links_name} in {datetime.datetime.now()}"
    print(result_text[:-7])
    write_file(result_text)


def close_link():
    driver.execute_script("window.close();")


def main():
    total = 1
    start_time = time.time()
    start = datetime.datetime.now()
    print(f"Start: {start}."[:-8])
    for times in range(total):
        print(f"{times + 1} period!")
        for link in links_name:
            open_link(link)
            sleep_func(time_sec=1)
            close_link()
            result_txt = f"close link {link} in {datetime.datetime.now()}"
            print(result_txt[:-7])
            write_file(result_txt + "\n")
        if times == total - 1:
            end = datetime.datetime.now()
            end_time = time.time()
            total_time = end_time - start_time
            process_time = datetime.timedelta(seconds=total_time)
            print(f"End: {end}."[:-8])
            print(f"Total process time is: {process_time}."[:-8])
    sleep_func(time_sec=random.choice([1, 2, 3, 4, 5]))


if __name__ == '__main__':
    main()
