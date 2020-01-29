import requests
import time
from bs4 import BeautifulSoup

trend_url_s = 'https://github.com/trending'

# r = requests.get(trend_url_s)
# f = open('trend.html','w')
# f.write(str(r.content))
# f.close()
f = open('trend.html', 'r')
d = f.read()
f.close()
content = d

html = BeautifulSoup(content, features='html.parser')

article_list = html.findAll('article')

# print(len(article_list))

#  名称 描述 星数 语言 作者
article_info = []
for i in range(len(article_list)):
    try:
        info = {'名称': '', '描述': '', '星数': '', '语言': '', '作者': ''}
        name_and_author = article_list[i].find('h1').find('a').attrs['href']
        info['名称'] = name_and_author.split('/')[2]
        info['作者'] = name_and_author.split('/')[1]
        try:
            info['描述'] = article_list[i].find('p').text.replace('\\n', '')
        except AttributeError:
            pass
        info['星数'] = article_list[i].findChildren('div')[1].findChildren('a')[0].text.replace('\\n','').replace(' ','')
        info['语言'] = article_list[i].find(lambda tag: tag.name=='span'
                                                       and 'itemprop' in tag.attrs
                                                       and tag['itemprop'] == 'programmingLanguage')
        article_info.append(info)
    except AttributeError:
        print('AttributeError')
print(int(time.time()))
print(article_info)
# print(len(article_info))
