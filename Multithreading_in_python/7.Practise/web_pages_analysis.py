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


def calc_words_count_per_page(results, lock_dict, line_index, lock_urls_file, result_path):
    url = get_url(lock_urls_file, result_path, line_index)
    # print(url)
    page_text = get_text_from_page(url)
    if page_text is not None:
        # page_text_without = page_text.split('\n')
        # page_text_without = ','.join(page_text_without)
        page_text_without = page_text.replace('\n', ' ')
        page_text_words_only = page_text_without.translate(str.maketrans('', '', string.punctuation))
        page_text_split = page_text_words_only.split(' ')
        for word in page_text_split:
            if word == '':
                page_text_split.remove(word)
        words_count = len(page_text_split)
        # print(words_count)

        filename = os.path.basename(url)
        with lock_dict:
            results[filename] = words_count
        print(f'Файл {filename} обработан')
        return words_count
    return None


def main():
    lock_urls_file = Lock()
    lock_dict = Lock()
    path = 'web_links/'
    filename = 'generated_links.txt'
    result_path = os.path.join(path, filename)
    results = {}

    # url = 'http://multithreading.ru/tasks/6.1/1/009879.txt'

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = []
        for line_index in range(1000):
            future = executor.submit(calc_words_count_per_page,
                            results, lock_dict, line_index,
                            lock_urls_file, result_path)
            futures.append(future)
        done, not_done = wait(futures)

        total_sum = sum(results.values())
        print(total_sum)
    # Рабочая ссылка:
    # print(calc_words_count_per_page('http://multithreading.ru/tasks/6.1/1/009879.txt'))

    # Нерабочая ссылка:
    # print(words_count_per_page('http://multithreading.ru/tasks/6.1/1/064b67.txt'))

main()
