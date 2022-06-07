from haystack.document_stores import ElasticsearchDocumentStore
from haystack.nodes import BM25Retriever
from haystack.nodes import TransformersReader
from haystack.pipelines import ExtractiveQAPipeline

class QAExtractor:  # 질문에 대한 답변만 출력 (1개) 
    def build_QA_model(self):
        document_store = ElasticsearchDocumentStore(host='localhost', username='root', password='1111', index='document')
        retriever = BM25Retriever(document_store=document_store)
        reader = TransformersReader(model_name_or_path='monologg/koelectra-small-v2-distilled-korquad-384', 
                                    tokenizer='monologg/koelectra-small-v2-discriminator', 
                                    context_window_size=500,
                                    max_seq_len=500, 
                                    doc_stride=300,
                                    use_gpu=2)
        
        pipe = ExtractiveQAPipeline(reader, retriever)
        
        return pipe
    
    def input_question(self):
        query = input('질문을 입력하세요: ')
        pipe = self.build_QA_model()
        prediction = pipe.run(query=query,
                              params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 1}})
        
        return prediction
    
    def get_answer(self):
        prediction = self.input_question()
        answer = prediction['answers'][0].answer
        context = prediction['answers'][0].context
        
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
            print(answer)
        else:
            print(text)