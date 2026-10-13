stack = []

stack.append(1)
stack.append(2) 
stack.append(3)

print("stack sebelum di push: ", stack)

atas = stack.pop()
print("stack setelah di pop: ", stack)
print("stack setelah pop: ", atas)

puncak = stack[-1]
print("elemen terakhir (peek)", puncak)

ks = stack.pop()
ks = stack.pop()

if len(stack) == 0:
    print("stack kosong")
print("stack setelah pop: ", stack)


class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop
        else:
            return None
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
    def size(self):
        return len(self.items)

s = Stack()
s.push(input("masukkan stack 1: "))
s.push(input("masukkan stack 2: "))
s.push(input("masukkan stack 3: "))

print("data pada stack: ", s.items)
s.pop()
print("data pada stack setelah pop: ", s.items )



