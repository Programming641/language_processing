import requests
import re

domain_url = "https://en.wikipedia.org"

machining_url = "https://en.wikipedia.org/wiki/Machine element"

title = "Machining"

res = requests.get(machining_url)
response = res.content

res_str = response.decode("utf-8")

filename = "html/" + title + ".html"

html_f = open(filename, mode='w', encoding="utf_8")
html_f.write(res_str)

lines = res_str.splitlines()

search = False
for line in lines:

   if "<body" in line.replace(" ", ""):
      # search begins
      search = True

   if "id=\"References\">References" in line.replace(" ", ""):
      # search ends
      break

   exclude_chars = [ "#", "jpg", "png", "edit" ]
   if search:
      href_ptn = "<\S.*href\S.*\"\S.*"
      results = re.findall(href_ptn, line)
      
      exclude_char_check = False
      for each_m in results:
         for check_char in exclude_chars:
            if check_char in each_m:
               # we don't want # in href because it is a link to the section of the current html page.
               # also we don't want link to the images
               # exclude edit too.
               exclude_char_check = True

         if not exclude_char_check:
            # link is not for section of the page, images or edit
            print(each_m)

            # now we proceed to extract reference pages
            # getting reference page between double quotations
            href_ptn = "href\s*=\s*\"\S+\""
            page_links = re.findall(href_ptn, each_m)
            
            for page_link in page_links:
               print(page_link)
               
               db_quo_1pos = page_link.find("\"")
               db_quo_2pos = page_link.find("\"", db_quo_1pos + 1)
               
               page_ref_path = page_link[db_quo_1pos + 1:db_quo_2pos ]
               
               print(page_ref_path)

               ref_page_url = domain_url + page_ref_path
               
               res = requests.get(ref_page_url)
               response = res.content

               res_str = response.decode("utf-8")
               
               
               
               filename = "html/" + page_ref_path.replace("/wiki/", "") + ".html"

               html_f = open(filename, mode='w', encoding="utf_8")
               html_f.write(res_str)
               html_f.close()

















