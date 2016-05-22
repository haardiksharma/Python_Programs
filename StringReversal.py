# A function to reverse an string
def reverse(text):
    holder = ""
    #smart use of looping
	for letter in text:
        holder = letter + holder
    return holder
    #another ingenious way of doing the string reversal using range option in loop 
''' def reverse(text):
    new_word = ""
    for i in range(0, len(text)):
        new_word += text[len(text) - 1 - i]
    return new_word'''