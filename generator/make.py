#!/usr/bin/env python3

import concurrent.futures
import os
import os.path
import requests
import sys


def convert(raw_path, pool):
    path = os.path.abspath(raw_path)
    dir_name, file_name = os.path.dirname(path), os.path.basename(path)
    base_name, _ = os.path.splitext(file_name)
    dest_html = os.path.join(dir_name, base_name + '.html')
    dest_err = os.path.join(dir_name, base_name + '.txt')
    url = 'https://api.csswg.org/bikeshed/'
    save_err_to_txt = False

    with open(path, 'rb') as bs_file:
        bs_bytes = bs_file.read()

    common_args = {'files': {'file': bs_bytes}, 'headers': {'Accept-Charset': 'utf-8'}}
    html_future = pool.submit(lambda: requests.post(url, data={'output': 'html'}, **common_args))
    err = requests.post(url, data={'output': 'err'}, **common_args)

    if len(err.content) != 0:
        print(err.text)
        if save_err_to_txt:
            with open(dest_err, 'wb') as err_file:
                err_file.write(err.content)
    else:
        if os.path.exists(dest_err):
            os.remove(dest_err)
        print(f'Successfully built "{raw_path}"')

    html = html_future.result()
    if html.status_code == 200:
        with open(dest_html, 'wb') as html_file:
            html_file.write(html.content)


def main():
    jobs = sys.argv[1:]
    if len(jobs) != 1:
        print('Usage: python make.py file.bs')
        return

    pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    for _ in pool.map(lambda job: convert(job, pool), jobs):
        pass
    pool.shutdown()


if __name__ == '__main__':
    main()
