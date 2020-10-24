import re
from math import ceil

from service.Service import validatePasswordContent, validateLoginContent

MATCHER_GROUP = 1
MATCHER_SPAN_END = 1
MATCHER_SPAN_START = 0
MATCHER_SPAN = 0

# inputPassword = 'password33377777777777ssssssssssss'
# inputLogin = 'login333081234567888887'

# inputPassword = 'login3330812password3337sslogin3330812'
# inputLogin = 'login333081234567888887'

# inputPassword = 'userususus'
# inputLogin = 'userus'
# inputLogin = 'useruseruser'

# inputPassword = 'password3331111111111111111111111111111111111111111111111111111111111111111111111111111111111111sssssssss'
# inputLogin = 'login33309'

# inputPassword = 'palololoololllooollololololsssssssss'
# inputLogin = 'ssss'

inputPassword = 'ssddffgghhjjXkkllooiiuuyyttrreXXewwddffgghhjjkkll;;ssddsgsdgsdgesgbcvhrdtyrtjXjrtjrejhmryertrh'
inputLogin = 'X'

allowedChars = '^[A-Za-z0-9 !@#$%^&*()_+{}:\"<>?\[\];\',\.]{1,100}$' #Length check included in Regexp
               #^[A-Za-z0-9 !@#$%^&*()_+{}:\"<>?\[\];\',\.]{1,100}$

def validate(inputLogin, inputPassword, allowedChars):
    validPassword =  validatePasswordContent(inputPassword, allowedChars)
    validLogin = validateLoginContent(inputLogin, allowedChars)
    mismatchMessage = ''
    if (not validPassword) & (not validLogin):
        mismatchMessage += ' [Password and Login didn\'t pass input validation]'
        raise ValueError(mismatchMessage)
    if not validPassword:
        mismatchMessage += ' [Password didn\'t pass input validation]'
        raise ValueError(mismatchMessage)
    if not validLogin:
        mismatchMessage += ' [Login didn\'t pass input validation]'
        raise ValueError(mismatchMessage)


    #2. Validation - Bruteforce
    lenLogin = len(inputLogin)
    lenPassword = len(inputPassword)

    # This check is not used!
    # if lenLogin/2 > lenPassword:
    #     return True, 'Login/2 is more than Password'
    # if lenPassword/2 > lenLogin:
    #     return True, 'Password/2 is more than Login'

    #2.1 Validate login
    loginParts, matchesOfLoginInPassword = findAllMatches(inputLogin, inputPassword, lenLogin)
    print('********************************************************')
    print(inputLogin, ' : LOGIN')
    print('--------------------------------------------------------')
    for i, el in enumerate(loginParts):
        print('' * i + el) #FixMe: shift is not implemented due to absence of info about shift
    print('********************************************************')

    #2.2 Validate password
    passwordParts, matchesOfPasswordInLogin = findAllMatches(inputPassword, inputLogin, lenPassword)
    # print('********************************************************')
    print(inputPassword, ' : PASSWORD')
    print('--------------------------------------------------------')
    for i, el in enumerate(passwordParts):
        print('' * i + el) #FixMe: shift is not implemented due to absence of info about shift
    # print('********************************************************')


    if len(matchesOfLoginInPassword) == 0 & len(matchesOfPasswordInLogin) == 0:
        return True, 'Password and Login checks (for inclusions more than 1/2) is OK'

    if not(len(matchesOfLoginInPassword) == 0):
        mismatchMessage += '\nPassword check for login inclusion (more than 1/2) below '
        loginShiftCount = (lenLogin//2) + 2
        passwordShiftCount = (lenPassword//2) + 1
        mismatchMessage += '\n|' + ' '*passwordShiftCount + 'PASSWORD' + ' '*passwordShiftCount \
                           + '| ' + ' '*loginShiftCount + 'LOGIN PART' +' '*loginShiftCount+ '|'

        for m in matchesOfLoginInPassword:
            mismatchMessage += '\n| ' \
                               + inputPassword[:m[MATCHER_SPAN][MATCHER_SPAN_START]] \
                               + ' << ' + m[MATCHER_GROUP] + ' >> ' \
                               + inputPassword[m[MATCHER_SPAN][MATCHER_SPAN_END]:] \
                               + ' | ' \
                               + ' '.join(map(str, m)) \
                               # + ' '*loginShiftCount + '|'

    if not(len(matchesOfPasswordInLogin) == 0):
        mismatchMessage += '\nLogin check for password inclusion (more than 1/2) below'
        loginShiftCount = (lenLogin//2) + 2
        passwordShiftCount = (lenPassword//2) + 0
        mismatchMessage += '\n|' + ' '*loginShiftCount + 'LOGIN' + ' '*loginShiftCount \
                           + '| ' + ' '*passwordShiftCount + 'PASSWORD PART' +' '*passwordShiftCount+ '|'
        for m in matchesOfPasswordInLogin:
            mismatchMessage += '\n|' \
                               + inputLogin[:m[MATCHER_SPAN][MATCHER_SPAN_START]] \
                               + ' << ' + m[MATCHER_GROUP] + ' >> ' \
                               + inputLogin[m[MATCHER_SPAN][MATCHER_SPAN_END]:] \
                               + ' | ' \
                               + ' '.join(map(str, m)) \
                               # + ' '*passwordShiftCount + '|'

    if (not (len(matchesOfLoginInPassword) == 0)) | (not (len(matchesOfPasswordInLogin) == 0)):
        return False, mismatchMessage

def findAllMatches(inputLogin, inputPassword, lenLogin):
    loginParts = []
    matchesOfLoginInPassword = []
    i = 0
    halfLen = ceil(lenLogin / 2)
    while (i + halfLen) <= lenLogin:
        j = (int)(i + halfLen)
        while j <= lenLogin:
            part = inputLogin[i:j]
            match = re.finditer(part, inputPassword)
            if not (match is None):
                for m in match:
                    matchesOfLoginInPassword.append((m.span(), m.group()))
            loginParts.append(part)
            # print(' ' * i + part) #Note: Shift here works well (but disabled because of extracting method for login and Password)
            j += 1
        i += 1
    return loginParts, matchesOfLoginInPassword

#################################################################
# print('********************************************************')
try:
    result, mismatchMessage = validate(inputLogin, inputPassword, allowedChars)
    print('********************************************************')
    print('RESULT OF VALIDATION IS {2} FOR\n   login [{0}]\npassword [{1}]'.format(inputLogin, inputPassword, result))
    print('--------------------------------------------------------')
    print(mismatchMessage)
except ValueError as e:
    print(
        'VALIDATION FINISHED WITH EXCEPTION {2} FOR\n   login [{0}]\npassword [{1}]'.format(inputLogin, inputPassword, e))