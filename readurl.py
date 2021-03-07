# -*- coding: utf-8 -*-

'''
 useful functions for reading from url 
'''

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import chardet


def get_url(url, headers=None):
    if not headers:
        headers = {}

    try:
        req = Request(url, headers=headers)
        response = urlopen(req)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.:{}'.format(url))
        print('Error code: ', e.code)
        exit()
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
        exit()

    return response


#
# download HTML text
#
def get_html(url, headers=None, charset=None):
    response = get_url(url, headers)
    data_bytes = response.read()
    if charset:
        content = data_bytes.decode(charset)
    else:
        char_guessed = chardet.detect(data_bytes)
        content = data_bytes.decode(char_guessed['encoding'])
    return content


#
# download binary from url
#
def download_binary(filepath, url, headers=None):
    response = get_url(url, headers)
    f_out = open(filepath, 'wb')
    f_out.write(response.read())
    f_out.close()
    return response


# test
default_user_agent = {
    'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0'
}

if __name__ == '__main__':
    url = 'https://www.chosun.com'
    html = get_html(url, headers=default_user_agent)
    print(html)

    url = 'https://i.pinimg.com/736x/17/54/f1/1754f1f4a1b31a7bb1ddbbeb0d58140f--adam-hughes-dc-comic.jpg'
    response = download_binary('test.jpg', url, headers=default_user_agent)
