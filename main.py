#vowel AEIOUaeiou
def translation(str):
    translation=""
    for x in str:
          if x.lower() in "aeiou":
              if x.isupper():
                 translation=translation+"P"  #space+p=p
              else:
                  translation = translation + "p"
          else:
               translation=translation+x        #space+letter=letter
    return translation

print(translation(input("enter phrase to translate it: \n")))
