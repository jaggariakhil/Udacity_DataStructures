#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[5]:


## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        """Initialize this node in the Trie"""
        
        self.is_word = False 
        self.children = {} 
        
        
    def insert(self, char):
        
        self.children[char] = TrieNode()
        
       
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
       
        self.root = TrieNode()  # Root of tree 

    def insert(self, word):
        
        node = self.root 
        
        for char in word:
            if char not in node.children:
                node.insert(char)
                
            node = node.children[char]
        node.is_word = True
   
    def find(self, prefix):
        """Finds the Trie node that represents this prefix"""
        
        node = self.root
        
        for char in prefix:
         
            if char not in node.children:
            
                return False
          
            node = node.children[char]
        
        return node
      


# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[9]:


class TrieNode:
    def __init__(self):
        """Initialize this node in the Trie"""
        self.children = {}  # Dictionary of children 
        self.is_word = False  # True if path taken up to this TrieNode is a word 
    
    def insert(self, char):
        
        self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
    
        suffixes = []
  
        for c, temp in self.children.items():
            

            if temp.is_word:
          
                suffixes.append(suffix + c)
                               
            if temp.children:
            
                suffixes.extend(temp.suffixes(suffix + c))
                
        return suffixes


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[10]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


# In[11]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');


# In[ ]:




