from concurrent.futures import ThreadPoolExecutor, wait

from threading import Lock

from http import HTTPStatus

import requests

import os

from pathlib import Path

from bs4 import BeautifulSoup

from urllib.request import urlopen

import string


def find_url_in_file(file_name, read_lock):
    path_to_dir = 'web_links/files_6_1'
    path_to_file = os.path.join(path_to_dir, file_name)
    with read_lock:
        with open(path_to_file, 'r') as file:
            lines = file.readlines()
            line = lines[0]
            url = line.strip()
        return url


def send_get_request(file_name, read_lock):
    url = find_url_in_file(file_name, read_lock)
    response = requests.get(url)
    if response.status_code == HTTPStatus.OK:
        return response.text
    else:
        return None


def check_secret_key_on_page(file_name, read_lock):
    response_text = send_get_request(file_name, read_lock)
    if response_text is not None:
        soup = BeautifulSoup(response_text, 'html.parser')
        line = soup.find('div', class_='secret-code')
        proxies = line.find_all('p')
        print(proxies)


def main():
    read_lock = Lock()
    path_to_dir = 'web_links/files_6_1'
    files = os.listdir(path_to_dir)
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = []
        for file_name in files:
            future = executor.submit(check_secret_key_on_page,
                                     file_name, read_lock)
            futures.append(future)
        
        done, not_done = wait(futures)

main()
