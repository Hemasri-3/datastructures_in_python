
#Stack using Linked List
class StackNode:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.root=None
    def isempty(self):
        return True if self.root is None else False
    def push(self,data):
        new_node=StackNode(data)
        new_node.next=self.root
        self.root=new_node
        print("pushed")
    def pop(self):
        curr=self.root
        if curr is None:
            return
        else:
            self.root=curr.next
            curr=None
            return
    def prints(self):
        curr=self.root
        while curr:
            print(curr.data,end='-->')
            curr=curr.next
            
    def top(self):
        return self.root.data
    def rev(self):
        while not self.isempty():
            
            x=self.top()
            print(x,end='')
            x=self.pop()
s=Stack()
print(s.isempty())
s.push('h')
s.push('e')
s.push('m')
s.push('a')
#s.pop()
#s.prints()
s.top()
s.rev()
