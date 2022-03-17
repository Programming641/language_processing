import nltk
import sys

from lib import word_helpers, class_helpers, word_num_helpers, sentence_helpers
from word2number import w2n


class Sentence_Processor:

   @classmethod
   def process(self,sentence):
      words = nltk.word_tokenize(sentence)
      print (words)
      
      
      # list of python reserved words. these words can not be used as the function name.
      python_kw = [ "is", "in", "or" ]
      
      # initializing skip word list.
      # if previous word resolves the next word and making it unneccessary to call, mark it as skip so that this word method will not be called
      skip_words = []
      
      # to make comparison simpler, convert each word to small letters.
      for each_token_pos in range( 0, len(words) ):
         words[each_token_pos] = words[each_token_pos].lower()
      
         skip_words.insert(each_token_pos, False )
         
      sentence_results = []
      
      word_pos = 0
      for each_token in words:
         # calling word methods
         
         if skip_words[word_pos] == True:
            print("successfully skipping " + each_token + " method")
            word_pos += 1
            continue
         
         if hasattr(Sentence_Processor, each_token ):
            token_func = getattr(Sentence_Processor, each_token )
            
            returned, ret_skip = token_func(word_pos, words)
            
            sentence_results.append(returned)
            



         # check if the word is a number written as word
         elif each_token in word_num_helpers.word_nums or each_token in word_num_helpers.word_num_p or each_token in word_num_helpers.word_num_pos:
            print("word is a number " + each_token )
            token_func = getattr(Sentence_Processor, "lan_" + "number" )
            
            returned, ret_skip = token_func(word_pos, words)
            
            sentence_results.append(returned)

     
         # check if the word one of the python reserved words
         elif each_token in python_kw:
            if hasattr(Sentence_Processor, "lan_" + each_token ):
               token_func = getattr(Sentence_Processor, "lan_" + each_token )
         
               returned, ret_skip = token_func(word_pos, words)
               
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
               if type( each_ret_skip ) != dict:
                     skip_words[each_ret_skip] = True

            # resetting ret_skip
            ret_skip = None

         word_pos += 1









            

      return sentence_results
   
   def most(word_pos, words):
      print("entered most method")
      
      # find if next word is noun.
      hit = False
      for word in words:
         if hit:
            w_form = word_helpers.get_word_form(word, words)
            
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
      
      
      
   def people(word_pos, words):
      print("entered people method")
      
      
   def eat(word_pos, words):
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
            prev_w_form = word_helpers.get_word_form(words[eat_pos - 1], words)
            
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
            eaten_cand_form = word_helpers.get_word_form( words[w_pos], words )        
            
            if type(eaten_cand_form) == int or type(eaten_cand_form) == float:
               eaten_skip[0]["skip_num"] += 1
               eaten.append( { "number": eaten_cand_form } )
               eaten_skip.append( w_pos )
               
            elif eaten_cand_form == "conjunction":
               eaten_skip[0]["skip_num"] += 1
               eaten.append( { "conjunction": words[w_pos] } )
               eaten_skip.append( w_pos )
               
            elif eaten_cand_form == "noun":
               # "eater" and "eaten" are both found.
               
               eaten_skip[0]["skip_num"] += 1
               eaten.append( { "noun": words[w_pos] } )
               eaten_skip.append( w_pos )
               
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
   
   
   
   
   def lan_number(word_pos, words):
      print("entered lan_number method")
      
   def lan_or(word_pos, words):
      print("entered lan_or method" )
      
   def lan_in(word_pos, words):
      # one of the most frequent use of the word "in" is with the noun, such as the sentence "in the forest", "in the studio" and so on.
      print("entered lan_in method")

      
      # storage for skipping words
      in_skip_w = [ {"skip_num": 0 }]


      # preparing "in" object
      in_cl_dict = class_helpers.check_get_w_class("in")
      in_cl_name = list(in_cl_dict.keys())[0]
      in_obj = in_cl_dict[ in_cl_name ]() 


      
      ano_w_counter = 1
      # see if next word is noun
      next_w_form = word_helpers.get_word_form(words[word_pos + ano_w_counter], words)
      
      print("next word is " + words[word_pos + ano_w_counter] )

      # check if it is subordinating conjunction "in order to"
      if words[word_pos + ano_w_counter] == "order" and words[word_pos + ano_w_counter + 1] == "to":
         print("this is \"in order to\" ")
         
         # adding "order" to in_skip_w
         in_skip_w[0]["skip_num"] += 1
         in_skip_w.append( word_pos + ano_w_counter )
         
         ano_w_counter += 1
         # add "to" to in_skip_w
         in_skip_w[0]["skip_num"] += 1
         in_skip_w.append( word_pos + ano_w_counter )

         ano_w_counter += 1
         # next word should be verb that goes with "in order to" so get it.
         orderto_v_cl_dict = class_helpers.check_get_w_class(words[word_pos + ano_w_counter])
         orderto_v_cl_name = list(orderto_v_cl_dict.keys())[0]
         orderto_v_obj = orderto_v_cl_dict[ orderto_v_cl_name ]()
         orderto_list = [ orderto_v_obj ]

         # adding "verb"
         in_skip_w[0]["skip_num"] += 1
         in_skip_w.append( word_pos + ano_w_counter )

         in_obj.set_inorderto( orderto_list )       
         
         return in_obj , in_skip_w

      
      if next_w_form == "noun":

         in_skip_w[0]["skip_num"] += 1
         in_skip_w.append( word_pos + ano_w_counter )
         
         t_w_cl_dict = class_helpers.check_get_w_class(words[word_pos + ano_w_counter])
         t_w_cl_name = list(t_w_cl_dict.keys())[0]
         t_obj = t_w_cl_dict[ t_w_cl_name ]()
         
         print("t_obj is " + str(t_obj) )         







         # see if article was also included
         if 'article_obj' in locals():
            in_obj.set_in( [ article_obj, t_obj ] )
                  
            return in_obj, in_skip_w
                  
         else:
            in_obj.set_in( [ t_obj ] )
                  
            return in_obj, in_skip_w


      elif next_w_form == "article":
         in_skip_w[0]["skip_num"] += 1
         in_skip_w.append( word_pos + ano_w_counter )
               
         article_cl_dict = class_helpers.check_get_w_class(words[word_pos + ano_w_counter])
         article_cl_name = list(article_cl_dict.keys())[0]
         article_obj = article_cl_dict[ article_cl_name ]()   
               
               
         
      
   
   def a(word_pos, words):
      print("entered a method")
   


   def there(word_pos, words):
      print("entered there method")

      # find position of word "there"
      there_pos = word_helpers.get_word_pos("there", words )

      # storage for skipping words
      there_skip_w = [ {"skip_num": 0 }]

      there_words_obj = []
      
      next_w_pos_counter = 1
      # one of the most frequest usage of there is "there is" or "there are". so check if next word is "is" or "are" 
      if words[there_pos + next_w_pos_counter ] == "is" or words[there_pos + next_w_pos_counter ] == "are":
         print("next word to \"there\" is \"is\" or \"are\" ")
         
         there_skip_w[0]["skip_num"] += 1
         there_skip_w.append( there_pos + next_w_pos_counter )

         next_w_pos_counter += 1
         resolved = False
         while not resolved:
            # we expect noun for the "there is" or "there are"
            next_cl_dict = class_helpers.check_get_w_class(words[there_pos + next_w_pos_counter])
            next_cl_name = list(next_cl_dict.keys())[0]
            next_obj = next_cl_dict[ next_cl_name ]()
            
            there_skip_w[0]["skip_num"] += 1
            there_skip_w.append( there_pos + next_w_pos_counter )
            there_words_obj.append( next_obj )
         
            if hasattr(next_obj, "quantity_word") and next_obj.quantity_word:
               print("this is quantity word " )
               print(next_obj)
         
            elif next_obj.get_w_form( words[there_pos + next_w_pos_counter] , words ) == "noun":
               # noun is found.
         
               # get word "there" object and set there_is_are objects
               there_cl_dict = class_helpers.check_get_w_class(words[there_pos])
               there_cl_name = list(there_cl_dict.keys())[0]
               there_obj = there_cl_dict[ there_cl_name ]()               
         
               there_obj.set_there_is_are( there_words_obj )
               
               return there_obj, there_skip_w
         
            next_w_pos_counter += 1



   def that(word_pos, words):
      print("entered that method")
      
      # check if previous word is noun and next word is "is" or "are".
      # then this is "noun that is/are ..... clause.
      
      # find position of current method word "that"
      that_pos = word_helpers.get_word_pos("that", words )

      # storage for skipping words
      that_skip_w = [ {"skip_num": 0 }]
      words_obj = []
      
      # first we will check if previous word is noun and next word is either "is" or "are"
      prev_w_form = word_helpers.get_word_form(words[that_pos - 1], words)
      
      if prev_w_form == "noun" and words[that_pos + 1] == "is" or words[that_pos + 1] == "are":
         is_are_cl_dict = class_helpers.check_get_w_class( words[that_pos + 1] )
         is_are_cl_name = list(is_are_cl_dict.keys())[0]
         is_are_obj = is_are_cl_dict[ is_are_cl_name ]()

         that_skip_w[0]["skip_num"] += 1
         that_skip_w.append( that_pos + 1 )
         words_obj.append( is_are_obj )         
      
         # get next word
         next_cl_dict = class_helpers.check_get_w_class( words[that_pos + 2] )
         next_cl_name = list(next_cl_dict.keys())[0]
         next_obj = next_cl_dict[ next_cl_name ]()

         that_skip_w[0]["skip_num"] += 1
         that_skip_w.append( that_pos + 2 )
         words_obj.append( next_obj )          
      
         next_w_form = next_obj.get_w_form( words[that_pos + 2], words )
         
         if next_w_form == "adjective":
            print("next word " + str(next_obj) + " is adjective" )
      
            # now we have. "noun that is/are adjective .... so get next word.
            next_cl_dict = class_helpers.check_get_w_class( words[that_pos + 3] )
            next_cl_name = list(next_cl_dict.keys())[0]
            next_obj = next_cl_dict[ next_cl_name ]()
            
            
            that_skip_w[0]["skip_num"] += 1
            that_skip_w.append( that_pos + 3 )
            words_obj.append( next_obj )              
            
            

            if next_cl_name == "Def_To":
               # get next word. then we will have " noun that is/are adjective to verb.
               next_cl_dict = class_helpers.check_get_w_class( words[that_pos + 4] )
               next_cl_name = list(next_cl_dict.keys())[0]
               next_obj = next_cl_dict[ next_cl_name ]()   

               that_skip_w[0]["skip_num"] += 1
               that_skip_w.append( that_pos + 4 )
               words_obj.append( next_obj )  

               
      
               # preparing to set all word objects to that object
               that_cl_dict = class_helpers.check_get_w_class( words[that_pos] )
               that_cl_name = list(that_cl_dict.keys())[0]
               that_obj = that_cl_dict[ that_cl_name ]()

               # setting the clause "noun that is/are adjective to verb." to that object.
               that_obj.set_n_is_are_adj_to_v( words_obj )

               return  that_obj, that_skip_w 


   def your(word_pos, words):
      print("entered your method")
      

      # storage for skipping words
      your_skip_w = [ {"skip_num": 0 }]

      words_obj = []
      
      # get the word "your" object
      your_cl_dict = class_helpers.check_get_w_class( words[word_pos] )
      your_cl_name = list(your_cl_dict.keys())[0]
      your_obj = your_cl_dict[ your_cl_name ]()
     

      # looking for your what? so noun is the word to look for.

      
      next_w_pos_counter = 1
      resolved = False
      while not resolved:
      
         next_cl_dict = class_helpers.check_get_w_class( words[word_pos + next_w_pos_counter] )
         next_cl_name = list(next_cl_dict.keys())[0]
         next_obj = next_cl_dict[ next_cl_name ]()
         
         your_skip_w[0]["skip_num"] += 1
         your_skip_w.append( word_pos + next_w_pos_counter )         
         
         
         words_obj.append(next_obj)
      

         next_w_form = word_helpers.get_word_form(words[ word_pos + next_w_pos_counter ], words)

         if next_w_form == "noun":
            # finish search

            your_obj.set_your_noun( words_obj )


            return your_obj, your_skip_w






         next_w_pos_counter += 1



   def to(word_pos, words):
   
      print("entered to method")
      
      # get the word "to" object
      to_cl_dict = class_helpers.check_get_w_class( words[word_pos] )
      to_cl_name = list(to_cl_dict.keys())[0]
      to_obj = to_cl_dict[ to_cl_name ]()
     
      
      # look for noun. so it probably has the meaning of direction toward noun.
      words_obj, skip_obj = sentence_helpers.look4noun( word_pos + 1, words )
      
      to_obj.set_to_noun( words_obj )
      
      return to_obj, skip_obj

















