import nltk
import sys
from lib import word_num_helpers, class_helpers
from lib.multiform_w import Multiform_W

from word2number import w2n


nouns = [ "people", "meal", "meals", "day", "days", "phrase", "phrases", "english", "routine", "person", "persons" ]
verbs = [ "use", "learn", "explain" ]
pronouns = [ "your" ]
adjectives = [ "most", "useful", "daily", "another" ]
articles = [ "a", "the" ]
conjunctions = [ "or" ]

# word that can be two or more forms depending on next or previous word. for example, "key" can be used as noun but this can be adjective
# if next word is also noun such as in "key phrases".
multiforms = [ "key" ]

word_forms = { "noun":nouns, "adjective": adjectives, "article": articles, "conjunction": conjunctions, "multiform": multiforms }

# initialize Multiform_W objects
# this is read as follows
# example data is the following. "key" , "adjective" ,  "next_w" ,  "noun"
# if key word's next word is noun, key word becomes adjective.
multiform_words = []

multiform_data = [ [ "key", "adjective", "next_w", "noun" ] ]
multif_obj_counter = 0
for multiform_datum in multiform_data:
   multiform_words.append(  Multiform_W() )
   multiform_words[ multif_obj_counter ].set_multiform_w ( multiform_datum[0], multiform_datum[1] ,  multiform_datum[2] ,  multiform_datum[3] )

   multif_obj_counter += 1

print("initialized multiform_words ")
print(multiform_words)

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


def get_word_pos(target_w, words ):
   t_word_pos = 0
   for word in words:
      if target_w == word:
         break
      else:
         t_word_pos += 1
         
         
   return t_word_pos



def get_word_form(word, words):
   word = word.lower()
   
   # get target word position
   t_word_pos = 0
   for each_word in words:
      if each_word == word:
         break
      else:
         t_word_pos += 1

   for each_word_f in word_forms:
      if word in word_forms[each_word_f]:
      
         if each_word_f == "multiform":
            for each_multiform_w in multiform_words:
               if each_multiform_w.t_wordname == word:
                  # current word is the target word. check position of the depended word
                  if each_multiform_w.ano_w_pos == "next_w":
                     # get target word's next word form
                     t_w_ano_word_f = get_word_form( words[t_word_pos + 1], words )
                     
                     print("target word's next word form is " + t_w_ano_word_f )
                     
                     if t_w_ano_word_f == each_multiform_w.ano_w_form:
                        return each_multiform_w.t_word_become
                     
         else:
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
         
            from word_classes.def_count import Def_Count
         
            def_count_obj = Def_Count().set_one_o_o_many(prec_w_numbers)

            t_w_obj.set_num(def_count_obj)


            return t_w_obj














