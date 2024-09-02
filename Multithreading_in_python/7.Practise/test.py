from threading import Thread, Lock

from concurrent.futures import ThreadPoolExecutor, wait

from http import HTTPStatus

import requests

import os

from bs4 import BeautifulSoup

from urllib.request import urlopen

import string

# req = requests.get('http://multithreading.ru/tasks/6.1/1/064b67.txt')

# print(req)


def send_get_request_to_url(url):
    try:
        response = requests.get(url)
        if response.status_code == HTTPStatus.OK:
            return response
        else:
            return None
    except:
        return None


def get_text_from_page(url):
    response = send_get_request_to_url(url)
    if response is not None:
        response_html = response.text
        soup = BeautifulSoup(response_html, 'html.parser')
        # return soup.prettify()
        return soup.get_text()
    return None


def create_file_name(url):
    filename = os.path.basename(url)
    return filename


def get_url(lock_urls_file, result_path, url_index):
    with lock_urls_file:
        with open(result_path, 'r') as file:
            lines = file.readlines()
            url = lines[url_index]
            url = url.strip()
            return url


def calc_words_count_per_page(url, results):
    page_text = get_text_from_page(url)
    if page_text is not None:
        # print(page_text)

        # for 

        page_text_without = page_text.replace('\n', ' ')
        # page_text_without = ','.join(page_text_without)
        # print(page_text)
        # page_text_without = page_text.strip()
        page_text_words_only = page_text_without.translate(str.maketrans('', '', string.punctuation))
        page_text_split = page_text_words_only.split(' ')
        for word in page_text_split:
            if word == '':
                page_text_split.remove(word)
        print(page_text_split)
        words_count = len(page_text_split)
        # print(words_count)

        filename = os.path.basename(url)
        results[filename] = words_count
        print(f'Файл {filename} обработан')
        return words_count
    return None


# def calc_words_count_per_page(url, results):
#     page_text = get_text_from_page(url)
#     if page_text is not None:
#         page_text_without = page_text.split('\n')
#         page_text_without = ','.join(page_text_without)
#         # print(page_text)
#         # page_text_without = page_text.strip()
#         page_text_words_only = page_text_without.translate(str.maketrans('', '', string.punctuation))
#         page_text_split = page_text_words_only.split(' ')
#         print(page_text_split)
#         words_count = len(page_text_split)
#         # print(words_count)

#         filename = os.path.basename(url)
#         results[filename] = words_count
#         print(f'Файл {filename} обработан')
#         return words_count
#     return None


def main():
    lock_urls_file = Lock()
    lock_dict = Lock()
    path = 'web_links/'
    filename = 'generated_links.txt'
    result_path = os.path.join(path, filename)
    results = {}

    valid_url = 'http://multithreading.ru/tasks/6.1/1/009879.txt'
    invalid_url = 'http://multithreading.ru/tasks/6.1/1/064b67.txt'

    calc_words_count_per_page(valid_url, results)
    calc_words_count_per_page(invalid_url, results)

    print(results)

    # Рабочая ссылка:
    # print(calc_words_count_per_page('http://multithreading.ru/tasks/6.1/1/009879.txt'))

    # Нерабочая ссылка:
    # print(words_count_per_page('http://multithreading.ru/tasks/6.1/1/064b67.txt'))

main()
