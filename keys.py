def bets1(i: str) -> str:
    
    '''This function is used for the encryption of uppercase letters'''
    
    if i == 'A':
        return '123'
    elif i == 'B':
        return '141'
    elif i == 'C':
        return '124'
    elif i == 'D':
        return '139'
    elif i == 'E':
        return '156'
    elif i == 'F':
        return '166'
    elif i == 'G':
        return '002'
    elif i == 'H':
        return '111'
    elif i == 'I':
        return '174'
    elif i == 'J':
        return '768'
    elif i == 'K':
        return '679'
    elif i == 'L':
        return '660'
    elif i == 'M':
        return '040'  
    elif i == 'N':
        return '598'
    elif i == 'O':
        return '069'
    elif i == 'P':
        return '127'
    elif i == 'Q':
        return '024'
    elif i == 'R':
        return '379'
    elif i == 'S':
        return '380'
    elif i == 'T':
        return '666'
    elif i == 'U':
        return '989'
    elif i == 'V':
        return '116'
    elif i == 'W':
        return '171'
    elif i == 'X':
        return '247'
    elif i == 'Y':
        return '050'
    elif i == 'Z':
        return '799'
    else:
        return ''


def bets2(i: str) -> str:
    
    '''This function is used for the encryption of lowercase letters'''
    
    if i == 'a':
        return '167'
    elif i == 'b':
        return '112'
    elif i == 'c':
        return '121'
    elif i == 'd':
        return '192'
    elif i == 'e':
        return '125'
    elif i == 'f':
        return '168'
    elif i == 'g':
        return '010'
    elif i == 'h':
        return '230'
    elif i == 'i':
        return '229'
    elif i == 'j':
        return '779'
    elif i == 'k':
        return '231'
    elif i == 'l':
        return '023'
    elif i == 'm':
        return '199'
    elif i == 'n':
        return '197'
    elif i == 'o':
        return '012'
    elif i == 'p':
        return '128'
    elif i == 'q':
        return '067'
    elif i == 'r':
        return '240'
    elif i == 's':
        return '241'
    elif i == 't':
        return '676'
    elif i == 'u':
        return '239'
    elif i == 'v':
        return '611'
    elif i == 'w':
        return '901'
    elif i == 'x':
        return '742'
    elif i == 'y':
        return '049'  
    elif i == 'z':
        return '791'
    else:
        return ''

def git(d: str) -> str:
    
    '''This function is used for the encryption of digits'''
    
    if d == '0':
        return '047'
    elif d == '1':
        return '031'
    elif d == '2':
        return '303'
    elif d == '3':
        return '269'
    elif d == '4':
        return '449'
    elif d == '5':
        return '056'
    elif d == '6':
        return '043'
    elif d == '7':
        return '078'
    elif d == '8':
        return '761'
    elif d == '9':
        return '191'


def space(s: str) -> str:
    
    '''This function is used for the encryption of a non-graphic character, space'''
    
    return '998'

def special(s: str) -> str:
    
    '''This function is used for the encryption of special characters'''
    
    if s == '~':
        return '007'
    elif s == '`':
        return '271'
    elif s == '!':
        return '986'
    elif s == '@':
        return '097'
    elif s == '#':
        return '008'
    elif s == '$':
        return '447'
    elif s == '%':
        return '232'  
    elif s == '*':
        return '117'
    elif s == '&':
        return '118'
    elif s == '^':
        return '421'
    elif s == '(':
        return '496'
    elif s == ')':
        return '423'
    elif s == '-':
        return '550'
    elif s == '_':
        return '545'
    elif s == '+':
        return '222'
    elif s == '=':
        return '333'
    elif s == '{':
        return '865'
    elif s == '}':
        return '720'
    elif s == '[':
        return '624'
    elif s == ']':
        return '244'
    elif s == ';':
        return '346'
    elif s == ':':
        return '422'
    elif s == "'":
        return '040'
    elif s == ',':
        return '881'
    elif s == '.':
        return '391'
    elif s == '<':
        return '753'
    elif s == '>':
        return '087'
    elif s == '/':
        return '412'
    elif s == '?':
        return '904'
    else:
        return '785'

