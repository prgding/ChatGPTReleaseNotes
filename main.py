import re

import requests
from lxml import html


def get_html():
    res = requests.get('https://help.openai.com/en/articles/6825453-chatgpt-release-notes')
    return re.sub('[^\x20-\x7E]+', '', res.text)


def xpath():
    # 创建 lxml 的 HTML 解析器
    parser = html.HTMLParser()

    # 将 HTML 文件解析为 lxml 的 Element 对象
    root = html.fromstring(html_content, parser=parser)

    # 使用 xpath 获取元素
    elements = root.xpath('//*[@id="__next"]/main/div/div/section/div[2]/div/div[1]/div/article/div[1]/h2')
    lastest_note = elements[0].text_content()

    # 比对
    with open('old.txt', 'r') as f:
        old_note = f.read()
        if old_note != lastest_note:
            print('new note')
            with open('old.txt', 'w') as f1:
                f1.write(lastest_note)
        else:
            print('no new note')


if __name__ == '__main__':
    html_content = get_html()
    xpath()
