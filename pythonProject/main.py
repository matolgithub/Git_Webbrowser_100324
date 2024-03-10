import webbrowser
import time
import datetime
from selenium import webdriver

driver = webdriver.Chrome()
file_name = "history.txt"


def write_file(text):
    with open(file_name, "a") as file:
        file.write(text)


def sleep_func(time_sec):
    time.sleep(time_sec)


def open_link(links_name):
    # webbrowser.open_new_tab(links_name)
    driver.get(links_name)
    result_text = f"open link: {links_name} in {datetime.datetime.now()}"
    print(result_text)
    write_file(result_text)


def close_link():
    driver.execute_script("window.close();")


def main():
    links_name = ["https://kvartiravkaluge.ru/", "https://domvkaluge.ru/", "https://uchastok40.ru/",
                  "https://kvartiravdubae.ru/", "https://prodazhanedvizhimosti.ru/"]
    for link in links_name:
        open_link(link)
        sleep_func(time_sec=2)
        close_link()
        result_txt = f"close link {link} in {datetime.datetime.now()}"
        print(result_txt)
        write_file("\n" + result_txt + "\n")


if __name__ == '__main__':
    main()
