#Using dictionary,develop a python program to determine and print the number of duplicate words in a sentence
sen = input("Enter the sentence: ")
words = sen.lower().split()
det = {}
for word in words:
    if word in det:
        det[word] += 1
    else:
        det[word] = 1
repeated = 0
print("Repeated words are:")
for key, value in det.items():
    if value > 1:
        print(key)
        repeated += 1
print("Total number of repeated elements are:", repeated)

