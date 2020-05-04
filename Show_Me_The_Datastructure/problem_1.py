class LRU_Cache(object):

    def __init__(self, capacity):
      self.capacity=capacity
      self.cache_dict=dict()
      self.elements=[]
        

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache_dict:
          self.elements.remove(key)
          self.elements.append(key)
          return self.cache_dict[key]
          
        else:
          return -1  


    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if(len(self.elements)>=self.capacity):
          del self.cache_dict[self.elements[0]]
          del self.elements[0]
        if key not in self.elements:  
            self.elements.append(key)  
        self.cache_dict[key]=value
our_cache = LRU_Cache(5)

our_cache.set(3, 1);
our_cache.set(4, 2);
our_cache.set(5, 3);
our_cache.set(6, 4);

our_cache.get(3) #returns 1
our_cache.get(9) #returns -1 since no key 9 available in dict


 
our_cache.set(7, 5);
our_cache.set(8, 6);

our_cache.get(4) #returns -1 since the cache is full and the lru ele is removed


our_cache.set(4,8)
our_cache.get(4) #returns 8


