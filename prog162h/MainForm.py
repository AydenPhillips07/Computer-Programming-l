import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(500, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(274, 86)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(249, 66)
		self._label1.TabIndex = 1
		self._label1.Text = "Enter Number of Guests"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(297, 33)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 26)
		self._textBox1.TabIndex = 2
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(297, 99)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 26)
		self._textBox2.TabIndex = 4
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(12, 75)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(249, 66)
		self._label2.TabIndex = 3
		self._label2.Text = "Enter Number of Chairs"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(64, 208)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(333, 206)
		self._label3.TabIndex = 5
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(500, 113)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(274, 86)
		self._button2.TabIndex = 6
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(500, 208)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(274, 86)
		self._button3.TabIndex = 7
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(786, 506)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog162h"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		if Chair > Guest
			
		 

	def Button2Click(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		pass