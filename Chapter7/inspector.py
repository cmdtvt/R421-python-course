def testme(inp):
    checkString = "abcdefghijklmnopqrstuvwxyzoäö0123456789"
    hasLetter = False
    hasNumber = False
    if len(inp) > 6:
        for i in inp.lower():
            if i not in checkString:
                return False
            else:
                if i.isnumeric():
                    hasNumber = True
                if i.isalpha():
                    hasLetter = True

        if hasLetter and hasNumber:
            return True
        else:
            return False
    else:
        return False
