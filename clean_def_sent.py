import requests
import re
import sys


def find_closing_tagname( target_str, pos ):

   print("inside find_closing_tagname target_str " + target_str + " pos " + str(pos) )

   tag_name = ""
   found = False
   letter_pos_counter = 0

   
   while not found:
      prev_letter = target_str[ pos - letter_pos_counter - 1 : pos - letter_pos_counter ] 
      if prev_letter != " " and prev_letter != "<":
         print("inside find_closing_tagname prev_letter " + prev_letter )
         
         tag_name =  target_str[ pos - letter_pos_counter - 1 : pos - letter_pos_counter ] + tag_name[0: letter_pos_counter ]
         
         print("inside find_closing_tagname tag_name " + tag_name )
         
         
         
         letter_pos_counter += 1
      else:
         return tag_name

dfilename = "def3.txt"

dfile = "definitions/" + dfilename


df_opened = open(dfile, mode="r", encoding="utf_8" )

lines = df_opened.readlines()

debug_counter = 0

cleaned_dfile = "definitions/" + "cleaned_" + dfilename

c_df_opened = open(cleaned_dfile , mode="a", encoding="utf_8")

for sentence in lines:

   print("current sentence " )
   print(sentence)
   


   while "<" in sentence:
      tag_open_pos = sentence.find("<")
      tag_close_pos = sentence.find(">")
      print("tag_o_pos " + str(tag_open_pos) )
      print("tag_close_pos " + str(tag_close_pos) )
   
      # finding tag name
   
      # space after opening tag
      sp_after_tag_o = sentence.find(" ", tag_open_pos)
   
      print("sp_after_tag_o " + str(sp_after_tag_o) )
   
      if sp_after_tag_o < tag_close_pos:
         # if space comes before closing tag, then it means that tag name is only letter and surround by space or it consists of two or more letters.
         tag_name = sentence[ tag_open_pos + 1 : sp_after_tag_o  ]
      
         print("tag_name " + tag_name )
      
         if tag_name.strip() == "sup" or tag_name.strip() == "style":
            # delete all letters from sup opening tag to the sup closing tag.
         
            closing_tag_found = False
            while not closing_tag_found:   
               if tag_open_pos > 0:
                  sentence = sentence[0: tag_open_pos ] + sentence[ tag_close_pos + 1 : len(sentence) ]

               else:
                  sentence = sentence[tag_close_pos + 1 : len(sentence)]  


               tag_close_pos = sentence.find(">") 

               closing_tag_name_temp =  find_closing_tagname( sentence, tag_close_pos )      
            
               print("closing_tag_name_temp " + closing_tag_name_temp )
            
               if closing_tag_name_temp.strip() == "sup" or closing_tag_name_temp.strip() == "/sup":
               
                  if tag_open_pos > 0:
                     sentence = sentence[0: tag_open_pos ] + sentence[ tag_close_pos + 1 : len(sentence) ]

                  else:
                     sentence = sentence[tag_close_pos + 1 : len(sentence)]                 

                  break
               
               elif closing_tag_name_temp.strip() == "style" or closing_tag_name_temp.strip() == "/style":
               
                  if tag_open_pos > 0:
                     sentence = sentence[0: tag_open_pos ] + sentence[ tag_close_pos + 1 : len(sentence) ]

                  else:
                     sentence = sentence[tag_close_pos + 1 : len(sentence)]                 

                  break
                    
               else:
                  print()
                  print("sentence" )
                  print(sentence)
                  print("closing_tag_name_temp " + closing_tag_name_temp )
               

            continue
   
   
      if tag_open_pos > 0:
         sentence = sentence[0: tag_open_pos ] + sentence[ tag_close_pos + 1 : len(sentence) ]

      else:
         sentence = sentence[tag_close_pos + 1 : len(sentence)]

   print(sentence)

   c_df_opened.write(sentence)





c_df_opened.close()

df_opened.close()





















