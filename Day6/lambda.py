import time
add=lambda x,y:x+y
print(add(5,6))
start_time=time.perf_counter()
find_largest_word=lambda sentence: max(sentence.split(" "), key=len)
sentence=input("Enter a sentence: ")
result=find_largest_word(sentence)
end_time=time.perf_counter()
print("Largest word: ",result)
execution_time=end_time-start_time
print(f"{execution_time:.6f} seconds")