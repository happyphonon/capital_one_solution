'''
给一个单词如 "hello" ，一个数组里是 { "he--o", "--loo", "-el-o", "h-"} 
要求返回一个数组，里面装第二个数组里符合第一个单词的字符串 {"he--o", "-el-o"}
'''
def solution(word, candidates):
    res = []
    for candidate in candidates:
        if len(candidate) != len(word):
            continue
        match = True
        for j, w in enumerate(candidate):
            if (w != '-') and (w != word[j]):
                match = False
                break
        if match:
            res.append(candidate)
    return res

print(solution("hello", ["he--o", "--loo", "-el-o", "h-"]))