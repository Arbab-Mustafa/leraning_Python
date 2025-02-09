import json

def readfile(DataFile):
    try:
         with open(DataFile, 'r') as f:
          data= json.load(f)
      
         for data in data:
           print("Name: ", data['name'])
           print("Age: ", data['age'])
           print("City: ", data['city'])
    except(FileNotFoundError, json.JSONDecodeError):
        print("File not found")
        print("Or File is empty")
        

     


def write(DataFile):
    try:
     
     with open(DataFile, 'r') as f:
        data = json.load(f)
        if not isinstance(data,list):
                data=[]

    except(FileNotFoundError, json.JSONDecodeError):
        data = []



    data.append({'name': 'Arbab2', 'age': 22, 'city': 'Karachi'})


    with open(DataFile, 'w') as f:
        json.dump(data, f, indent=4)
        print("Total Element",data.index(data[-1]))
     

 
           

     