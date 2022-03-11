import nltk
from lib import word_num_helpers, class_helpers
from word_classes.def_count import Def_Count
from word2number import w2n


nouns = [ "people", "meal", "meals", "day", "days" ]
adjectives = [ "most" ]
articles = [ "a", "the" ]
conjunctions = [ "or" ]



word_forms = { "noun":nouns, "adjective": adjectives, "article": articles, "conjunction": conjunctions }

# get target word's preceding word combinations
def get_t_w_prec_w_combi(words):
   # all target word's associated preceding word combinations
   # target word's preceding words combinations
   t_w_preceding_w_combi = {}
   
   temp_combi = {}
   for word in words:
      if word.get("number"):
         if "number" in temp_combi:
            temp_combi["number"] += 1
         else:
            temp_combi["number"] = 1
      
      if word.get("conjunction") and word["conjunction"] == "or":
         if "or" in temp_combi:
            temp_combi["or"] += 1
         else:
            temp_combi["or"] = 1
         
   if temp_combi.get("number"):
      if temp_combi.get("or"):
         t_w_preceding_w_combi["number_or"] = {"number": temp_combi.get("number"), "or": temp_combi.get("or")}

   print("t_w_preceding_w_combi " + str(t_w_preceding_w_combi) )
   return t_w_preceding_w_combi




def get_word_form(word):
   word = word.lower()

   for each_word_f in word_forms:
      if word in word_forms[each_word_f]:
         return each_word_f

      elif word in word_num_helpers.word_nums:
         return w2n.word_to_num(word)


# fill word object
def fill_w_obj(words, t_w_form):
   # if the t_w_form, which is target word form, is the noun, then we should get its all preceding associated words like 
   # adjective, number and so on...
   
   print("inside fill_w_obj words")
   print(words)
   
   # all target word's associated preceding word combinations
   # target word's preceding words combinations
   preceding_w_pair = get_t_w_prec_w_combi(words)
   
  
   # first, we have to move the target word form to the front of the list
   # so that we can easily get its associated preceding words in a loop
   target_pos = 0
   for word in words:
      if word.get(t_w_form):
         break
      else:
         target_pos += 1
   
   # deleting target word and inserting it to the first position.
   words.insert(0, words.pop(target_pos))
   
   #preceding word numbers
   prec_w_numbers = set()
   for word in words:
            
            
      if t_w_form == "noun" and word.get("noun"):
         # target word is noun
         
         t_w_cl_dict = class_helpers.check_get_w_class( word.get("noun") )
         print("inside fill_w_obj t_w_cl_dict " + str(t_w_cl_dict) )
         
         t_w_cl_name = list(t_w_cl_dict.keys())[0]
         t_w_obj = t_w_cl_dict[ t_w_cl_name ]()
         
         print("inside fill_w_obj t_w_obj " + str(t_w_obj) )
         
         # now we have target object, we proceed to get all its associated preceding words.
         

      if "number_or" in preceding_w_pair :
         # target word's preceding words are number and or
         if word.get("number"):
            prec_w_numbers.add( word.get("number") )
            
            preceding_w_pair["number_or"]["number"] -= 1
         
         if preceding_w_pair["number_or"]["number"] == 0:
         
            def_count_obj = Def_Count().set_one_o_o_many(prec_w_numbers)

            t_w_obj.set_num(def_count_obj)


            return t_w_obj














