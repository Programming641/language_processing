import os



dfile = "definitions/def2.txt"

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
   
   search_wrds = [title]
   
   if title[len(title) - 1:len(title)].lower() == "s":
      # if title ends with "s", this title might be multiple word. so remove it to make it singular 
      print(title + " ends in s. so add singular form")
      search_wrds.append(title[:-1])
      
   found = False
   for line in lines:
      for search_wrd in search_wrds:
         if search_wrd.lower() + " is " in line.lower() or search_wrd.lower() + " are " in line.lower():
         
            df_opened.write(search_wrd + "\n" + line + "\n")
            found = True
            break
         
         elif search_wrd.lower() + "</b> is " in line.lower() or search_wrd.lower() + "</b> are " in line.lower():

            df_opened.write(search_wrd + "\n" + line + "\n")
            found = True
            break

      if found:
         break

df_opened.close()
































