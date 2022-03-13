from word_classes.def_common_word import Word_Common

class Def_Day(Word_Common):
   pass

class Daily(Def_Day):
   pass


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