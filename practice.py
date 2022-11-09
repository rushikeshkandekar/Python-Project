name = input("enter your name\n")
print("good morning," + name)

letter = '''hello <|N|>,you are selected
Date: <|DATE|>'''
name = input("Enter your name\n")
date = input("Enter date\n")
letter = letter.replace("<|N|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)
st = "hi my   name is rushi"
doubleSpaces = st.find("  ")
print(doubleSpaces)
