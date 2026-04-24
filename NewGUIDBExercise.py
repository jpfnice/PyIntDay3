"""
The goal is to complete this code (TODO comments) in order for this script
to be able to retrieve, from a socket service, the price and the qty of the 
corresponding product.

There will be a need, int order for this client to work, to define a "Socket Service" that will implement the following protocol:
    
    1) The service expect it's client to send the name of a product
    2) the service will search the product name in the table "product" 
    (database file epfl.db in https://github.com/jpfnice/PyIntDay2)
    3) if the product exist, the service send back to the client the price and 
    the qty of the product.
    Note: you could implement the service in such a way that it sends back to the     client the whole product object as bytes (using pickle), but it is simply an option
    4) if the product does not exist, the service send back a error message to 
    the client
    5) The client will send a "stop" message to inform the service it does not 
    need anything else

"""

import tkinter as tk
import tkinter.messagebox as mb

class MyWindow(tk.Tk):
    
    def __init__(self):
        super().__init__() # To call the method __init__() of the "super" class (here Tk)
        
        self.minsize(900,300)
        self.maxsize(1200,600)
        self.title("Tkinter Exercise")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        # Binding variables:
        self.nameStr=tk.StringVar()
        self.priceFloat=tk.DoubleVar()
        self.qtyInt=tk.IntVar()

        nameL=tk.Label(self, text="Name")
        nameL.grid(row=0, column=0, padx=10, pady=10)
        
        nameE=tk.Entry(self, textvariable=self.nameStr)
        nameE.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E+tk.W)
        
        priceL=tk.Label(self, text="Price")
        priceL.grid(row=0, column=1, padx=10, pady=10)
        
        priceE=tk.Entry(self, textvariable=self.priceFloat)
        priceE.grid(row=1, column=1, padx=10, pady=10, sticky=tk.E+tk.W)
        
        qtyL=tk.Label(self, text="Qty")
        qtyL.grid(row=0, column=2, padx=10, pady=10)
        
        qtyE=tk.Entry(self, textvariable=self.qtyInt)
        qtyE.grid(row=1, column=2, padx=10, pady=10, sticky=tk.E+tk.W)
        
        loadB=tk.Button(self, text="Load", command=self.load)
        loadB.grid(row=1, column=3, padx=10, pady=10)
        
        self.setMenu()

        
    def setMenu(self):
        import sys
        mainmenu = tk.Menu(self)  # MenuBar 
        menuFile = tk.Menu(mainmenu)  # Menu 
        menuFile.add_command(label="Quit", command=sys.exit) 
  
        menuHelp = tk.Menu(mainmenu) # Menu
        menuHelp.add_command(label="About", command=self.about) 
        
        mainmenu.add_cascade(label = "File", menu=menuFile) 
        mainmenu.add_cascade(label = "Help", menu=menuHelp) 
        
        # display the menu
        self.config(menu = mainmenu) 
        
    def load(self):

        try:
            pass
            # TODO: send a Product name to a Socket Server and get it's 
            # Price and Qty
        except Exception as ex:
            print(ex)
      
    def about(self): 
        mb.showinfo("A tkinter example", "Version 1.0")       
               
if __name__== "__main__":
    win=MyWindow()
    tk.mainloop()