from transformers import ElectraTokenizer
from haystack.document_stores import ElasticsearchDocumentStore
from haystack.nodes import BM25Retriever
from haystack.nodes import TransformersReader
from haystack.pipelines import ExtractiveQAPipeline

class NewsSearcher:  # 질문에 대한 답변과 출처 기사 링크 제공 (3개)
    def build_QA_model(self):
        tokenizer = ElectraTokenizer.from_pretrained('monologg/koelectra-small-v3-discriminator')
        document_store = ElasticsearchDocumentStore(host='localhost', username='root', password='1111', index='document')
        retriever = BM25Retriever(document_store=document_store)
        reader = TransformersReader(model_name_or_path='monologg/koelectra-small-v2-distilled-korquad-384', 
                                    tokenizer='monologg/koelectra-small-v2-discriminator', 
                                    context_window_size=500,
                                    max_seq_len=500, 
                                    doc_stride=300)
        
        pipe = ExtractiveQAPipeline(reader, retriever)
        
        return pipe
    
    def input_question(self):
        query = input('질문을 입력하세요: ')
        pipe = self.build_QA_model()
        prediction = pipe.run(query=query,
                              params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 3}})
        
        return prediction
    
    def get_answer(self):
        prediction = self.input_question()
        links = []
        
        for i in range(3):
            answer = prediction['answers'][i].answer
            context = prediction['answers'][i].context
            title = prediction['answers'][i].meta['title']
            link = prediction['answers'][i].meta['link']
            
            if link in links:
                continue
            
            print(f'\n=====추천 뉴스=====')
            
            start = prediction['answers'][i].offsets_in_context[0].start - 200
            if start < 0:
                start = 0
            end = prediction['answers'][i].offsets_in_context[0].start + 200

            cut = context[start:end]
        
            text = ''
            for line in context.split('. '):
                if line in cut and answer in line:
                    text += line+'. '
                    
            if len(text) == 0:
                print(answer)
            else:
                print(text)
                
            print(title)
            print(link)
            links.append(link)