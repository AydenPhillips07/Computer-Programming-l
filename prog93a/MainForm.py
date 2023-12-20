import math
import System.Drawing
import System.Windows.Forms
from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.MediumSlateBlue
		self._button1.Location = System.Drawing.Point(41, 385)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(149, 105)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.MediumSlateBlue
		self._button2.Location = System.Drawing.Point(320, 385)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(149, 105)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.MediumSlateBlue
		self._button3.Location = System.Drawing.Point(615, 385)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(149, 105)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.MediumSlateBlue
		self._label1.Location = System.Drawing.Point(31, 21)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(144, 55)
		self._label1.TabIndex = 3
		self._label1.Text = "Enter KWH Used"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.MediumSlateBlue
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(212, 31)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 35)
		self._textBox1.TabIndex = 4
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.MediumSlateBlue
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(347, 9)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(447, 356)
		self._label2.TabIndex = 5
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkOrange
		self.ClientSize = System.Drawing.Size(806, 490)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog93a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		kwused = int(self._textBox1.Text)
		kwph = kwused * 0.0475
		basecharge = round(kwph, 2)
		surcharge = basecharge * 0.10
		Surcharge = round(surcharge, 2)
		citytax = basecharge * 0.03
		Citytax = round(citytax, 2)
		amountdue = basecharge + Surcharge + Citytax
		latepenalty = amountdue * 0.04
		Latepenalty = round(latepenalty, 2)
		LatePenalty = amountdue + Latepenalty
		
		
		self._label2.Text = "Base Rate :" + str(kwused) + " x 4.75 cents" + " = $" + str(basecharge) + "\n Surcharge $" + str(Surcharge) + "\n City Tax $" + str(Citytax) + "\n ------------- " + "\n Pay this amount : $" + str(amountdue) + "\n -------------" + "\n After May 20th, pay : $" + str(LatePenalty) 

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label2.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()