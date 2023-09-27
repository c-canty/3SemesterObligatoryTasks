
import json
from socket import *



def isfloat(s): # check if input is a float
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def isdigit(s): # check if input is a digit
    try:
        int(s)
        return True
    except ValueError:
        return False
    

class Submission:
    def __init__(self, action, num1, num2, answer=0): # constructor, sets answer to 0 by default
        self.action = action
        self.num1 = num1
        self.num2 = num2
        self.answer = answer
        
    def __str__(self):
        return "\nAction: " + self.action + "\nNumber 1: " + self.num1.__str__() + "\nNumber 2: " + self.num2.__str__() + "\nAnswer: " + self.answer.__str__() # print message

def runserver():
    while True:
        serverHost = '127.0.0.1' # host name
        serverPort = 12000 # port number
        
        clientSocket = socket(AF_INET, SOCK_STREAM) # create socket. AF_INET is IPv4, SOCK_STREAM is TCP
        clientSocket.connect((serverHost, serverPort)) # connect to server
                
        
        action = input("Enter the action (Random, Add, Subtract): ") # get input from user
        if action.lower() == "random" or action.lower() == "add" or action.lower() == "subtract":
            pass
        else:
            print("Please enter a valid action")
            action = input("Enter the action (Random, Add, Subtract): ") # get input from user


        num1 = input("Enter the first number (Int or Float): ") # get input from user
        if isdigit(num1) or isfloat(num1):
             pass
        else:
            print("Please enter a number")
            num1 = input("Enter the first number (Int or Float): ") 
                           
            

        num2 = input("Enter the second number (Int or Float): ") # get input from user
        if isdigit(num2) or isfloat(num2):
             pass
        else:
            print("Please enter a number")
            num2 = input("Enter the second number (Int or Float): ")
            
        
        SendSubmission = Submission(action, num1, num2) # create object
        
        JSONSubmission = json.dumps(SendSubmission.__dict__) # convert object to JSON
        
        clientSocket.send(JSONSubmission.encode()) # send object to server
        
                                        
        resultJSON = clientSocket.recv(1024).decode() # receive message from server
        
        result = json.loads(resultJSON) # convert JSON to object
        
        ResultSubmission = Submission(result['action'], result['num1'], result['num2'], result['answer']) # create object
        
        print("From Server: ", ResultSubmission.__str__()) # print message
        clientSocket.close() # close connection
        return True
    

def runAgain():

    ask = input("Would you like to connect? (y/n): ")
    while ask.lower() == "y":
        runserver() 
               
        runAgain()
        
        
    if ask.islower == "n" or "exit":
            print("Goodbye!")
            exit()
    else:
        print("Please enter y or n")
        runAgain()

runAgain() 


