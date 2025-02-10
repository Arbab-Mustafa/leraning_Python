# Author:  Arbab Mustafa

from guess import GuessNumber
from calculator import Calculator
from stuent import  write, readfile
from a import read,write
from api import  GetIP

DataFile = "./student.json"
a= "a.txt"

def main():
     # GuessNumber()
     # print("Calculator")
     # print("Enter first number: ")
     # x = int(input())
     # print("Enter second number: ")
     # y = int(input())
     # Calculator(x,y)

    # write(DataFile)
    # readfile(DataFile)

    # write(a)
    # read(a)
    data = GetIP("/data", None)

    if isinstance(data, dict):  # Ensure data is a dictionary
        print(data.get('hostname', 'N/A'))
        print(data.get('city', 'N/A'))
        print(data.get('region', 'N/A'))
    else:
        print("Invalid response received")








if __name__ == "__main__":
    main()

             