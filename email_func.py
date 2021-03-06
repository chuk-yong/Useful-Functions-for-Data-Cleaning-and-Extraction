import re

def extract(text, flatten = False):
    ''' text can be a str or a list
    returns a list of emails \n
    flatten = True will return list. False returns a list of lists
    '''
    # if text is not a list, convert to a list
    text = [text] if isinstance(text, str) else text
    match = []
    for t in text:
        match.append(re.findall(r'[\w\.-]+@[\w\.-]+', t))
    if flatten == True:
        match = [item for sublist in match for item in sublist]
    return match

def validate(email, pattern = 'simple'):
    ''' validate emails \n
    returns True or False \n
    if pattern = 'html5', uses W3C Html5 standard
    '''
    
    if pattern == 'html5':
        pattern = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
    else:    
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if re.match(pattern, email):
        return True
    return False
