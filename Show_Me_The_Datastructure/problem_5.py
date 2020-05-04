import hashlib
import datetime
import hashlib
import datetime
class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data)
      self.next=None  

    def calc_hash(self, data):
      sha = hashlib.sha256()
      hash_str = data.encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        

    def insert(self, data):
        timestamp=datetime.datetime.now()
        if self.head==None:
            self.head = Block(timestamp, data, 0)
            self.tail=self.head
            #prev_hash=self.tail.hash
            
        else:
            self.tail.next=Block(timestamp,data,self.tail.hash)
            self.tail=self.tail.next
            
            
       
list=LinkedList()
list.insert("firstblock")

#testcase1

print(list.head.data) #first_block
print(list.head.timestamp) #first_block_time_stamp
print(list.head.previous_hash)      #0



#testcase2

list.insert("secondblock")
print(list.head.next.data) #second_block
print(list.head.next.timestamp) #2nd_block_time_stamp
print(list.head.next.previous_hash)      #first_block_hash_value





#testcase3
list.insert("thirdblock")
print(list.head.next.next.data) #third_block
print(list.head.next.next.timestamp) #3rd_block_time_stamp
print(list.head.next.next.previous_hash)      #second_block_hash_value





 

