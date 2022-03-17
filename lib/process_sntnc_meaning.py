
import sys

# postv -> post verb. can it come right after verb? 
sentence_patterns = [ { "pattern_id": "1", "class": "word_classes.def_common_word.There", "operation": "is_are_words", "postv": False }, 
                      { "pattern_id": "2", "class": "word_classes.def_common_word.That", "operation": "n_is_are_adj_to_v", "postv": True },
                      { "pattern_id": "3", "class": "word_classes.def_common_word.Def_In", "operation": "in_noun", "postv": True }, 
                      { "pattern_id": "4", "class": "word_classes.def_common_word.Def_In", "operation": "inorderto", "postv": True },                      
                      { "pattern_id": "5", "class": "word_classes.def_animate_pronoun.Your", "operation": "your_noun", "postv": True },
                      { "pattern_id": "6", "class": "word_classes.def_common_word.Def_To", "operation": "to_noun", "postv": True } ]
                      
                      
                      
                      


class Sentence_Meaning_Processor:
   def process(sentence_results):
   
   
      # determine sentence structure
      sntnc_struct = []   
   
      for each_sntnc_obj in sentence_results:

         obj_dict = each_sntnc_obj.__dict__
         
         
         for sntnc_ptn in sentence_patterns:
            if each_sntnc_obj.__module__ + "." + each_sntnc_obj.__class__.__name__  ==  sntnc_ptn["class"] and list(obj_dict.keys())[0] == sntnc_ptn["operation"]:
               print("current class " + sntnc_ptn["class"] + " operation " + sntnc_ptn["operation"] )
         
               sntnc_struct.append ( sntnc_ptn["pattern_id"] )
               break
         
         print()     

      print("sntnc_struct " + str(sntnc_struct) )
      sentence_counter = -1
      skip_sntnc_cmpnt = []
      # sentence noun
      sntnc_noun = {}
      
      # sentence graphs
      sntnc_grahs = {}
      sntnc_nodes = {}
      
      for each_sntnc_obj in sentence_results:
         obj_dict = each_sntnc_obj.__dict__
         sentence_counter += 1
         print()
         print("sentence component " + str( each_sntnc_obj ) )
         print( obj_dict )

         
         if sentence_counter in skip_sntnc_cmpnt:
            print("skipping " + str( each_sntnc_obj ) )
            continue
         
         for each_v in obj_dict.values():

            
            if type( each_v ) == list:

               if sntnc_struct[ sentence_counter ] == "1":
                  # existence words
                  sntnc_noun[ sentence_counter ] = each_v

                  break
            
               word_counter = -1
               for each_obj in each_v:
                  
                  word_counter += 1
                  cur_obj_fullname = each_obj.__module__ + "." + each_obj.__class__.__name__
                  print( cur_obj_fullname )

                  if sntnc_struct[ sentence_counter ] == "2":
                     if cur_obj_fullname == "word_classes.def_common_word.Def_Is" or cur_obj_fullname == "word_classes.def_common_word.Def_Are":
                        print("current object is either Is or Are")
                        continue
                              
                     if hasattr(each_obj, "w_form") and each_obj.w_form == "adjective":
                        print("current object is adjective")
                     
                        # current operation is n_is_are_adj_to_v. so get noun just before this.
                        ptn2_n = sntnc_noun[ sentence_counter - 1 ]
                     
                        print("ptn2_n " + str(ptn2_n) )
                     
                        if cur_obj_fullname == "word_classes.def_common_vocab1.Useful":
                           # current adjective is useful
                           print("current adjective is Useful")

                           what_is_useful = ptn2_n
                           usflsubj_gnodename = "useful_subj"
                           sntnc_nodes[usflsubj_gnodename] = what_is_useful
                           
                           useful_gnodename = "useful"
                           sntnc_nodes[useful_gnodename] = each_obj
                           
                           sntnc_grahs[ usflsubj_gnodename ] = set(  )
                           sntnc_grahs[ usflsubj_gnodename ].add( useful_gnodename )

                           # getting verb from "n_is_are_adj_to_v"
                           if each_v[ word_counter + 1 ].__module__ + "." + each_v[ word_counter + 1 ].__class__.__name__ == "word_classes.def_common_word.Def_To":
                              useful_for = [ each_v[ word_counter + 1 ], each_v[ word_counter + 2 ] ]
                              
                              
                              usflfor_gnodename = "useful_for"
                              sntnc_nodes[ usflfor_gnodename ] = useful_for
                              
                              sntnc_grahs[ useful_gnodename ] = set(  )
                              sntnc_grahs[ useful_gnodename ].add( usflfor_gnodename )
 
                              print("useful_for " + str(useful_for) )
                              
                              # check what kind of word the useful_for is
                              if len(useful_for) == 2 and useful_for[1].category == "mental" and useful_for[1].sub_category == "put_in":
                                 # check the sentence pattern of next sentence component.
                                 if  sntnc_struct[ sentence_counter + 1 ] == "3":
                                    mental_subject = [ sentence_results[ sentence_counter + 1 ] ]
                                    mental_subject = mental_subject + sentence_results[ sentence_counter + 1 ].__dict__["in_noun"]
                                    
                                    mentalsubj_gnodename = "mental_subj"
                                    sntnc_nodes[ mentalsubj_gnodename ] = mental_subject
                                    
                                    sntnc_grahs[ usflfor_gnodename ] = set(  )
                                    sntnc_grahs[ usflfor_gnodename ].add( mentalsubj_gnodename )
                                    
                                    print("mental_subject " + str(mental_subject) )
                                    
                                    

                                    skip_sntnc_cmpnt.append( sentence_counter + 1 )                               
                              
                              # done current each_sntnc_obj
                              break
                        

                  if sntnc_struct[ sentence_counter ] == "4":
                     print("current sentence component has sentence structure pattern 4")

                     # in order to has the clause before it. so find it.
                     
                     # candidate clause for preclause in order to. 
                     candi4pre_cl_inorderto = [ "2" ]
                     
                     # get post clauses for in order to.
                     post_cl4inorderto = []
                     ptn4_hit = False
                     for i in range( 0, len(sntnc_struct) ):
                        if ptn4_hit:
                           if sentence_patterns[ int(sntnc_struct[i]) - 1 ]["postv"]:
                              post_cl4inorderto.append( { i : sentence_patterns[ int(sntnc_struct[i]) - 1 ]["operation"] }  )
                        
                        if sntnc_struct[i] == "4":
                           ptn4_hit = True
                           
                     print("post_cl4inorderto " + str(post_cl4inorderto) ) 
                     
                     for i in reversed( range( 0, sentence_counter ) ):
                        if sntnc_struct[i] in candi4pre_cl_inorderto:
                           print("subject clause for the \"inorderto\" is " + sntnc_struct[i])
                           
                           pre_cl4inorderto = sntnc_struct[i]
                           break
                          

                     if pre_cl4inorderto == "2" and "useful_for" in locals():
                        # inoderto target has sentence structure pattern 2
                        # this will become the real or 2nd ( if there will be another useful target ) useful target
                        # for reference, see note: "Make computer to understand sentence - 2"
                        
                        print("inorderto clause is the useful target")
                                             
                        
                        # post clauses 4 inorderto list
                        post_cl4inorderto_l = []
                        for  each_post_cl4inorderto in post_cl4inorderto:
                           for sntnc_i in each_post_cl4inorderto:
                              post_cl4inorderto_l.append( sentence_results[ sntnc_i ] )
                              post_cl4inorderto_l = post_cl4inorderto_l + sentence_results[ sntnc_i ].__dict__[ each_post_cl4inorderto[sntnc_i] ]
                              skip_sntnc_cmpnt.append( sntnc_i )   
                              
                             
                        print("post_cl4inorderto_l " + str( post_cl4inorderto_l ) )     
                              
                        postcl4inorderto_gnodename = "postcl4inorderto"
                        sntnc_nodes[ postcl4inorderto_gnodename ] = post_cl4inorderto_l
                        sntnc_grahs[ useful_gnodename ].add( postcl4inorderto_gnodename )                              
                              
                        
                             
                        print("sntnc_grahs " + str( sntnc_grahs ) )      
                              
                              
                              
                              
            else:
               print("ERROR. list containing word object is not present ")
               sys.exit()
               
  
               
               
               
               
               
               
