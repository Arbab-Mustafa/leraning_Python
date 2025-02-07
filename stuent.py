import json

DataFile = 'students.json'

 

def readfile():
 with open(DataFile, 'r') as f:
      data= json.load(f)
      
 for data in data:
   print("Name: ", data['name'])
   print("Age: ", data['age'])
   print("City: ", data['city'])
     
  