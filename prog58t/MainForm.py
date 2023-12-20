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
					self._textBox1 = System.Windows.Forms.TextBox()
					self._textBox2 = System.Windows.Forms.TextBox()
					self.SuspendLayout()
					# 
					# button1
					# 
					self._button1.BackColor = System.Drawing.Color.LawnGreen
					self._button1.Location = System.Drawing.Point(2, 97)
					self._button1.Name = "button1"
					self._button1.Size = System.Drawing.Size(123, 72)
					self._button1.TabIndex = 0
					self._button1.Text = "Calculate"
					self._button1.UseVisualStyleBackColor = False
					self._button1.Click += self.Button1Click
					# 
					# button2
					# 
					self._button2.BackColor = System.Drawing.Color.LawnGreen
					self._button2.Location = System.Drawing.Point(123, 97)
					self._button2.Name = "button2"
					self._button2.Size = System.Drawing.Size(123, 72)
					self._button2.TabIndex = 1
					self._button2.Text = "Clear"
					self._button2.UseVisualStyleBackColor = False
					self._button2.Click += self.Button2Click
					# 
					# button3
					# 
					self._button3.BackColor = System.Drawing.Color.LawnGreen
					self._button3.Location = System.Drawing.Point(242, 97)
					self._button3.Name = "button3"
					self._button3.Size = System.Drawing.Size(123, 72)
					self._button3.TabIndex = 2
					self._button3.Text = "Exit"
					self._button3.UseVisualStyleBackColor = False
					self._button3.Click += self.Button3Click
					# 
					# label1
					# 
					self._label1.BackColor = System.Drawing.Color.GreenYellow
					self._label1.Location = System.Drawing.Point(25, 16)
					self._label1.Name = "label1"
					self._label1.Size = System.Drawing.Size(100, 23)
					self._label1.TabIndex = 3
					self._label1.Text = "Price"
					self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
					# 
					# label2
					# 
					self._label2.BackColor = System.Drawing.Color.GreenYellow
					self._label2.Location = System.Drawing.Point(2, 43)
					self._label2.Name = "label2"
					self._label2.Size = System.Drawing.Size(143, 35)
					self._label2.TabIndex = 4
					self._label2.Text = "Amount given"
					self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
					# 
					# label3
					# 
					self._label3.BackColor = System.Drawing.SystemColors.ActiveCaptionText
					self._label3.ForeColor = System.Drawing.Color.LightGreen
					self._label3.Location = System.Drawing.Point(409, 8)
					self._label3.Name = "label3"
					self._label3.Size = System.Drawing.Size(296, 286)
					self._label3.TabIndex = 5
					self._label3.TextAlign = System.Drawing.ContentAlignment.TopCenter
					# 
					# textBox1
					# 
					self._textBox1.BackColor = System.Drawing.SystemColors.HotTrack
					self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._textBox1.ForeColor = System.Drawing.SystemColors.MenuBar
					self._textBox1.Location = System.Drawing.Point(151, 16)
					self._textBox1.Name = "textBox1"
					self._textBox1.Size = System.Drawing.Size(112, 31)
					self._textBox1.TabIndex = 6
					# 
					# textBox2
					# 
					self._textBox2.BackColor = System.Drawing.Color.DarkSlateGray
					self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._textBox2.ForeColor = System.Drawing.SystemColors.Window
					self._textBox2.Location = System.Drawing.Point(151, 47)
					self._textBox2.Name = "textBox2"
					self._textBox2.Size = System.Drawing.Size(112, 31)
					self._textBox2.TabIndex = 7
					# 
					# MainForm
					# 
					self.BackColor = System.Drawing.Color.DarkGreen
					self.ClientSize = System.Drawing.Size(718, 303)
					self.Controls.Add(self._textBox2)
					self.Controls.Add(self._textBox1)
					self.Controls.Add(self._label3)
					self.Controls.Add(self._label2)
					self.Controls.Add(self._label1)
					self.Controls.Add(self._button3)
					self.Controls.Add(self._button2)
					self.Controls.Add(self._button1)
					self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self.Name = "MainForm"
					self.Text = "prog58t"
					self.Load += self.MainFormLoad
					self.ResumeLayout(False)
					self.PerformLayout()


    def Button1Click(self, sender, e):
        p = float(self._textBox1.Text)
        r = float(self._textBox2.Text)
        change = r - p
        Dollar = change // 1
        Quarter = (change - Dollar) // 0.25
        Dimes = (change - Dollar - (Quarter / 4)) // 0.10
        Nickels = (change - Dollar - (Quarter / 4) - (Dimes / 10)) // 0.05
        Pennies = (change - Dollar - (Quarter / 4) - (Dimes / 10) - (Nickels / 20)) // 0.01
        
        self._label3.Text = "Dollar: " + str(Dollar) + "\nQuarters: " + str(Quarter) + "\nDimes" + str(Dimes) + "\nNickels: " + str(Nickels) + "\nPennies: " + str(Pennies)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label3.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()   

		
		
		
		
		
		
		

	

	def MainFormLoad(self, sender, e):
		pass