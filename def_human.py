


class Human:
   
   
   def activate(self, attribute):
      if attribute == "act":
         self.act = True
      if attribute == "think":
         self.think = True
      if attribute == "feel":
         self.feel = True
         
         
   def set_timespan(self, t_attr, time_obj ):
      if hasattr(self, "activity"):
         self.activity.update( { "activity_name" : t_attr, "timespan" : time_obj } )
      
      else:
         self.activity = { "activity_name" : t_attr, "timespan" : time_obj }
         


class People(Human):
   pass
   
   
   
   
   
   
   