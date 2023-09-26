
from socket import *
from random import randint


def isdigit(num): 
    try:
        int(num)
        return True
    except ValueError:
        return False
    

def runserver():
    serverPort = 12000  # Port number
    serverHost = '127.0.0.1'  # Host name

    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSocket.bind((serverHost, serverPort))
    serverSocket.listen(1)
    print("The server is ready to receive")

    connectionSocket, address = serverSocket.accept()
    print("Connection from:", address)


    actionRecv = connectionSocket.recv(1024).decode()
    num1recv = connectionSocket.recv(1024).decode()   
    num2recv = connectionSocket.recv(1024).decode()
    
    if isdigit(num1recv) == False:
        num1 = float(num1recv)
    else:
        num1 = int(num1recv)


    if isdigit(num2recv) == False:
        num2 = float(num2recv)
    else:
        num2 = int(num2recv)
    
    action = str(actionRecv)

    def calculate(num1, num2, action):
        
        if action.lower() == "random": 
            if num1 > num2:
                calc = randint(num2, num1) # Random number between num2 and num1
                return f"A random number between {num2} and {num1} = {calc}"
            else:
                calc = randint(num1, num2) # Random number between num1 and num2
                return f"A random number between {num1} and {num2} = {calc}"
        
        elif action.lower() == "add":
            calc = num1 + num2
            return f"Result of {num1} + {num2} = {calc}"
        
        elif action.lower() == "subtract":
            calc = num1 - num2
            return f"Result of {num1} - {num2} = {calc}"
        else:
            return "Please enter a valid action" # Added security, even though this is handled client side

    result = calculate(num1, num2, action)
    print("Sending:", result)
    connectionSocket.send(result.encode())
    connectionSocket.close()
    serverSocket.close()

def runAgain():
    while True:
       runserver()


runAgain()

