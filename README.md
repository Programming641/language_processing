# language_processing

# get term definition for many words automatically from wikipedia!

# how to use

inside get_htmlpages.py, provide the wikipedia's page that you want to get definitions for. and change the title of the page.


![image](https://user-images.githubusercontent.com/56218301/155877506-076b08ee-36d9-448e-a309-49be14b337bd.png)



above example gets definitions for "Machine element" page

then, you can execute get_htmlpages.py

in windows 10

py get_htmlpages.py

it gets all reference html files in the page.

![image](https://user-images.githubusercontent.com/56218301/155876773-2b91af5d-4e9c-49ed-b86b-268e3472ea93.png)


then you execute the get_def_sent2.py

inside the get_def_sent2.py, choose the definition file name as shown in the below image

![image](https://user-images.githubusercontent.com/56218301/156565083-566cdae1-0b92-4c03-b8cd-9ac6682d8141.png)



py get_def_sent2.py

then definitions will be created in definitions folder.

![image](https://user-images.githubusercontent.com/56218301/155876448-f7720b0f-b775-409e-85b7-e69c150a275e.png)


then execute clean_def_sent.py

it will remove all html tags

![image](https://user-images.githubusercontent.com/56218301/156565532-d5b7a34b-dc51-422e-97c3-e2d5feb7d928.png)




# warning!

not perfect but works fairly good and it does find definitions well.

