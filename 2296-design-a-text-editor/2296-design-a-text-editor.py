class TextEditor:
    

    def __init__(self):
        self._left = []
        self._right = []
        

    def addText(self, text: str) -> None:
        for char in text:
            self._left.append(char)
        

    def deleteText(self, k: int) -> int:
        actual = 0
        for i in range(k):
            if self._left:
                self._left.pop()
                actual += 1
        return actual
        

    def cursorLeft(self, k: int) -> str:
        for i in range(k):
            if self._left:
                self._right.append(self._left.pop())
    
        if len(self._left) <= 10:
            return ''.join(self._left)
        else:
            return ''.join(self._left[len(self._left)-10:])
        

    def cursorRight(self, k: int) -> str:
        for i in range(k):
            if self._right:
                self._left.append(self._right.pop())
                
        
        if len(self._left) < 10:
            return ''.join(self._left)
        else:
            return ''.join(self._left[len(self._left)-10:])
        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)