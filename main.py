# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
      
def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, "r") as file:
        contents = file.read()
        #retun "Hello World"
        return contents
        
def count_words():
    text = read_file_content("./story.txt")
       # [assignment] Add your code here
    split_text = text.split()
    count={}
    for words in split_text:
        if words in count:
            count[words] += 1
        else:
            count[words] =  1
    return count
    # return {"as": 10, "would": 20}
print(count_words()) 