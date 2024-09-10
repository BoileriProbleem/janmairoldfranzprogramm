from flask import Flask
from tkinter import *

testtxt = "argus"

root = Tk()

root.geometry("500x500")
root.title("ui")

def testfun():
    testtxt = "saku"

testbtn = Button(root, text="klik", command=testfun) 
testbtn.pack()


root.mainloop()


app = Flask(__name__)

@app.route("/")
def home():
    return testtxt