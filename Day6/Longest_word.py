def find_longest_word(sentence):
    words=sentence.split(" ")
    idx=0
    max=0
    for i in words:
        if len(i)>max:
            max=len(i)
            idx=words.index(i)
    return words[idx]
sentence=input("Enter a sentence: ")
result=find_longest_word(sentence)
print("Longest word: ",result)