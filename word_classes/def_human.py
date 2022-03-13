from word_classes.def_common_word import Word_Common



class Human(Word_Common):
   
   
   def activate(self, attribute):
      if attribute == "act":
         self.atr_act = True
      if attribute == "think":
         self.atr_think = True
      if attribute == "feel":
         self.atr_feel = True
         
         
   def set_timespan(self, t_attr, time_obj ):
      if hasattr(self, "activity"):
         self.activity.update( { "activity_name" : t_attr, "timespan" : time_obj } )
      
      else:
         self.activity = { "activity_name" : t_attr, "timespan" : time_obj }
         
   def eat(self, eaten ):
      self.do_eat = True
      self.eaten = eaten


class Person(Human):
   pass


class People(Human):

   def set_num(self, count):
      self.num = count
   
   
   
   
   
   