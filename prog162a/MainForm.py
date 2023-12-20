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
					self._textBox1 = System.Windows.Forms.TextBox()
					self._label1 = System.Windows.Forms.Label()
					self._label2 = System.Windows.Forms.Label()
					self.SuspendLayout()
					# 
					# button1
					# 
					self._button1.BackColor = System.Drawing.Color.DarkGreen
					self._button1.ForeColor = System.Drawing.Color.White
					self._button1.Location = System.Drawing.Point(486, 0)
					self._button1.Name = "button1"
					self._button1.Size = System.Drawing.Size(212, 133)
					self._button1.TabIndex = 0
					self._button1.Text = "Calculate"
					self._button1.UseVisualStyleBackColor = False
					self._button1.Click += self.Button1Click
					# 
					# button2
					# 
					self._button2.BackColor = System.Drawing.Color.DarkGreen
					self._button2.ForeColor = System.Drawing.Color.White
					self._button2.Location = System.Drawing.Point(486, 152)
					self._button2.Name = "button2"
					self._button2.Size = System.Drawing.Size(212, 133)
					self._button2.TabIndex = 1
					self._button2.Text = "Clear"
					self._button2.UseVisualStyleBackColor = False
					self._button2.Click += self.Button2Click
					# 
					# button3
					# 
					self._button3.BackColor = System.Drawing.Color.DarkGreen
					self._button3.ForeColor = System.Drawing.Color.White
					self._button3.Location = System.Drawing.Point(486, 310)
					self._button3.Name = "button3"
					self._button3.Size = System.Drawing.Size(213, 132)
					self._button3.TabIndex = 2
					self._button3.Text = "Exit"
					self._button3.UseVisualStyleBackColor = False
					self._button3.Click += self.Button3Click
					# 
					# textBox1
					# 
					self._textBox1.BackColor = System.Drawing.Color.SpringGreen
					self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._textBox1.Location = System.Drawing.Point(287, 37)
					self._textBox1.Name = "textBox1"
					self._textBox1.Size = System.Drawing.Size(157, 31)
					self._textBox1.TabIndex = 3
					# 
					# label1
					# 
					self._label1.BackColor = System.Drawing.Color.LightGreen
					self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._label1.ForeColor = System.Drawing.Color.Black
					self._label1.Location = System.Drawing.Point(2, 9)
					self._label1.Name = "label1"
					self._label1.Size = System.Drawing.Size(279, 92)
					self._label1.TabIndex = 4
					self._label1.Text = "Enter a Number"
					# 
					# label2
					# 
					self._label2.BackColor = System.Drawing.Color.Chartreuse
					self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._label2.ForeColor = System.Drawing.Color.Black
					self._label2.Location = System.Drawing.Point(3, 101)
					self._label2.Name = "label2"
					self._label2.Size = System.Drawing.Size(477, 347)
					self._label2.TabIndex = 5
					# 
					# MainForm
					# 
					self.BackColor = System.Drawing.Color.SeaGreen
					self.ClientSize = System.Drawing.Size(710, 478)
					self.Controls.Add(self._label2)
					self.Controls.Add(self._label1)
					self.Controls.Add(self._textBox1)
					self.Controls.Add(self._button3)
					self.Controls.Add(self._button2)
					self.Controls.Add(self._button1)
					self.Name = "MainForm"
					self.Text = "prog162a"
					self.ResumeLayout(False)
					self.PerformLayout()


    def Button1Click(self, sender, e):
        Num1 = self._textBox1.Text
        Num1 = int(Num1)
        l = 1
        if Num1 > 0:
            for num in range(1, Num1+1):
                l = num * l
            self._label2.Text = "The Value" + str(Num1) + "! is" + str(l)
        else:
            self.label1.Text = ""
        
        
    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._label2.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()   
	