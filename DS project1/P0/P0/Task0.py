"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

data1=texts[0]
print("First record of texts,{} texts {} at time {}".format(data1[0],data1[1],data1[2]))

data2=calls[-1]
print("last record of calls,{} calls {} at time {},lasting {} seconds".format(data2[0],data2[1],data2[2],data2[3]))

"""
BIG-O_NOTATION:Notation: (O(1))
"""
