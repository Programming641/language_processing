import nltk

from importlib import import_module

avail_classes = { "Def_Count": "def_count", "Most": "def_count", "Everyday_Life": "def_date", 
                    "Daily_Life": "def_date", "Routine_Life": "def_date", "Human": "def_human", 
                    "People": "def_human", "Def_Time": "def_time", "Daily_Basis": "def_time", "Food": "def_food", 
                    "Meal": "def_food", "Day": "def_date", "Def_In": "def_common_word", "Def_A": "def_common_word", "Some": "def_count",
                    "Key": "def_common_vocab1", "Keys": "def_common_vocab1", "Phrase": "def_word", "Phrases": "def_word", "There": "def_common_word",
                    "Use": "def_common_vocab1", "Useful": "def_common_vocab1", "Def_Is": "def_common_word", "Def_Are": "def_common_word",
                    "Def_To": "def_common_word", "Learn": "def_common_vocab1", "That": "def_common_word", "English": "def_common_vocab1",
                    "Explain": "def_common_vocab1", "Your": "def_animate_pronoun", "Daily": "def_date", "Routine": "def_common_vocab1",
                    "Another": "def_common_word", "Person": "def_human" }


def _check_get_w_class(word):

   for each_w_class in avail_classes:
      if each_w_class[0:4].lower() == "def_":
         # "def_" is added in front of the word if this word might clash with the python reserved words.
         
         # get rid of "def_" and compare with the given word
         if each_w_class[4: len(each_w_class) ].lower() == word :
            print("available class is found for " + word )
            
            t_mod = import_module( "word_classes." + avail_classes[each_w_class] )
            
            t_class = getattr( t_mod , each_w_class )
            
            return { each_w_class: t_class }

      elif each_w_class.lower() == word:
         print("available class is found for " + word )
         
         t_mod = import_module(  "word_classes." + avail_classes[each_w_class] )
            
         t_class = getattr( t_mod , each_w_class )
            
         return { each_w_class: t_class }







# check if the given word is available as a class
def check_get_w_class(word):
   word = word.lower()
   
   # if the given word ends with s, this might be plural word. so search both words with or without "s".
   if word[len(word) - 1 : len(word) ] == "s":
      returned = _check_get_w_class(word)
      
      if returned:
         return returned
      else:
         word = word[0:len(word) - 1 ]
         
         returned = _check_get_w_class(word)
         
         return returned

   else:
      return _check_get_w_class(word)














