from word_classes.def_common_word import Word_Common


class Def_Count(Word_Common):
   word_type = "quantity"
   
   
   # one out of many. for example. 2 or 3. choices are 2, 3 but only one should be chosen
   def set_one_o_o_many( self, num_set=None , specified=None ):
      if specified:
         self.one_o_o_many = specified
      
      else:
         if num_set:
            # if number is not specified then just choose the random one
            self.one_o_o_many = num_set[0]
            
         else:
            # num_set is also None
            self.one_o_o_many = 1


class Most(Def_Count):

   def set_num(self, in_general=False ):
      self.in_general = in_general
      return self 
   



class Some(Def_Count):
   
   default_percentage = 30
   