def fun(i: str) -> str:
    
    '''This function is used for decrypting an encrypted data'''
    
    # Uppercase alphabet 
    if i == '123':
        return 'A'
    elif i == '141':
        return 'B'
    elif i == '124':
        return 'C'
    elif i == '139':
        return 'D'
    elif i == '156':
        return 'E'
    elif i == '166':
        return 'F'
    elif i == '002':
        return 'G'
    elif i == '111':
        return 'H'
    elif i == '174':
        return 'I'
    elif i == '768':
        return 'J'
    elif i == '679':
        return 'K'
    elif i == '660':
        return 'L'
    elif i == '040':  
        return 'M'
    elif i == '598':
        return 'N'
    elif i == '069':
        return 'O'
    elif i == '127':
        return 'P'
    elif i == '024':
        return 'Q'
    elif i == '379':
        return 'R'
    elif i == '380':
        return 'S'
    elif i == '666':
        return 'T'
    elif i == '989':
        return 'U'
    elif i == '116':
        return 'V'
    elif i == '171':
        return 'W'
    elif i == '247':
        return 'X'
    elif i == '050':
        return 'Y'
    elif i == '799':
        return 'Z'
    
    # Lowercase alphabet 
    elif i == '167':
        return 'a'
    elif i == '112':
        return 'b'
    elif i == '121':
        return 'c'
    elif i == '192':
        return 'd'
    elif i == '125':
        return 'e'
    elif i == '168':
        return 'f'
    elif i == '010':
        return 'g'
    elif i == '230':
        return 'h'
    elif i == '229':
        return 'i'
    elif i == '779':
        return 'j'
    elif i == '231':
        return 'k'
    elif i == '023':
        return 'l'
    elif i == '199':
        return 'm'
    elif i == '197':
        return 'n'
    elif i == '012':
        return 'o'
    elif i == '128':
        return 'p'
    elif i == '067':
        return 'q'
    elif i == '240':
        return 'r'
    elif i == '241':
        return 's'
    elif i == '676':
        return 't'
    elif i == '239':
        return 'u'
    elif i == '611':
        return 'v'
    elif i == '901':
        return 'w'
    elif i == '742':
        return 'x'
    elif i == '049':  
        return 'y'
    elif i == '791':
        return 'z'
    
    # Digits mappings
    elif i == '047':
        return '0'
    elif i == '031':
        return '1'
    elif i == '303':
        return '2'
    elif i == '269':
        return '3'
    elif i == '449':
        return '4'
    elif i == '056':
        return '5'
    elif i == '043':
        return '6'
    elif i == '078':
        return '7'
    elif i == '761':
        return '8'
    elif i == '191':
        return '9'
    
    # Special characters 
    elif i == '007':
        return '~'
    elif i == '271':
        return '`'
    elif i == '986':
        return '!'
    elif i == '097':
        return '@'
    elif i == '008':
        return '#'
    elif i == '447':
        return '$'
    elif i == '232':  
        return '%'
    elif i == '117':
        return '*'
    elif i == '118':
        return '&'
    elif i == '421':
        return '^'
    elif i == '496':
        return '('
    elif i == '423':
        return ')'
    elif i == '550':
        return '-'
    elif i == '545':
        return '_'
    elif i == '222':
        return '+'
    elif i == '333':
        return '='
    elif i == '865':
        return '{'
    elif i == '720':
        return '}'
    elif i == '624':
        return '['
    elif i == '244':
        return ']'
    elif i == '346':
        return ';'
    elif i == '422':
        return ':'
    elif i == '040':
        return "'"
    elif i == '881':
        return ','
    elif i == '391':
        return '.'
    elif i == '753':
        return '<'
    elif i == '087':
        return '>'
    elif i == '412':
        return '/'
    elif i == '904':
        return '?'
    elif i == '998':
        return ' '
    else:
        return ' '  
    
def decrypt(content : str) -> str:
    
    text = str()
    for i in range(0, len(content), 3):
        ele = content[i:i+3]
        text += fun(ele)

    return text

def texties(filedata: str) -> str:
    
    '''This function is used for encrypting data'''
    
    encrypted_text = str()

    for i in filedata:
        if i.isalpha():
            code = bets1(i) if i.isupper() else bets2(i)
        elif i.isdigit():
            code = git(i)
        elif i.isspace():
            code = space(i)
        else:
            code = special(i)
        encrypted_text += code
  
    return encrypted_text