try:
    f = open('demo.txt', 'x')
except:
    pass  


with open('demo.txt', 'w') as f:
    f.write('hai my name is dhanushya v s')


longest_word = ""
with open('demo.txt', 'r') as f:
    for line in f:
        words = line.strip().split(' ')
        for word in words:
            if word and len(word) > len(longest_word):
                longest_word = word

print(longest_word)
