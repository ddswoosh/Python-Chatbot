from main import Bot
import pyodbc

connection_string = ("Driver={SQL Server}; Server=PC\SQLEXPRESS;Database=nc_auth;trusted_connetion=Yes;")

conn = pyodbc.connect(connection_string)
cur = conn.cursor()

data = cur.execute("SELECT * FROM User_auth")
        
class Data:
    
    def __init__(self):
        
        self.head = int(1)
        self.current_node = self.head
        self.next = self.current_node + int(1)

#         self.username = #input(pyscript.js)
#         self.password = #input(pyscript.js)
        self.auth = "attempt"
    
    def firstNode(self):
        con.execute(f"INSERT INTO (ID,Username,Password) VALUES ({self.current_node},{self.username},{self.password})")
        self.current_node = self.next
        self.auth = True
             
    def nextNode(self):
        self.current_node = self.next 
        con.execute(f"INSERT INTO (ID) VALUES ({self.current_node},{self.username},{self.password})")
        self.auth = True

    def auth(self):
        if self.username in data:
            if self.password in data:
                done = con.execute(f"SELECT ID FROM User_auth WHERE Username = {self.username} AND Password = {self.password}")
                return done and self.auth = True

        else:
            self.auth = False
            js.alert = print("Authorization Error")
                      
            
    def run(self):
        if self.auth == "attempt":    
            d.auth()
        
        elif self.auth == False:
            if self.current_node == self.head:
                d.firstNode()
            elif self.current_node == self.next:
                d.nextNode()
        
    def storeVar(self):
        if self.auth == True:
            con.execute(f"SELECT * FROM User_data WHERE ID = {self.current_node}")
        
                   
d = Data()
d.run()



#imported bot class from backend file and will link together to store variables such as credit score in database
#all username and passwords auths will be given a unique ID and this will be the primary key of the auththenication databse
#while being the foreign key in the user data database so we can access it at anytime after auth
