


# multiform words 
# data structure needed to determine the word form for the current multiform word
# t_wordname -> "name of multiword" t_word_become -> " this multiword becomes this form " ano_w_pos -> " position of another word "
# ano_w_form -> " another word form " 
# Explanation
# multiword becomes xxx form if the another word located at some position is yyy form
# "key" becomes adjective if the next word is noun
class Multiform_W():
   def set_multiform_w(self, t_wordname, t_word_become, ano_w_pos, ano_w_form ):
      self.t_wordname = t_wordname
      self.t_word_become = t_word_become
      self.ano_w_pos = ano_w_pos
      self.ano_w_form = ano_w_form





