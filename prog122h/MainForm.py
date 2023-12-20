import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.LightCoral
		self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.ForeColor = System.Drawing.Color.White
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 20
		self._listBox1.Location = System.Drawing.Point(106, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.ScrollAlwaysVisible = True
		self._listBox1.Size = System.Drawing.Size(586, 324)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Firebrick
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(34, 387)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(132, 97)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Firebrick
		self._button2.ForeColor = System.Drawing.Color.White
		self._button2.Location = System.Drawing.Point(334, 387)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(132, 97)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Firebrick
		self._button3.ForeColor = System.Drawing.Color.White
		self._button3.Location = System.Drawing.Point(648, 387)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(132, 97)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self.ClientSize = System.Drawing.Size(813, 496)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "prog122h"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		Header = "Number\t Square\t Square Root\t Cube\t Fourth Root"
		self._listBox1.Items.Add(Header)
		for num in range(1, 20+1):
			square = num**2
			squareroot = math.sqrt(num)
			cube = num** 3
			fourthroot = num** 0.25
			columns = str(num) + "\t" + str(square) + "\t" + str(squareroot) + "\t" + str(cube) + "\t" + str(fourthroot)
			self._listBox1.Items.Add(columns)	
			
			
			
			
			
	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()