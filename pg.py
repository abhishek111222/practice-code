hudef sentence_maker(word):
    interrogatives = ("what", "which", "when", "where", "who", "whom", "whose", "why", "whether", "how", "are")
    capitalized = word.capitalize()
    if word.startswith(interrogatives):
        return f"{capitalized}?"
    else:
        return f"{capitalized}."




say_something = ""
l = []
while True : 
    say_something = input("Say Something : ")
    if say_something == "\end":
        break 
    else : 
        a = sentence_maker(say_something)
        l.append(a)
        #print(l)
        continue

for i in l:
    print(i, end = " ")




