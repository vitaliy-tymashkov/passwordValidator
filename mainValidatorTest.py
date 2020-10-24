from App import validate
from service.Service import validatePasswordContent

inputPasswordLessThan100CharsExample01 = 'password333111111111111111111111111111111111111111111111111111111111111111111111111111111111'
inputLoginLessThan100CharsExample01 = 'werwerwqetwqet'

inputMoreThan100Chars = 'password3331111111111111111111111111111111111111111111111111111111111111111111111111111111111111ssssssssszzzzzzzzzz'
inputLessThan1Char = ''
inputNotAllowedChars = '/s'
allowedChars = '^[A-Za-z0-9 !@#$%^&*()_+{}:\"<>?\[\];\',\.]{1,100}$'

def test_whenLessThan100CharsAndAllCharsAllowed_thenReturnTrue():
    result, mismatchMessage = validate(inputLoginLessThan100CharsExample01, inputPasswordLessThan100CharsExample01, allowedChars)
    assert result == True




