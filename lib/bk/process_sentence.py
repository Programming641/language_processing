import nltk

from word_forms import get_word_form
from class_helpers import check_w_class


class Sentence_Processor:

   @classmethod
   def process_sentence(self,sentence):
      words = nltk.word_tokenize(sentence)
      print (words)
      
      
      for each_token in words:
         w_form = get_word_form(each_token)
   
         
         print(w_form)

         check_w_class(each_token)










sentence = "Most people eat two or three meals in a day."


Sentence_Processor.process_sentence(sentence)