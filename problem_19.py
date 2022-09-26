'''
two strings combine into one string, alternative.
string1: eape, string2: xml, output: example
string1: aaaaa, string2: bb, output: ababaaa
'''
def solution(string1, string2):
    combine = ''
    i, j = 0, 0
    while i < len(string1) or j < len(string2):
        if i < len(string1):
            combine += string1[i]
            i += 1
        if j < len(string2):
            combine += string2[j]
            j += 1
    return combine

print(solution("eape", "xml"))
print(solution("aaaaa", "bb"))