import os

from urllib.request import urlopen

from concurrent.futures import ThreadPoolExecutor, as_completed


urls = ['https://asyncio.ru/multithreading/zadachi/6.2/1/1XhKkbDD.txt',
        'https://asyncio.ru/multithreading/zadachi/6.2/1/7S2gWnLv.txt',
        'https://asyncio.ru/multithreading/zadachi/6.2/1/g277YKL0.txt',
        'https://asyncio.ru/multithreading/zadachi/6.2/1/I1HtO6Mq.txt',
        'https://asyncio.ru/multithreading/zadachi/6.2/1/IhOYyvOe.txt',
        'https://asyncio.ru/multithreading/zadachi/6.2/1/M1wlL6jq.txt',
        'https://asyncio.ru/multithreading/zadachi/6.2/1/M3ifGSqg.txt',
        'https://asyncio.ru/multithreading/zadachi/6.2/1/tEWbv18D.txt',
        'https://asyncio.ru/multithreading/zadachi/6.2/1/usMtkqVB.txt',
        'https://asyncio.ru/multithreading/zadachi/6.2/1/x2Ifki9M.txt']


def download_file(url):
    try:
        with urlopen(url, timeout=10) as connection:
            print(f'Рабочий url: {url}')
            return (connection.read(), url)
    except Exception as e:
        print(f'Нерабочий url: {url}')
        return (None, url)


def save_file(url, data, path):
    filename = os.path.basename(url)
    print(f'Название файла: {filename}')
    outpath = os.path.join(path, filename)
    print(f'Путь до файла: {outpath}')
    with open(outpath, 'wb') as file:
        file.write(data)
        print(f'Данные записаны в файл {filename}')
    return (outpath, filename)


def download_docs(urls, path):
    os.makedirs(path, exist_ok=True)
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for url in urls:
            future = executor.submit(download_file, url)
            futures.append(future)

        for future in as_completed(futures):
            data, url = future.result()
            print(f'Первым скачался: {url}')
            if data is None:
                continue
            outpath, filename = save_file(url, data, path)
            print(f'Первый скачанный файл: {filename}')
            break

PATH = 'web_links/files_7_2'

download_docs(urls, PATH)
