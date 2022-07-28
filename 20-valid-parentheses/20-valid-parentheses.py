class Solution:
    def isValid(self, s: str) -> bool:
        # make a dictionary {closing mark: opening mark}
        # iterate, push opening mark to a stack
        # when see closing mark, check the stack and pop appropriate opening mark
        # if not match, return invalid
        
        if len(s) < 2: return False
        
        marks = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for bracket in s:
            if bracket not in marks:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                elif stack[len(stack)-1] == marks[bracket]:
                    stack.pop()
                else:
                    return False
                
        return False if len(stack) != 0 else True