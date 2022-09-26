'''
unix string指示:给一个string数组代表一串unix的指令,
可能出现的指令ls,mv,cp,!index,其中index是数字,代表执行index-1th的指令.
例如{”ls“,"cp","mv","!3'}，那!3需要执行的就是元素commands[2],即mv.
结果要返回ls,cp,mv分别执行多少次的数组.
'''
from collections import defaultdict
def solution(commands):
    command_counter = defaultdict(int)
    for command in commands:
        if "!" in command:
            index = int(command[1:]) # assume index is valid
            command_counter[commands[index - 1]] += 1
        else:
            command_counter[command] += 1
    return command_counter

print(solution(["ls","cp","mv","!3"]))
print(solution(["ls","cp","!2", "ls", "mv","!4"]))