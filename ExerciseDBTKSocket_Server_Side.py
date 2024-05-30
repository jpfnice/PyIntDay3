"""

Exercise:

The goal is to develop a client<->server program using a stream socket.

The server is in charge of returning information about a product 
(given it's name). The server will make use of the SQlLite table "product" 
created yesterday.

The "client", with the help of a GUI (see NewGUIDBExercise.py in 
https://github.com/jpfnice/PyIntDay3AM), will send a product name to the
server. And will then wait for the server to return it's corresponding 
price and qty.
If the product name does not exist, the server will return an error message.

"""
import socket

def getProduct(name):
    import sqlite3
    try:
        conn=sqlite3.connect(r"epfl.db")
        cursor=conn.cursor()
        cursor.execute (f"SELECT * FROM product where name='{name}'")
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row
    except Exception as ex:
        print(ex)


try:
    sock_srv=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_srv.bind(("localhost", 34566)) # nmap or netstat
    sock_srv.listen(2)
    while True:
        print("Server ready")
        sock_cli, addr_cli=sock_srv.accept()
        print(f"connection established with {addr_cli}")
        try:
                
            messageB=sock_cli.recv(40)
            # messageB is a "bytes" object
            messageS=messageB.decode() # to transform bytes into str
            print(f"message received: {messageS}")
            
            resp=getProduct(messageS)
            if resp== None: # If the product name does not exist, 
                            # it returns an empty list to the client
                resp=[]
            
            import pickle 
            # If the product name exist, 
            # it returns, with the help of pickle, a list to the client
            # this list (returned by the select statement) represent a row
            # of the table "product"
            sock_cli.send(pickle.dumps(resp))

        except:
            sock_cli.close()
            break
        
    sock_srv.close()
except Exception as ex:
    print(ex)

