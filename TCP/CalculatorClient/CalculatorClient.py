
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

def runserver():
    while True:
        serverHost = '127.0.0.1' # host name
        serverPort = 12000 # port number
        
        clientSocket = socket(AF_INET, SOCK_STREAM) # create socket. AF_INET is IPv4, SOCK_STREAM is TCP
        clientSocket.connect((serverHost, serverPort)) # connect to server
        
        action = input("Enter the action (Random, Add, Subtract): ") # get input from user
        if action.lower() == "random" or action.lower() == "add" or action.lower() == "subtract":
            clientSocket.send(action.encode())
        else:
            print("Please enter a valid action")
            action = input("Enter the action (Random, Add, Subtract): ") # get input from user


        num1 = input("Enter the first number (Int or Float): ") # get input from user
        if isdigit(num1) or isfloat(num1):
             clientSocket.send(num1.encode()) # send message to server
        else:
            print("Please enter a number")
            num1 = input("Enter the first number (Int or Float): ") 
                           
            

        num2 = input("Enter the second number (Int or Float): ") # get input from user
        if isdigit(num2) or isfloat(num2):
             clientSocket.send(num2.encode()) # send message to server
        else:
            print("Please enter a number")
            num2 = input("Enter the second number (Int or Float): ")
                                        
        result = clientSocket.recv(1024) # receive message from server
        print("From Server: ", result.decode()) # print message
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

