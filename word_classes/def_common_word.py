
# all word classes should inherit Word_Common
class Word_Common:
   def set_w_form(self, w_form):
      self.w_form = w_form
      
   def get_w_form(self):
      return self.w_form


# in_words is a list containing word objects
class Def_In(Word_Common):
   def set_in(self, in_words):
      self.in_words = in_words
      
      
      
      
class Def_A(Word_Common):
   pass
      
      
      
      
      
      
      
      
      
      