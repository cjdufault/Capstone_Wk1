import re


def main():
    string = input("Type a sentence: ")
    
    if not is_valid_variable(string):
        proceed = show_warning("Won't produce a valid variable name. Continue? Y/n ")
        if not proceed:
            return
        
    print(make_camel(string))
    
    
def make_camel(string):
    token_list = string.split()
    
    # remove 1st token and use it in all lower case to start out our output string
    camel_string = token_list.pop(0).lower()
    
    # add all other tokens, capitalized, to output string
    for token in token_list:
        camel_string = camel_string + token.title()
        
    return camel_string
    
    
# returns True if a string is a valid python variable name, False if not
def is_valid_variable(string):
    # check that 1st char is valid
    if not string[0].isalpha() or string[0] == "_":
        return False
    
    # check for special characters
    sp_char_regex = re.compile("[!@#$%^&*()<>?/\|}{~:\[\],.+-]")
    if sp_char_regex.search(string) == None:
        return True
    return False
    

# shows a warning, returns True if user wants to continue, False if not
def show_warning(string):
    answer = input(string)
    if answer.lower() == "y" or answer.lower() == "yes":
        return True
    elif answer.lower() == "n" or answer.lower() == "no":
        return False
    else:
        return show_warning(string) # ask again if answer is other than yes or no


if __name__ == "__main__":
    main()
