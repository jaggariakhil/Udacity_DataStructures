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
        

    def insert(self, data):
        timestamp=datetime.datetime.now()
        if self.head==None:
            self.head = Block(timestamp, data, 0)
         
            
        else:    
            block = self.head
            while block.next:
                block = self.next
            prev_hash=block.hash
            block.next = Block(timestamp,data,prev_hash)
            return
list=LinkedList()
list.insert("firstblock")
list.insert("secondblock")


print(list.head.data) #first_block
print(list.head.timestamp) #first_block_time_stamp
print(list.head.hash)      #0


print(list.head.next.data) #second_block
print(list.head.timestamp) #2nd_block_time_stamp
print(list.head.hash)      #first_block_hash_value



 
