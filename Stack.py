class Stack:
    def __init__(self):  # 初始化
        self.items = []

    def push(self, item):  # 元素入栈
        self.items.append(item)

    def pop(self):  # 元素出栈，如果栈为空，抛出stackIsEmpty异常
        if self.is_empty():
            raise Exception('stackIsEmpty')
        else:
            return self.items.pop()

    def peek(self):  # 返回栈顶元素，元素不出栈
        if self.is_empty():
            raise Exception('stackIsEmpty')
        else:
            return self.items[-1]

    def is_empty(self):  # 栈为空返回True，否则返回False
        return self.items == []

    def size(self):  # 返回栈内元素个数
        return len(self.items)
