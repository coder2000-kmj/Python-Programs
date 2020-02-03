words=['airplane','chocolate','elephant','car','one','year']

def word(st,end=len(words)):
    if st<end:
        if words[st][0] in "aeiou":
            if st + 1 < len(words) - 1:
                words[st] = words[st + 1];
                st+=1;word(st,end)
            else:
                print("can't replace")
word(st=0,end=len(words))
print(words)
