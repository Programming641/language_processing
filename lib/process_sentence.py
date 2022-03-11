import nltk
import sys

from lib import word_helpers, class_helpers, word_num_helpers
from word2number import w2n


class Sentence_Processor:

   @classmethod
   def process_sentence(self,sentence):
      words = nltk.word_tokenize(sentence)
      print (words)
      
      
      # list of python reserved words. these words can not be used as the function name.
      python_kw = [ "is", "in", "or" ]
      
      # initializing skip word list.
      # if previous word resolves the next word and making it unneccessary to call, mark it as skip so that this word method will not be called
      skip_words = {}
      
      # to make comparison simpler, convert each word to small letters.
      temp_counter = 0
      for each_token in words:
         words[temp_counter] = each_token.lower()
         temp_counter += 1
      
      
      
      for each_token in words:
         skip_words[each_token] = False
         
      sentence_results = []
      
      for each_token in words:
         # calling word methods
         
         if skip_words[each_token] == True:
            print("successfully skipping " + each_token + " method")
            continue
         
         if hasattr(Sentence_Processor, each_token ):
            token_func = getattr(Sentence_Processor, each_token )
            
            returned, ret_skip = token_func(words)
            
            sentence_results.append(returned)
            



         # check if the word is a number written as word
         elif each_token in word_num_helpers.word_nums or each_token in word_num_helpers.word_num_p or each_token in word_num_helpers.word_num_pos:
            print("word is a number " + each_token )
            token_func = getattr(Sentence_Processor, "lan_" + "number" )
            
            returned, ret_skip = token_func(words)
            
            sentence_results.append(returned)

     
         # check if the word one of the python reserved words
         elif each_token in python_kw:
            if hasattr(Sentence_Processor, "lan_" + each_token ):
               token_func = getattr(Sentence_Processor, "lan_" + each_token )
         
               returned, ret_skip = token_func(words)
               
               sentence_results.append(returned)


         if not ret_skip and returned and type(returned) == dict and returned.get("skip_obj"):
            skip_cl_name = type( returned.get("object") ).__name__
               
            # by convention in python, class name starts with capital letter, so convert all letters to lowercase to make comparison simpler
            skip_cl_name = skip_cl_name.lower()
               
            print("skipping " + skip_cl_name )
               
            if skip_cl_name in skip_words.keys():
               skip_words[skip_cl_name] = True
            else:
               skip_cl_name = skip_cl_name[0:1].upper() + skip_cl_name[1: len(skip_cl_name) ]
               skip_words[skip_cl_name] = True
                  
         if ret_skip:
            print("ret_skip " + str(ret_skip) )
               
            for each_ret_skip in ret_skip:
               # skipping skip_num {'skip_num': 4}. skip words are list of strings
               if type( each_ret_skip ) != dict and each_ret_skip in skip_words.keys():
                     skip_words[each_ret_skip] = True












            

      print("sentence_results ")
      print(sentence_results)
   
   def most(words):
      print("entered most method")
      
      # find if next word is noun.
      hit = False
      for word in words:
         if hit:
            w_form = word_helpers.get_word_form(word)
            
            # check if it's a noun. if it is, the word "most" goes with it.
            if w_form == "noun":
               # get this class, then instantiate it
               next_cl_dict = class_helpers.check_get_w_class(word)
               
               # class definition starts with capital letter. so capitalize the word's first letter
               word = word[0:1].upper() + word[1: len(word) ]
               
               next_obj = next_cl_dict[word]()
               
               # now get most class then instantiate it
               most_cl_dict = class_helpers.check_get_w_class("most")
               
               # in convention in python, class name starts with capital letter
               most_obj = most_cl_dict["Most"]().set_num(in_general=True)
               
               next_obj.set_num(most_obj)
               
               # now we have most and its associated word. return it. next_obj will be skipped
               return { "object": next_obj, "skip_obj": True }, None
               
               
            
            break
            
         if word == "most":
            hit = True
      
      
      
   def people(words):
      print("entered people method")
      
      
   def eat(words):
      print("entered eat method")
      # word eat has "what1" eat "what2". what1 is the eater. what2 is eaten.
      
      # find "what1" eater which is noun.
      
      # eaten word storage
      eaten_skip = [ {"skip_num": 0 }]
      
      # find position of word eat, then look up the previous word to see if it's noun. if it is, it is the eater.
      eat_pos = 0
      for word in words:
         if word == "eat":
            # word eat found. now see if previous word is noun
            prev_w_form = word_helpers.get_word_form(words[eat_pos - 1])
            
            if prev_w_form == "noun":
               # eater is found
               eater = words[eat_pos - 1 ]
               
               print("eater is " + eater)
      
               break
         else:
            eat_pos += 1
   
      if eater:
         eaten = []
         
         # now that eater is found, next is to find "eaten". "eaten" is also noun but it may be preceeded by number, conjunctions, or etc...
         for w_pos in range( eat_pos + 1 , len(words) ):
            # eaten candidate word form 
            eaten_cand_form = word_helpers.get_word_form( words[w_pos] )        
            
            if type(eaten_cand_form) == int or type(eaten_cand_form) == float:
               eaten_skip[0]["skip_num"] += 1
               eaten.append( { "number": eaten_cand_form } )
               eaten_skip.append( words[w_pos] )
               
            elif eaten_cand_form == "conjunction":
               eaten_skip[0]["skip_num"] += 1
               eaten.append( { "conjunction": words[w_pos] } )
               eaten_skip.append( words[w_pos] )
               
            elif eaten_cand_form == "noun":
               # "eater" and "eaten" are both found.
               
               eaten_skip[0]["skip_num"] += 1
               eaten.append( { "noun": words[w_pos] } )
               eaten_skip.append( words[w_pos] )
               
               # eater class should have "eat" behavior
               eater_cl_dict = class_helpers.check_get_w_class(eater)
               eater_cl_name = list(eater_cl_dict.keys())[0]
               eater_obj = eater_cl_dict[ eater_cl_name ]()
               
               # now that we have eater object instantiated, we proceed to get eaten object
               eaten_obj = word_helpers.fill_w_obj(eaten, "noun")
               
               print("inside eat method eaten_obj ")
               print(eaten_obj)
               
               eater_obj.eat(eaten_obj)
               
               print("inside eat method eater_obj")
               print(eater_obj) 
               
               return eater_obj, eaten_skip

         
      else:
         print("Encountered word \"eat\" comprehension problem. I don't understand this sentence")
   
   
   
   
   def lan_number(words):
      print("entered lan_number method")
      
   def lan_or(words):
      print("entered lan_or method" )
      
   def lan_in(words):
      # one of the most frequent use of the word "in" is with the noun, such as the sentence "in the forest", "in the studio" and so on.
      print("entered lan_in method")
      
      # storage for skipping fords
      in_skip_w = [ {"skip_num": 0 }]
      
      
      # find position of word in, then look up next word's form. keep looking until finding noun.
      in_pos = 0
      in_found = False
      for word in words:
         
         if in_found:
            # word in found. now see if next word is noun
            next_w_form = word_helpers.get_word_form(words[in_pos])
            
            if next_w_form == "noun":
               # target word for "in" is found
               in_target_w = words[in_pos ]
               in_skip_w[0]["skip_num"] += 1
               in_skip_w.append( words[in_pos ] )
               
               print("in_target_w is " + in_target_w)
               t_w_cl_dict = class_helpers.check_get_w_class(words[in_pos])
               t_w_cl_name = list(t_w_cl_dict.keys())[0]
               t_obj = t_w_cl_dict[ t_w_cl_name ]()        

               # preparing to send to "in" object
               in_cl_dict = class_helpers.check_get_w_class("in")
               in_cl_name = list(in_cl_dict.keys())[0]
               in_obj = in_cl_dict[ in_cl_name ]()

               # see if article was also included
               if 'article_obj' in locals():
                  in_obj.set_in( [ article_obj, t_obj ] )
                  
                  return in_obj, in_skip_w
                  
               else:
                  in_obj.set_in( [ t_obj ] )
                  
                  return in_obj, in_skip_w
      
               break

            elif next_w_form == "article":
               in_skip_w[0]["skip_num"] += 1
               in_skip_w.append( words[in_pos ] )
               
               article_cl_dict = class_helpers.check_get_w_class(words[in_pos])
               article_cl_name = list(article_cl_dict.keys())[0]
               article_obj = article_cl_dict[ article_cl_name ]()   
               
               
         if word == "in":
            in_found = True

         
         in_pos += 1   
         
      sys.exit()
      
   
   def a(words):
      print("entered a method")
   
















