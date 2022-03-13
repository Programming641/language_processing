import nltk

from word_classes import def_count, def_human, def_time, def_food, def_date, def_common_word, def_word, def_common_vocab1, def_animate_pronoun

avail_classes = { "Def_Count": def_count.Def_Count, "Most": def_count.Most, "Everyday_Life": def_date.Everyday_Life, 
                    "Daily_Life": def_date.Daily_Life, "Routine_Life": def_date.Routine_Life, "Human": def_human.Human, 
                    "People": def_human.People, "Def_Time": def_time.Def_Time, "Daily_Basis": def_time.Daily_Basis, "Food": def_food.Food, 
                    "Meal": def_food.Meal, "Day": def_date.Def_Day, "Def_In": def_common_word.Def_In, "Def_A": def_common_word.Def_A, "Some": def_count.Some,
                    "Key": def_common_vocab1.Key, "Keys": def_common_vocab1.Keys, "Phrase": def_word.Phrase, "Phrases": def_word.Phrases, "There": def_common_word.There,
                    "Use": def_common_vocab1.Use, "Useful": def_common_vocab1.Useful, "Def_Is": def_common_word.Def_Is, "Def_Are": def_common_word.Def_Are,
                    "Def_To": def_common_word.Def_To, "Learn": def_common_vocab1.Learn, "That": def_common_word.That, "English": def_common_vocab1.English,
                    "Explain": def_common_vocab1.Explain, "Your": def_animate_pronoun.Your, "Daily": def_date.Daily, "Routine": def_common_vocab1.Routine,
                    "Another": def_common_word.Another, "Person": def_human.Person }


def _check_get_w_class(word):

   for each_w_class in avail_classes:
      if each_w_class[0:4].lower() == "def_":
         # "def_" is added in front of the word if this word might clash with the python reserved words.
         
         # get rid of "def_" and compare with the given word
         if each_w_class[4: len(each_w_class) ].lower() == word :
            print("available class is found for " + word )
            
            return { each_w_class: avail_classes[each_w_class] }

      elif each_w_class.lower() == word:
         print("available class is found for " + word )
         
         return { each_w_class: avail_classes[each_w_class] }







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














