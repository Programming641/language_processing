from word_classes.def_common_word import Word_Common


class Def_Count(Word_Common):
   quantity_word = True
   
   
   # one out of many. for example. 2 or 3. choices are 2, 3 but only one should be chosen
   def set_one_o_o_many( self, num_set ):
      self.one_o_o_many = num_set
      


class Most(Def_Count):

   def set_num(self, in_general=False ):
      self.in_general = in_general
      return self 
   



class Some(Def_Count):
   default_percentage = 30
   