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
        self.auth = False
    
    def firstNode(self):
        if self.auth == False:
            if self.current_node == self.head:
                con.execute(f"INSERT INTO (ID,Username,Password) VALUES ({self.current_node},{self.username},{self.password}")
                self.auth = True
            else:
                d.secondNode()
             
    def secondNode(self):
        if self.auth == False:
            if self.current_node == self.head:
                self.current_node = self.next
                con.execute(f"INSERT INTO (ID) VALUES ({self.next},{self.username},{self.password}")
                self.auth = True
            else:
                d.nextNode()
               
    def nextNode(self):
        if self.auth == False:
            if self.current_node == self.next:
                self.next = self.next + int(5)
                con.execute(f"INSERT INTO (ID) VALUES ({self.next},{self.username},{self.password}")
                self.auth = True
            else:
                d.auth()
        
    def auth(self):
        if self.username in data:
            if self.password in data:
                done = con.execute(f"SELECT ID FROM User_auth WHERE Username = {self.username} AND Password = {self.password}")
                return done and self.auth = True

        else:
            js.alert = print("Authorization Error")

        
d = Data()
d.firstNode()
