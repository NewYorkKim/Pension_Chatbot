import pandas as pd
import json
import requests
from bs4 import BeautifulSoup
import pymongo
from datetime import datetime
import schedule
import calendar
from threading import Timer
from dateutil.relativedelta import relativedelta
from haystack.document_stores import ElasticsearchDocumentStore

class DBUpdater:
    def __init__(self):
        self.connection = pymongo.MongoClient()
        self.db_pension = self.connection.pension

        print(self.db_pension)

        self.db_pension_news = self.db_pension.news

        print(self.db_pension_news)
        
    def __del__(self):
        self.client.close()
    
    def update_news(self, pages=10):
        now = datetime.today()
        last = now - relativedelta(years=1)

        now = now.strftime('%Y.%m.%d')
        last = last.strftime('%Y.%m.%d')
        
        search = ['ETF', 'IRP', '연금저축', '연금상품',
          '증권', '수익률', '수령', '납입', '한도',
          '이전', '사망', '노후', '출금', '세제',
          '연령', '세대', '2030', '퇴직',
          '국민연금', '연금개혁', '운용', '펀드',
          '종목', '가입', '수수료', '가입서류', '연금계좌',
          '원금보장', '비교', '해지']

        base = ['"개인연금"', '"퇴직연금"']
        subjects = base + [f'{b} +'+s for b in base for s in search]
        
        link_list = set()

        for row in self.db_pension_news.find():
            link_list.add(row['link'])
        
        for subject in subjects:
            for i in range(0, pages):
                start = 1 + (i*10)
    
                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/98.0.4758.102"}
                url = f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={subject}&sort=0&photo=0&field=0&pd=5&ds={last}&de={now}&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:1y,a:all&start={start}'

                res = requests.get(url)
                res.raise_for_status()

                soup = BeautifulSoup(res.text, 'lxml')

                ul = soup.find('ul', {'class': 'list_news'})
                links = ul.find_all('a', {'class': 'info'})

                for link in links:
                    if link not in link_list and '네이버' in link.text:
                        url_a = link['href']
                        try:
                            res_a = requests.get(url_a, headers=headers)
                            soup_a = BeautifulSoup(res_a.text, 'lxml')
                            title = soup_a.find('h2', {'class': 'media_end_head_headline'})
                            date = soup_a.find('span', {'class': 'media_end_head_info_datestamp_time _ARTICLE_DATE_TIME'})
                            article = soup_a.find('div', {'class': 'newsct_article'})
                            article = article.text.replace('\t\t', '\n\n').split('\n\n')
                            for p in article:
                                p = p.replace('\n', ' ').replace('\t', '').replace('\xa0', ' ').strip()
                                if len(p) < 30:
                                    continue
                                else:
                                    temp = dict()
                                    temp['title'] = title.text
                                    temp['date'] = date.text.split()[0][:-1]
                                    temp['article'] = p
                                    temp['link'] = url_a
                                    temp['subject'] = ''.join(subject.replace('"', '').split('+'))
                                    self.db_pension_news.insert_one(temp)
                                    link_list.add(url_a)
                        except:
                            pass
                
            print(f'{subject} is done!')
        print('Update: END')
        
    def delete_old_news(self):
        old = datetime.today() - relativedelta(years=1)
        old = old.strftime('%Y.%m.%d') 
        self.db_pension_news.delete_many({"date": {"$lt": old}}) 
        print('Delete: END')
        
    def unpdate_document_store(self):
        mongo_data = self.client['pension']['news'].find()
        df = pd.DataFrame(mongo_data)

        document_store = ElasticsearchDocumentStore(host='localhost', username='root', password='1111', index='document')
        document_store.delete_documents()
        
        news_list = []
        for i in range(len(df)):
            data = df.iloc[i]
            temp = {}
            article = data['article'].strip()
            temp['content'] = article
            temp['meta'] = {'title': data['title'], 'subject': data['subject'], 'link': data['link']}
            news_list.append(temp)
            
        document_store.write_documents(news_list)
        self.delete_old_news()

        print('MongoDB - ElasticSearch 연동이 완료되었습니다.')        
        
    def execute_daily(self):
        try:
            with open('config.json', 'r') as in_file:
                config = json.load(in_file)
                pages_to_fetch = config['pages_to_fetch']
        except FileNotFoundError:
            with open('config.json', 'w') as out_file:
                pages_to_fetch = 5
                config = {'pages_to_fetch': pages_to_fetch}
                json.dump(config, out_file)
                
        # self.unpdate_document_store(pages_to_fetch)

        schedule.every().day.at("03:00").do(self.unpdate_document_store(pages_to_fetch))
        
        # today = datetime.now()
        # lastday = calendar.monthrange(today.year, today.month)[1]
        
        # if today.month == 12 and today.day == lastday:
        #     nextday = today.replace(year=today.year+1, month=1, day=1, hour=3, minute=0, second=0)
        # elif today.day == lastday:
        #     nextday = today.replace(month=today.month+1, day=1, hour=3, minute=0, second=0)
        # else:
        #     nextday = today.replace(day=today.day+1, hour=3, minute=0, second=0)
            
        # diff = nextday - today
        # secs = diff.seconds
        
        # t = Timer(secs, self.execute_daily)
        
        # print(f"\n다음 업데이트 예정 시간: ({nextday.strftime('%Y-%m-%d %H:%M')})\n")
        
        # t.start()    