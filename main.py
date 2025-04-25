import requests
from bs4 import BeautifulSoup

class Douban:
    
    def __init__(self):
        self.url = 'https://movie.douban.com/top250'
        startnum = []
        for i in range(0, 226, 25):
            startnum.append(i)
        self.header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
        
    def get_top250(self):
        for start_index in start_num:
            start_index = str(start_index)
            html = requests.get(self.url,params={'start': start_index},headers=self.header)
            soup = BeautifulSoup(html,'html.parser')
            text = soup.select('#content > div > div.article > ol > li:nth-child(1) > div > div.info > div.hd > a > span.other')
            print(text)
            
            
            
if __name__ == __main__:
    db = Douban()
    db.get_top250()