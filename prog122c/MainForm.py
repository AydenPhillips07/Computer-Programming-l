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
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(78, 392)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(133, 75)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Cursor = System.Windows.Forms.Cursors.Arrow
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(339, 392)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(133, 75)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(587, 392)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(133, 75)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.White
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(170, 35)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(570, 47)
		self._label1.TabIndex = 3
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.White
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(170, 101)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(570, 47)
		self._label2.TabIndex = 5
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.White
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(170, 172)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(570, 47)
		self._label3.TabIndex = 7
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.White
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(170, 244)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(570, 47)
		self._label4.TabIndex = 9
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.White
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(170, 312)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(570, 47)
		self._label5.TabIndex = 11
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(812, 511)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog122c"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		lb1 = 2
		lb2 = lb1 + 1
		lb3 = lb1 * 2
		lb4 = lb1 * lb1
		self._label1.Text = str(lb1) + "              " + str(lb2) + "              " + str(lb3) + "              " + str(lb4)
		Lb1 = 4
		Lb2 = Lb1 + 1
		Lb3 = Lb1 * 2
		Lb4 = Lb1 * Lb1
		self._label2.Text = str(Lb1) + "              " + str(Lb2) + "              " + str(Lb3) + "              " + str(Lb4)
		lB1 = 6
		lB2 = lB1 + 1
		lB3 = lB1 * 2
		lB4 = lB1 * lB1
		self._label3.Text = str(lB1) + "              " + str(lB2) + "              " + str(lB3) + "              " + str(lB4)
		LB1 = 8
		LB2 = LB1 + 1
		LB3 = LB1 * 2
		LB4 = LB1 * LB1
		self._label4.Text = str(LB1) + "              " + str(LB2) + "              " + str(LB3) + "              " + str(LB4)
		LBL1 = 10
		LBL2 = LBL1 + 1
		LBL3 = LBL1 * 2
		LBL4 = LBL1 * LBL1
		self._label5.Text = str(LBL1) + "             " + str(LBL2) + "            " + str(LBL3) + "           " + str(LBL4)
	def Button2Click(self, sender, e):
		self._label1.Text = ""
		self._label2.Text = ""
		self._label3.Text = ""
		self._label4.Text = ""
		self._label5.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()