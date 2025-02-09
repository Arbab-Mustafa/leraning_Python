import json
def read(txtFile):
  try:
      with open(txtFile, 'r') as f:
         data = f.readlines()
         print("File content",data)
         
         for line in data:
              print(line.strip())
  except(FileNotFoundError, json.JSONDecodeError):
        print("File not found")
        print("Or File is empty")
      

def write(txtFile):
    try:
        with  open(txtFile, 'r') as f:
            data = f.readlines()
            if not isinstance(data,list):
                data=[]
    except(FileNotFoundError, json.JSONDecodeError):
        data = []
        



    with open(txtFile, 'w') as f:
        data.append("This is a new line3\n")
        f.writelines(data)
        print("File is written successfully")  
        

     
     
