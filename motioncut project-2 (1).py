#Word Counter

def counter(word): 
    #Function for counting the word
    count = word.split() 
    #Storing the word which counted using the split() Method
    return len(count) 
    #using len for the count of words
def has_numbers(word):  
    #Function for checking if the input contains any numbers or not
    return any(char.isdigit() for char in word)  
    #check each char of input is number or not using for loop
try: 
    #try block to check if any error occurs or not
    word = input('Enter the sentence or paragraph: ')   
    #user_input
    if not word:  
        #If the input is null returns error
          raise ValueError("Enter the input")
    
    if has_numbers(word):   
        #If the input contains it returns error
        raise ValueError("Numbers Are invalid enter letters")
    
     word_count = counter(word)  
    #calling the function counter
    print("Number of words:", word_count)  
    #Display the output   
except ValueError as ve: 
    #Except block
    print("Error :",ve)
    