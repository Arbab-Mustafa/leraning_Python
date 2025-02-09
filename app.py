# Author:  Arbab Mustafa

from guess import GuessNumber
from calculator import Calculator
from stuent import  write, readfile
from a import read,write
from api import data_get

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
    data_get("/data", params={"key": "value"})

    







if __name__ == "__main__":
    main()

             