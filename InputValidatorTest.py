from service.Service import validatePasswordContent

inputLessThan100Chars = 'password333111111111111111111111111111111111111111111111111111111111111111111111111111111111'
inputMoreThan100Chars = 'password3331111111111111111111111111111111111111111111111111111111111111111111111111111111111111ssssssssszzzzzzzzzz'
inputLessThan1Char = ''
inputNotAllowedChars = '/s'
allowedChars = '^[A-Za-z0-9 !@#$%^&*()_+{}:\"<>?\[\];\',\.]{1,100}$'

def test_whenLessThan100CharsAndAllCharsAllowed_thenReturnTrue():
    assert validatePasswordContent(inputLessThan100Chars, allowedChars) == True

def test_whenMoreThan100Chars_thenReturnFalse():
    assert validatePasswordContent(inputMoreThan100Chars, allowedChars) == False

def test_whenLessThan1Char_thenReturnFalse():
    assert validatePasswordContent(inputLessThan1Char, allowedChars) == False

def test_whenNotAllowedChars_thenReturnFalse():
    assert validatePasswordContent(inputNotAllowedChars, allowedChars) == False