from word_classes.def_common_word import Word_Common, Verb_Common



class Use(Word_Common):
   pass
   
   
   
class Useful(Use):
   # useful helps to raise verb's capacity because useful helps to do something.
   w_form = "adjective"
      
      
class Learn(Word_Common):
   category = "mental"
   sub_category = "put_in"
   w_form = "verb"
   
   
   
class English(Word_Common):
   category = "language"
   
   
class Explain(Word_Common, Verb_Common):
   # explain ( or probably many other verbs too ) has capacity rated by how well explain target is explained.
   pass
   
   
   

class Key(Word_Common):
   category = "importance"
   
   
class Keys(Key):
   pass
      

class Routine(Word_Common):
   pass
   
   
   
   
   
   
   
   
   
   
   
