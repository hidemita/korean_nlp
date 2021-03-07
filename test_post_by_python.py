# -*- coding: utf-8 -*-

import requests, json
import argparse


def show_result(j):
    sentence = j["sentence"]
    norm = j["norm"]
    stem = j["stem"]
    result = j["result"]
    print(f'input: "{sentence}"')
    print(f' flag stem = {stem}')
    print(f' flag norm = {norm}')
    for e in result:
        print(e)


if __name__ == '__main__':
    # read command-line arguments
    desc = 'korean text morpheme analyzer test program by Okt.'
    ap = argparse.ArgumentParser(description=desc)
    ap.add_argument('-q',
                    '--query',
                    default='',
                    help='input sentence in Korean langualge')
    ap.add_argument('--url',
                    default="http://localhost:8080/test",
                    action='store_true',
                    help='Okt server url (default="http://localhost:8080/test")')
    ap.add_argument('-t',
                    '--test',
                    action='store_true',
                    help='test with example input')
    ap.add_argument('-v',
                    '--verbose',
                    action='store_true',
                    help='verbose output')
    args = ap.parse_args()

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    url = args.url
    if args.test:
        s = u'저는 내일 친구하고 영화를 봅니다.'
    else:
        s = args.query

    data = {'sentence': s}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    print(f'status:{r.status_code}')
    # TODO: r.ok into show_result. show_result shows error reulsts, too.
    if r.ok:
        show_result(r.json())

    data['norm'] = True
    r = requests.post(url, data=json.dumps(data), headers=headers)
    print(f'status:{r.status_code}')
    if r.ok:
        show_result(r.json())

    data['stem'] = True
    r = requests.post(url, data=json.dumps(data), headers=headers)
    print(f'status:{r.status_code}')
    if r.ok:
        show_result(r.json())
