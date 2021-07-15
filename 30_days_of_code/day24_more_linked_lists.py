class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #start
        #if head is none, than the list is empty, if head.next is none 
        # then there is only one entry hence no repetation hence return the head without change
        if head == None or head.next == None:
            return head
        else:
            current_node = head
            while hasattr(current_node, 'next') and not current_node.next == None: 
                focused_node = current_node
                while hasattr(focused_node.next, 'next') and not focused_node.next == None:
                    if current_node.data == focused_node.next.data:
                        focused_node.next = focused_node.next.next
                    else:
                        focused_node = focused_node.next
                current_node = current_node.next
            return head
        #end  

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 