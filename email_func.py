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


text1 = " we are location at abc@gmail.com or at ttsh@hotmail.com"
text2 = " you can contact us at 12348@goog.io"
text3 = []
text3.append(text1)
text3.append(text2)

emails = extract(text3)
print(emails)
print(extract(text3, flatten=True))