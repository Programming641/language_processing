import os




def find_tagname_backward( target_str, pos ):

   print("inside find_tagname target_str " + target_str + " pos " + str(pos) )

   tag_name = ""
   letter_pos_counter = 0
   
   o_c_tag_letter_counter = 0

   
   while o_c_tag_letter_counter != 2:
      print("o_c_tag_letter_counter " + str(o_c_tag_letter_counter) )
      prev_letter = target_str[ pos - letter_pos_counter - 1 : pos - letter_pos_counter ] 
      if prev_letter == ">" or prev_letter == "<":
         o_c_tag_letter_counter += 1

         
      elif o_c_tag_letter_counter > 0:
         print("inside find_tagname prev_letter " + prev_letter )
         
         tag_name =  target_str[ pos - letter_pos_counter - 1 : pos - letter_pos_counter ] + tag_name[0: letter_pos_counter ]
         
         print("inside find_tagname tag_name " + tag_name )     
         
         
      letter_pos_counter += 1
   
   return tag_name, pos - letter_pos_counter - 1


dfile = "definitions/def3.txt"

if os.path.exists(dfile):
   os.remove(dfile)
   
df_opened = open(dfile, mode="a", encoding="utf_8" )
pfiles = os.listdir('html')

print(pfiles)

for each_pf in pfiles:

   # now we search for definition sentence. we first need to get title for this page.
   title = each_pf.replace("_", " ").replace(".html", "") 

   html_f =  open('html/' + each_pf, encoding="utf_8")
   lines = html_f.readlines()
   
   print("title " + title)
   
   search_wrd = "<b>" + title + "</b>"
   

   found = False
   for line in lines:
      if search_wrd.lower() in line.lower():
      
         search_wrd_pos = line.lower().find(search_wrd.lower()) 
         
         tag_name, search_wrd_pos = find_tagname_backward( line, search_wrd_pos )
         
         if search_wrd_pos < 3:
            # <b> title <b> is at the beginning of sentence
            print("found line" )
            print(line)
         
            df_opened.write(search_wrd + "\n" + line + "\n")
            found = True
         
         while not found:
         
            print("search_wrd_pos " + str(search_wrd_pos) )

            if tag_name == "p" or tag_name == "/":
               
               
               def_sentence = line[ search_wrd_pos + 1 : len(line) ]
            
               print("def_sentence" )
               print(def_sentence)
         
               df_opened.write(search_wrd + "\n" + line + "\n")
               found = True
               break
               
               
            tag_name, search_wrd_pos = find_tagname_backward( line, search_wrd_pos + 1 )
         
            print("tag_name " + tag_name )

      if found:
         break

df_opened.close()
































