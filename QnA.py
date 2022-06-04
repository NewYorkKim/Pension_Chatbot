import torch
import transformers
from transformers import AutoModelWithLMHead, PreTrainedTokenizerFast
from fastai.text.all import *
import fastai
import re
import pandas as pd


class Chatbot:
    def __init__(self):
        self.tokenizer = PreTrainedTokenizerFast.from_pretrained("jihae/kogpt2news",
        bos_token='</s>', eos_token='</s>', unk_token='<unk>',
        pad_token='<pad>', mask_token='<mask>')

        self.model = AutoModelWithLMHead.from_pretrained("jihae/kogpt2news")

    # def learn_tokenizer(self):
    #     #learn.model.save_pretrained("jihae/kogpt2news")
    #     tokenizer = PreTrainedTokenizerFast.from_pretrained("jihae/kogpt2news",
    #     bos_token='</s>', eos_token='</s>', unk_token='<unk>',
    #     pad_token='<pad>', mask_token='<mask>')
    #     return tokenizer 

    # def learn_model(self):
    #     model = AutoModelWithLMHead.from_pretrained("jihae/kogpt2news")
    #     return  model

    def get_answer(self, prompt):
        input_ids = self.tokenizer.encode(prompt)
        gen_ids = self.model.generate(torch.tensor([input_ids]),
                                  max_length=128,
                                  repetition_penalty=4.0,
                                  pad_token_id=self.tokenizer.pad_token_id,
                                  eos_token_id=self.tokenizer.eos_token_id,
                                  bos_token_id=self.tokenizer.bos_token_id,
                                  use_cache=True
                                )
        generated = self.tokenizer.decode(gen_ids[0,:].tolist())
        return generated

# ch = Chatbot()
# print(ch.get_answer('개인연금은 중도인출이 가능한가요?'))