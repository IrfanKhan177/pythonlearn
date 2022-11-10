#Problem: Create a dicttionary and take input from the user and return the meaning of the word from the dictionary

words = {"ram":"Random Access Memory","rom":"Read only Memory","cpu":"Control Processing Unit","pc":"Personal Computer"}
print("Enter your word...")
word = input()
meaning = words.get(word)
print("The meaning of",word,"is",meaning)