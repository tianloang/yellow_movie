#!coding:utf-8
import sys
import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':

    for i in range(0,3835):
        url = r'http://k68363.cn/hui3huang/mb5/k1uyhp2cw.php?ms=0&h='+str(i)+'';
        head = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
        }

        session = requests.session()
        requ = session.get(url,  headers=head)
        soup = BeautifulSoup(requ.content, 'lxml') # r.content就是响应内容，转换为lxml的bs对象[/color]
        imgs = soup.find_all(name='source', attrs={})  # 查找所有的img标签，并获取标签属性值（为列表类型）
        title = soup.find_all(name='h1', attrs={})

        s = imgs[0].get("src");
        # print(title[0].text)
        # print(s)
        sys.stdout = open('src.txt', mode='a', encoding='utf-8')
        print(title[0].text + ''+s)
        sys.stdout.close();


