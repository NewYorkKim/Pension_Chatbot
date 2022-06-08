
from haystack.document_stores import ElasticsearchDocumentStore
from haystack.nodes import BM25Retriever
from haystack.nodes import TransformersReader
from haystack.pipelines import ExtractiveQAPipeline

class NewsSearcher:  # 질문에 대한 답변과 출처 기사 링크 제공 (3개)
    def build_QA_model(self):
        document_store = ElasticsearchDocumentStore(host='localhost', username='root', password='1111', index='document')
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
        prediction = pipe.run(query=query,
                              params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}})
        
        return prediction
    
    def get_answer(self, query):
        prediction = self.input_question(query)
        links = []
        top3 = []
        
        for i in range(5):
            output = {}
            answer = prediction['answers'][i].answer
            context = prediction['answers'][i].context
            title = prediction['answers'][i].meta['title']
            link = prediction['answers'][i].meta['link']
            
            if link in links:
                continue
                        
            start = prediction['answers'][i].offsets_in_context[0].start - 200
            if start < 0:
                start = 0
            end = prediction['answers'][i].offsets_in_context[0].start + 200

            cut = context[start:end]
        
            output = ''
            text = ''
            for line in context.split('. '):
                if line in cut and answer in line:
                    text += line+'. '
                    
            if len(text) == 0:
                output += answer + '...[더보기]<br><br>'
            else:
                output += text[:50] + '...[더보기]<br><br>'
                
            output += f'<a href={link} target="_blank">{title}</a>'
            top3.append(output)
            links.append(link)

            if len(top3) == 3:
                break

        return top3
        

# ns = NewsSearcher()
# print(ns.get_answer('개인연금은 중도인출이 가능한가요?'))
