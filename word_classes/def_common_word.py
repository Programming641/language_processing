from lib import word_helpers


# all word classes should inherit Word_Common
class Word_Common:
   def set_w_form(self, w_form):
      self.w_form = w_form
      
   def get_w_form(self, word, words):
      return word_helpers.get_word_form( word, words )


# in_words is a list containing word objects
class Def_In(Word_Common):
   def set_in(self, in_words):
      self.in_words = in_words
   
   
   def set_inorderto(self, words):
      self.inorderto = words

class Def_To(Word_Common):
   def set_to_noun( self, words ):
      self.to_noun = words
      
      
class Def_A(Word_Common):
   pass


class Def_Is(Word_Common):
   pass
   
   
class Def_Are(Word_Common):
   pass


class That(Word_Common):
   # noun that is/are adjective to verb.
   def set_n_is_are_adj_to_v(self, words ):
      self.n_is_are_adj_to_v = words



class There(Word_Common):
   def set_there_is_are( self, is_are_words ):
      self.is_are_words = is_are_words   
      
      
class Another(Word_Common):
   pass
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
      
      
      