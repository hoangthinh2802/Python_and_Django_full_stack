import re

def multi_re_find(patterns, phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')


test_phrase = 'sdsd...sssddd...ssddsdsd..sdsdsdsdsss...sdddddd'
test_patterns = ['sd*']
multi_re_find(test_patterns, test_phrase)