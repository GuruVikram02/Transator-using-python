#before executing this program dont forget to install translate module in your python intrepeter or windows terminal using the command pip isntall translate
from translate import Translator

second=input("Enter the language you want to convert :")
#here enter the language it should be converted

first=input("Enter the language your using now :") 
#here enter the language your using now 
translator= Translator(from_lang=first,to_lang=second)

sentence=input("Enter the sentence you want to convert :")

translation = translator.translate(sentence)

print(translation)
