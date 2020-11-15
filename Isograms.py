from collections import Counter
def is_isogram(string):
    if len(string) == 0:
        return True
    else:
        string = string.lower()
        letters = Counter(string)
        for key in letters.keys():
            if letters[key] != 1:
                return False
    return True

print(is_isogram("moOse"))