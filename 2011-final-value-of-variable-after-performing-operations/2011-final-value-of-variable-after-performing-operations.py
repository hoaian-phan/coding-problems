class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # iterate through each element and check what operation it has then perform the operation
        
        X = 0
        
        for operation in operations:
            if operation[1] == "+":
                X += 1
            elif operation[1] == "-":
                X -= 1
                
        return X