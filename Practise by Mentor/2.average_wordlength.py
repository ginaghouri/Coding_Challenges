sentence1 = "Hi class, we are practicing solving algorithms. It is fun, don't you think?.."
sentence2 = "We need to work very hard to learn more about algorithms!"

def wordsLength(sentence):
    words = sentence.split(' ') # Split the sentence based on spaces ' '. 'words' is now a list of words
    
    # formula for average length
    # average = total length of all words / number of words
    total_length = 0
    for word in words:
        total_length += len(word)
        
    number_of_words = len(words) # Number of words are basically the number of items in the list 'words'. We can use len() function go get the length of the list, which is basically the number of words
    
    average = total_length / number_of_words
    
    return average
    
print(wordsLength(sentence1))
print(wordsLength(sentence2))