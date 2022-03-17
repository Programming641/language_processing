from lib import word_helpers, class_helpers



def look4noun( word_pos, words ):
   
   skip_words = [ {"skip_num": 0 }]
   words_obj = []
   
   next_w_pos_counter = 0
   resolved = False
   while not resolved:      
      
      
      next_cl_dict = class_helpers.check_get_w_class( words[word_pos + next_w_pos_counter] )
      next_cl_name = list(next_cl_dict.keys())[0]
      next_obj = next_cl_dict[ next_cl_name ]()
         
      skip_words[0]["skip_num"] += 1
      skip_words.append( word_pos + next_w_pos_counter )         
         
         
      words_obj.append(next_obj)
      

      next_w_form = word_helpers.get_word_form(words[ word_pos + next_w_pos_counter ], words)

      if next_w_form == "noun":
         # finish search

         return words_obj, skip_words    


      next_w_pos_counter += 1
      
      
      
      
      
      
      



