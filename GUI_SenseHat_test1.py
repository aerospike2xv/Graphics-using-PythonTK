# --------------------------------------------------------------------------------------- #
# ------------- GRAPHICAL INTERFACE FOR RASPBERRY PI - SENSE HAT MODULE ----------------- #
# --------------------------------------------------------------------------------------- #

# Author : Abhishek Sharma, BioMIP, Ruhr University, Germany.
# Email  : abhishek.sharma@rub.de 
# Date   : Friday, 11.11.2016

"""
    --- Description --- 
    
    -> LED Array : 8 x 8 
    -> RGB LEDs  : [R, G, B]
    
    The LED Matrix layout looks like :
      + --------------- +
      | o o o o o o o o |
      | o o o o o o o o |
      | o o o o o o o o |
      | o o o o o o o o |
      | o o o o o o o o |
      | o o o o o o o o |
      | o o o o o o o o |
      | o o o o o o o o | 
      + --------------- +
    
    -> Clicking buttons : 1 -> Red   : (255, 0, 0)
                          2 -> Green : (0, 255, 0)
                          3 -> Blue  : (0, 0, 255)
                          4 -> Off   : (0, 0, 0)
"""

import sys
import Tkinter as Tk
import tkMessageBox
import numpy as np
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

class RPiLEDMatrix(Tk.Frame):
	
	def __init__(self, parent):
		Tk.Frame.__init__(self, parent)
		self.parent = parent
		
		# Setting colors for Sense Hat
		self.dark = (0, 0, 0)
		self.red = (255, 0, 0)
		self.green = (0, 255, 0)
		self.blue = (0, 0, 255)
		self.white = (255, 255, 255)
		
		# Background : Dark : 0 / White : 1
		self.background = 0
		
		self.startGUI()
			
    
	def startGUI(self):
		
		'''
		  Creates GUI for Raspberry Pi : Sense Hat.
		'''
		
		self.parent.title("RPi SenseHat")
		self.parent.grid_rowconfigure(1, weight=1)
		self.parent.grid_columnconfigure(1, weight=1)
		
		self.frame = Tk.Frame(self.parent)
		self.frame.pack(fill=Tk.X, padx=5, pady=5)
		
		self.frame2 = Tk.Frame(self.parent)
		self.frame2.pack(fill=Tk.X, padx=5, pady=5)
		
		# Creating Buttons : 8 x 8 Led Matrix
		self.dim = 8
		self.arr = np.zeros((self.dim, self.dim))
		
		self.buttonGrid = []
		self.buttonClickCount = np.zeros((self.dim, self.dim))
		
		for i in range(0, self.arr.shape[0]):
			row = []
			for j in range(0, self.arr.shape[1]):
				self.button = Tk.Button(self.frame, bg = 'white', text = str(i+1)+ str(j+1), 
					command = lambda i=i, j=j: self.testButton(i, j))
				row.append(self.button)
				row[-1].grid(row=i,column=j)
			
			self.buttonGrid.append(row)
		
		self.startLEDMatrix()		
	
	def startLEDMatrix(self):
		
		for i in range(self.dim):
			for j in range(self.dim):
				if self.background == 0:
					sense.set_pixel(i, j, self.dark)
				else:
					sense.set_pixel(i, j, self.white)								
				
	def testButton(self, posX, posY):		
		
		print "button : ", (posX+1), " ", (posY+1), " count: ", self.buttonClickCount[posX][posY]
		self.buttonClickCount[posX][posY] += 1	
		
		if self.buttonClickCount[posX][posY] == 1:
			self.buttonGrid[posX][posY]["bg"] = 'red'
			sense.set_pixel(posX, posY, self.red)
		
		elif self.buttonClickCount[posX][posY] == 2:
			self.buttonGrid[posX][posY]["bg"] = 'green'
			sense.set_pixel(posX, posY, self.green)
		     
		elif self.buttonClickCount[posX][posY] == 3:
			self.buttonGrid[posX][posY]["bg"] = 'blue'
			self.buttonClickCount[posX][posY] = 0
			sense.set_pixel(posX, posY, self.blue)
		
		else:
			self.buttonGrid[posX][posY]["bg"] = 'white'
			sense.set_pixel(posX, posY, self.white)
		
				
if __name__ == "__main__":
	root = Tk.Tk()
	app = RPiLEDMatrix(root) 
	root.mainloop()			




		    
        








