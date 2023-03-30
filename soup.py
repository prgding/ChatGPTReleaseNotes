from bs4 import BeautifulSoup

# 将上面给出的 HTML 字符串存储在变量中
with open('Notes.html', 'r') as f:
    html_string = f.read()

# 使用 BeautifulSoup 解析 HTML 字符串
soup = BeautifulSoup(html_string, 'html.parser')

# 查找所有 h2 标签
h2_tags = soup.find_all('h2')

# 遍历 h2 标签并打印出它们的文本内容
for h2 in h2_tags:
    if h2.text:
        print(h2.text)
