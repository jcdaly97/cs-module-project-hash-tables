

def word_count(s):
    #make a dictionary
    count = {}
    #remove punctuation and make lowercase
    punc = ''':";,.-+=/\\|[]{}()*^&'''
    for char in s:
        if char in punc:
            s = s.replace(char, "")
    s = s.lower()
    #split into a list of words
    arr = s.split()
    for i in arr:
        if i not in count:
            count[i] = 1
        else:
            count[i]+=1
    return count

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))