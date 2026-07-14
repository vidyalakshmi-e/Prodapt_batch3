def count_vowels(text):
    vowels="aeiou"
    count=0

    length=len(text)
    while length>0:
        if text[length-1].lower() in vowels:
            count+=1
        length-=1
    return count

sentence=input("Enter a string: ")
result=count_vowels(sentence)

print("Vowels count: ",result)