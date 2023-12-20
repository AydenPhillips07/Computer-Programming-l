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
					self._label4 = System.Windows.Forms.Label()
					self.SuspendLayout()
					# 
					# button1
					# 
					self._button1.BackColor = System.Drawing.SystemColors.HotTrack
					self._button1.ForeColor = System.Drawing.SystemColors.ControlText
					self._button1.Location = System.Drawing.Point(107, 327)
					self._button1.Name = "button1"
					self._button1.Size = System.Drawing.Size(99, 55)
					self._button1.TabIndex = 0
					self._button1.Text = "Calculate"
					self._button1.UseVisualStyleBackColor = False
					self._button1.Click += self.Button1Click
					# 
					# button2
					# 
					self._button2.BackColor = System.Drawing.SystemColors.HotTrack
					self._button2.ForeColor = System.Drawing.SystemColors.ControlText
					self._button2.Location = System.Drawing.Point(337, 327)
					self._button2.Name = "button2"
					self._button2.Size = System.Drawing.Size(99, 55)
					self._button2.TabIndex = 1
					self._button2.Text = "Clear"
					self._button2.UseVisualStyleBackColor = False
					self._button2.Click += self.Button2Click
					# 
					# button3
					# 
					self._button3.BackColor = System.Drawing.SystemColors.HotTrack
					self._button3.ForeColor = System.Drawing.SystemColors.ControlText
					self._button3.Location = System.Drawing.Point(574, 327)
					self._button3.Name = "button3"
					self._button3.Size = System.Drawing.Size(99, 55)
					self._button3.TabIndex = 2
					self._button3.Text = "Exit"
					self._button3.UseVisualStyleBackColor = False
					self._button3.Click += self.Button3Click
					# 
					# label1
					# 
					self._label1.BackColor = System.Drawing.Color.LightSeaGreen
					self._label1.ForeColor = System.Drawing.SystemColors.ButtonFace
					self._label1.Location = System.Drawing.Point(107, 9)
					self._label1.Name = "label1"
					self._label1.Size = System.Drawing.Size(124, 60)
					self._label1.TabIndex = 3
					self._label1.Text = "Speed limit"
					self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
					self._label1.Click += self.Label1Click
					# 
					# label2
					# 
					self._label2.BackColor = System.Drawing.Color.LightSeaGreen
					self._label2.ForeColor = System.Drawing.SystemColors.ButtonFace
					self._label2.Location = System.Drawing.Point(107, 107)
					self._label2.Name = "label2"
					self._label2.Size = System.Drawing.Size(124, 60)
					self._label2.TabIndex = 4
					self._label2.Text = "Car's Speed"
					self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
					# 
					# label3
					# 
					self._label3.BackColor = System.Drawing.Color.LightSeaGreen
					self._label3.ForeColor = System.Drawing.SystemColors.ButtonFace
					self._label3.Location = System.Drawing.Point(107, 210)
					self._label3.Name = "label3"
					self._label3.Size = System.Drawing.Size(124, 60)
					self._label3.TabIndex = 5
					self._label3.Text = "Fine price$"
					self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
					# 
					# textBox1
					# 
					self._textBox1.BackColor = System.Drawing.Color.DodgerBlue
					self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._textBox1.Location = System.Drawing.Point(337, 18)
					self._textBox1.Name = "textBox1"
					self._textBox1.Size = System.Drawing.Size(193, 35)
					self._textBox1.TabIndex = 6
					self._textBox1.TextChanged += self.TextBox1TextChanged
					# 
					# textBox2
					# 
					self._textBox2.BackColor = System.Drawing.Color.DodgerBlue
					self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._textBox2.Location = System.Drawing.Point(337, 116)
					self._textBox2.Name = "textBox2"
					self._textBox2.Size = System.Drawing.Size(193, 35)
					self._textBox2.TabIndex = 7
					# 
					# label4
					# 
					self._label4.BackColor = System.Drawing.Color.DodgerBlue
					self._label4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
					self._label4.Location = System.Drawing.Point(337, 222)
					self._label4.Name = "label4"
					self._label4.Size = System.Drawing.Size(193, 36)
					self._label4.TabIndex = 8
					self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
					# 
					# MainForm
					# 
					self.BackColor = System.Drawing.Color.DarkSlateGray
					self.ClientSize = System.Drawing.Size(914, 574)
					self.Controls.Add(self._label4)
					self.Controls.Add(self._textBox2)
					self.Controls.Add(self._textBox1)
					self.Controls.Add(self._label3)
					self.Controls.Add(self._label2)
					self.Controls.Add(self._label1)
					self.Controls.Add(self._button3)
					self.Controls.Add(self._button2)
					self.Controls.Add(self._button1)
					self.Name = "MainForm"
					self.Text = "prog82a"
					self.ResumeLayout(False)
					self.PerformLayout()


    def Label1Click(self, sender, e):
        pass

    def TextBox1TextChanged(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        num1 = int(self._textBox1.Text)
        num2 = int(self._textBox2.Text)
        num3 = num2 - num1
        num4 = num3 * 5.00 + 20.00
        self._label4.Text = str(num4)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label4.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()   
