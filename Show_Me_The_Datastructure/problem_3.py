import sys
global priority_dict
priority_dict={}

def count_char(data):
  huff_dict={}
  for char in data:
    if char not in huff_dict:
      huff_dict[char]=0
    huff_dict[char]+=1
  return huff_dict

def priority(huff_dict):
  h_dict={}
  for i in sorted(huff_dict,key=huff_dict.get):
    h_dict[i]=huff_dict[i]
  return h_dict


def priority_pattern(priority_dict):
    list=[]
    for i in priority_dict:
      list.append(i)
  #print(list)
  #print()    
    i=1
    while(len(list)>1):
    
    
        last1=list.pop(0)
        last2=list.pop(0)
        #print(list)

        key=last2+last1  
        val=priority_dict[last1]+priority_dict[last2]
        list.append(key)
        del priority_dict[last2]
        del priority_dict[last1]
        #print(priority_dict)
        priority_dict[key]=val
        priority_dict=priority(priority_dict)
        #l=[list[0],priority_dict]
    return list[0]




def encoding(data):
  global priority_dict
  huff_dict=count_char(data)
  priority_dict=priority(huff_dict)
  return priority_pattern(priority_dict)

def encode(data):
  encoder={}
  

  pattern=encoding(data)
  #print(v)
  temp='0'
  
  encoder[pattern[0]]='0'  
  for i in pattern[1:]:
    temp='1'+temp
    encoder[i]=temp
  #print(encoder)
  return encoder  

def huffman_encoding(data):
  de=""
  dict={}
  if(data==""):
    return de,dict 
  dict=encode(data)
  de=''
  for i in data:
    de=de+dict[i]
  
  return de,dict



def huffman_decoding(data,tree):
  
  priority_dict=tree
  dec_dict = {v: k for k, v in priority_dict.items()}  
  
  
  
  decoder=''
  temp=''
  
  for i in data:
      
    if i == '1':
        temp+='1'
    else:
        temp+='0'
        decoder+=dec_dict[temp]
        temp=''
        
    
  return decoder
#huffman_decoding('011111101111101101011111110110101111111011110111')


#Testcase1


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "abc"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence))) #52
    print ("The content of the data is: {}\n".format(a_great_sentence))   #abc

    encoded_data, tree = huffman_encoding(a_great_sentence) 
    print(tree)
    # print(encoded_data)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))  #28
    print ("The content of the encoded data is: {}\n".format(encoded_data))  #100110
 
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) #52
    print ("The content of the decoded data is: {}\n".format(decoded_data))   #abc



#testcase2



if __name__ == "__main__":
    codes = {}

    a_great_sentence = "Udacity is the best portal for online education"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence))) #96
    print ("The content of the data is: {}\n".format(a_great_sentence))   #'Udacity is the best portal for online education'

    encoded_data, tree = huffman_encoding(a_great_sentence) 
    # print(tree)
    # print(encoded_data)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(encoded_data)))  #533
    print ("The content of the encoded data is: {}\n".format(encoded_data))  #1111101111111111111111101111111111110111111111111111101111111111011111110111101111110111111111101111111111111110111111011111110111011111111101111110110111111111011111111111111101111111011111101011111111011111111111111011111110111111111111011111111111110111111001111111101111111111111101111110111111110111111111110111111111111101111111111011111111111011111111101111110111111111011111111111111111011111111111111111101111111111111111011111111111101111111011111111110111111110111111111110

 
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) #96
    print ("The content of the decoded data is: {}\n".format(decoded_data))   #"Udacity is the best portal for online education"


#testcase3
    


if __name__ == "__main__":
    codes = {}

    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence))) #51
    print ("The content of the data is: {}\n".format(a_great_sentence))   #''

    encoded_data, tree = huffman_encoding(a_great_sentence) 
    # print(tree)
    # print(encoded_data)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(encoded_data)))  #51
    print ("The content of the encoded data is: {}\n".format(encoded_data))  #''
 
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) #51
    print ("The content of the decoded data is: {}\n".format(decoded_data))   #""
    
    

