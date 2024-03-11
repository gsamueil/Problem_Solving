class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
    def __str__(self) :
        temp_node=self.head
        result=''
        while temp_node is not None:
            result+=str(temp_node.value)
            if temp_node.next is not None:
                result+=' -> '
            temp_node=temp_node.next
        return result
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        
    def insert(self,index,value):
        new_node=Node(value)
        if index <0 or index>self.length:
            return False
            
        elif self.length==0:
            self.head=new_node
            self.tail=new_node
        elif index==0:
            new_node.next=self.head
            self.head=new_node
        else:
            
            temp_node=self.head
            for _ in range(index-1):
                temp_node=temp_node.next
            new_node.next=temp_node.next
            temp_node.next=new_node
        self.length+=1
        return True
    
    def traverse(self):
        current=self.head
        while current :
            print(current.value)
            current=current.next
            # current.transpose()
        return current
    def search(self,target):
        current = self.head
        index=0
        while current:
            if current.value==target:
                return print('Exist in index number = ',index)
            current=current.next
            index+=1
        return -1
    def get(self,index):
        current=self.head
        if index==-1:
            return self.tail
        if index<=-1 or index >len(index):
            return None
        for _ in len(index):
            current=current.next
        return current
    def set_value(self,index,value )  :
        temp=self.get(index) 
        if temp:
            temp.value=value
            return True
        return False
    
    def pop_first(self):
        if self.length==0:
            return print(None,'empty list')
        pop_node=self.head
        if self.length==1:
            self.head=None
            self.tail=None
            print('no element now')
        else:
            
            self.head=self.head.next
            pop_node.next=None
        self.length -=1
        return pop_node
    def remove(self,index):
        prev_node=self.get(index-1)
        poped_node=prev_node.next
        prev_node.next=poped_node.next
        poped_node.next=None
        self.length-=1
        return poped_node
    def delete_all(self):
        self.head=None
        self.tail=None
        self.length=0
        return print('empty linkedList')
    
new_linked_list=LinkedList()
# new_linked_list.insert(0,200)
new_linked_list.append(5)
new_linked_list.append(10)
new_linked_list.append(20)


print(new_linked_list)
# new_linked_list.insert(-5,40000)
# print(new_linked_list)
# print(new_linked_list.search(5))
# new_linked_list.pop_first()
# new_linked_list.pop_first()
# new_linked_list.pop_first()
new_linked_list.delete_all()
print(new_linked_list)