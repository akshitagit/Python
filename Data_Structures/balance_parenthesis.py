def check(s):
    stk = list()
    open_char = ['[', '{', '(']
    close_char = [']', '}', ')']
    for i in s:
        if len(stk)==0 and i in close_char:
            return False
        else:
            if i in open_char:
                stk.append(i)
            if i in close_char:
                # can individually check for the other brackets if dont want to use python buitin functions
                if open_char.index(stk[-1]) == close_char.index(i): 
                    stk.pop()
                else:
                    return False
    return True if len(stk)==0 else False

if __name__ == '__main__':
    brackets = input()
    print("Balanced" if check(brackets) else "Not Balanced")