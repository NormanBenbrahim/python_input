# input

# using the 'input' function

# we will use this script to get a sentence from the user, and save that 
# sentence into a text file

response = input("Please give me a sentence to write: ")
print("")

with open('response.txt', 'w') as f:
    f.write(response)