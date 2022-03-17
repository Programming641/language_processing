from word_classes.def_common_word import Word_Common
from word_classes.def_count import Def_Count


class Def_Day(Word_Common):
   # timespan start and end hour, minutes, and seconds
   timespan = { "start_h": 0, "start_m": 0, "start_s": 0 , "end_h": 23, "end_m": 59, "end_s": 59 }

class Daily(Def_Day):
   day_num = 1

   


class Everyday_Life(Word_Common):
   def define(self, sentence, meaning ):
      if hasattr(self, "sentences" ):
         cur_sentence_num = len( self.sentences )
         self.sentences.update( { "sentence" + str(cur_sentence_num + 1) : sentence, "meaning" + str(cur_sentence_num + 1) : meaning } )
      else:
         self.sentences = { "sentence1" : sentence, "meaning1" : meaning }
         
   
class Daily_Life(Everyday_Life):
   pass

class Routine_Life(Everyday_Life):
   pass
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
