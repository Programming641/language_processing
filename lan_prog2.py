from lib.process_sentence import Sentence_Processor
from lib.process_sntnc_meaning import Sentence_Meaning_Processor

   
   
#sentence = "Most people eat two or three meals in a day."

sentence = "There are some key phrases that are useful to learn in English in order to explain your daily routine to another person."


sentence_results = Sentence_Processor.process(sentence)
print()
print("sentence_results")
print(sentence_results)
print()
print()


print("sentence processing done. now proceed to process sentence meaning")
print()

Sentence_Meaning_Processor.process(sentence_results)




