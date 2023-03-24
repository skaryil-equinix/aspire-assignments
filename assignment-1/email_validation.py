import re

def extract_info(email):
    # extract the first name and last name using regular expressions
    name_pattern = re.compile(r'([a-zA-Z0-9]+)\.([a-zA-Z0-9]+)')
    name_match = name_pattern.search(email)
    
    # extract the domain name using regular expressions
    domain_pattern = re.compile(r'@([a-zA-Z]+\.[a-zA-Z]+)')
    domain_match = domain_pattern.search(email)
    
    # check if both the name and domain patterns were found
    if name_match and domain_match:
        first_name = name_match.group(1)
        last_name = name_match.group(2)
        domain_name = domain_match.group(1)
        
        return first_name, last_name, domain_name
    
    # return None if either pattern was not found
    return None

def remove_digits(string):
    new_string = ""
    for char in string:
        if not char.isdigit():
            new_string += char
    return new_string


email = input("Enter email: ")
info = extract_info(email)

if info:
    print(f'First Name: {remove_digits(info[0])}')
    print(f'Last Name: {remove_digits(info[1])}')
    print(f'Domain Name: {info[2]}')
else:
    print('Invalid email ID')



