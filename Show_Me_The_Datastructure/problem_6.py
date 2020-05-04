
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)
class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    s=set()
    l=LinkedList()
    li=llist_1
    m=llist_2
    head1=li.head
    head2=m.head
    
    while(head1):
        s.add(head1.value)
        head1=head1.next
        
    while(head2):
        s.add(head2.value)
        head2=head2.next
    for i in s:
        l.append(i)    
       
    return l
    
def intersection(llist_1, llist_2):
    # Your Solution Here
    l=LinkedList()
    list1=[]
    list=[]
    list2=[]
    head1=llist_1.head
    head2=llist_2.head
    
    while(head1):
    
            list1.append(head1.value)
            head1=head1.next
        
    while(head2):
            list2.append(head2.value)
            head2=head2.next
    for i in list2:
        if (i in list1):
            if i not in list:
                list.append(i)
    for i in list:
        l.append(i)    
       
    return l        
    
# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))




# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [2]
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))#3
print (intersection(linked_list_5,linked_list_6)) #''




# Test case 4

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [800,400,255,363,8447,3837,22872]
element_2 = [800,244,255,938,837,3939,9383]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print (union(linked_list_7,linked_list_8))  #800 -> 255 -> 3939 -> 837 -> 9383 -> 938 -> 363 -> 400 -> 244 -> 22872 -> 3837 -> 8447 -> 
print (intersection(linked_list_7,linked_list_8)) #800 -> 255 -> 



