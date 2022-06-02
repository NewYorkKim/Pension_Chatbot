import pandas as pd
from haystack.document_stores import ElasticsearchDocumentStore
from haystack.nodes import BM25Retriever
from haystack.nodes import TransformersReader
from haystack.pipelines import ExtractiveQAPipeline
import warnings

warnings.filterwarnings(action='ignore')

class NewsSearcher:  # 질문에 대한 답변과 출처 기사 링크 제공 (3개)
    # def __init__(self):
    #     df = pd.read_csv('./data/naver_news_all2.csv')
    #     document_store = ElasticsearchDocumentStore(host='localhost', username='root', password='1111', index='test')
    #     document_store.delete_documents()
        
    #     news_list = []
    #     for i in range(len(df)):
    #         data = df.iloc[i]
    #         temp = {}
    #         article = data['article'].strip()
    #         temp['content'] = article
    #         temp['meta'] = {'title': data['title'], 'subject': data['subject'], 'link': data['link']}
    #         news_list.append(temp)
            
    #     document_store.write_documents(news_list)
    #     print('MongoDB - ElasticSearch 연동이 완료되었습니다.')  

    def build_QA_model(self):
        document_store = ElasticsearchDocumentStore(host='localhost', username='root', password='1111', index='document')
        # document_store = ElasticsearchDocumentStore(host='localhost', username='root', password='1111', index='test')
        retriever = BM25Retriever(document_store=document_store)
        reader = TransformersReader(model_name_or_path='monologg/koelectra-small-v2-distilled-korquad-384', 
                                    tokenizer='monologg/koelectra-small-v2-discriminator', 
                                    context_window_size=500,
                                    max_seq_len=500, 
                                    doc_stride=300)
        
        pipe = ExtractiveQAPipeline(reader, retriever)
        
        return pipe
    
    def input_question(self, query):
        pipe = self.build_QA_model()
        # prediction = pipe.run(query=query,
        #                       params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 3}})
        prediction = pipe.run(query=query,
                              params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 1}})
        
        return prediction
    
    def get_answer(self, query):
        prediction = self.input_question(query)
        # links = []
        # outputs = []
        
        # for i in range(3):
        #     output = {}
        #     answer = prediction['answers'][i].answer
        #     context = prediction['answers'][i].context
        #     title = prediction['answers'][i].meta['title']
        #     link = prediction['answers'][i].meta['link']
            
        #     if link in links:
        #         continue
            
        #     print(f'\n=====추천 뉴스=====')
            
        #     start = prediction['answers'][i].offsets_in_context[0].start - 200
        #     if start < 0:
        #         start = 0
        #     end = prediction['answers'][i].offsets_in_context[0].start + 200

        #     cut = context[start:end]
        
        #     text = ''
        #     for line in context.split('. '):
        #         if line in cut and answer in line:
        #             text += line+'. '
                    
        #     if len(text) == 0:
        #         output['answer'] = answer + '...[더보기]'
        #     else:
        #         output['answer'] = text[:50] + '...[더보기]'
                
        #     output['title'] = title
        #     output['link'] = link
        #     outputs.append(output)
        #     links.append(link)

        # return outputs

        output = {}
        answer = prediction['answers'][0].answer
        context = prediction['answers'][0].context
        title = prediction['answers'][0].meta['title']
        link = prediction['answers'][0].meta['link']

        start = prediction['answers'][0].offsets_in_context[0].start - 200
        if start < 0:
            start = 0
        end = prediction['answers'][0].offsets_in_context[0].start + 200
        
        cut = context[start:end]

        text = ''
        for line in context.split('. '):
            if line in cut and answer in line:
                text += line+'. '

        if len(text) == 0:
            output["answer"] = answer + '...[더보기]'
        else:
            output["answer"] = text[:50] + '...[더보기]'

        output["title"] = title
        output["link"] = link
    
        return output
        

# ns = NewsSearcher()
# print(ns.get_answer('개인연금은 중도인출이 가능한가요?'))
