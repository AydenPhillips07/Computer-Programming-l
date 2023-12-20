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
					self._listBox1 = System.Windows.Forms.ListBox()
					self._textBox1 = System.Windows.Forms.TextBox()
					self._label1 = System.Windows.Forms.Label()
					self.SuspendLayout()
					# 
					# button1
					# 
					self._button1.BackColor = System.Drawing.Color.DimGray
					self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._button1.ForeColor = System.Drawing.Color.DarkViolet
					self._button1.Location = System.Drawing.Point(514, 160)
					self._button1.Name = "button1"
					self._button1.Size = System.Drawing.Size(152, 109)
					self._button1.TabIndex = 0
					self._button1.Text = "Calculate"
					self._button1.UseVisualStyleBackColor = False
					self._button1.Click += self.Button1Click
					# 
					# button2
					# 
					self._button2.BackColor = System.Drawing.Color.DimGray
					self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._button2.ForeColor = System.Drawing.Color.DarkViolet
					self._button2.Location = System.Drawing.Point(514, 275)
					self._button2.Name = "button2"
					self._button2.Size = System.Drawing.Size(150, 109)
					self._button2.TabIndex = 1
					self._button2.Text = "Clear"
					self._button2.UseVisualStyleBackColor = False
					self._button2.Click += self.Button2Click
					# 
					# button3
					# 
					self._button3.BackColor = System.Drawing.Color.DimGray
					self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._button3.ForeColor = System.Drawing.Color.DarkViolet
					self._button3.Location = System.Drawing.Point(514, 390)
					self._button3.Name = "button3"
					self._button3.Size = System.Drawing.Size(149, 109)
					self._button3.TabIndex = 2
					self._button3.Text = "Exit"
					self._button3.UseVisualStyleBackColor = False
					self._button3.Click += self.Button3Click
					# 
					# listBox1
					# 
					self._listBox1.BackColor = System.Drawing.SystemColors.ActiveCaptionText
					self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._listBox1.ForeColor = System.Drawing.Color.DarkOrchid
					self._listBox1.FormattingEnabled = True
					self._listBox1.ItemHeight = 33
					self._listBox1.Location = System.Drawing.Point(-3, 94)
					self._listBox1.Name = "listBox1"
					self._listBox1.Size = System.Drawing.Size(474, 433)
					self._listBox1.TabIndex = 3
					# 
					# textBox1
					# 
					self._textBox1.BackColor = System.Drawing.SystemColors.HotTrack
					self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 36, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._textBox1.ForeColor = System.Drawing.Color.Black
					self._textBox1.Location = System.Drawing.Point(367, 12)
					self._textBox1.Name = "textBox1"
					self._textBox1.Size = System.Drawing.Size(351, 62)
					self._textBox1.TabIndex = 4
					self._textBox1.TextChanged += self.TextBox1TextChanged
					# 
					# label1
					# 
					self._label1.BackColor = System.Drawing.Color.Transparent
					self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._label1.ForeColor = System.Drawing.Color.DarkViolet
					self._label1.Location = System.Drawing.Point(99, 9)
					self._label1.Name = "label1"
					self._label1.Size = System.Drawing.Size(262, 59)
					self._label1.TabIndex = 5
					self._label1.Text = "Enter Num:"
					self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
					# 
					# MainForm
					# 
					self.BackColor = System.Drawing.Color.SlateGray
					self.ClientSize = System.Drawing.Size(730, 567)
					self.Controls.Add(self._label1)
					self.Controls.Add(self._textBox1)
					self.Controls.Add(self._listBox1)
					self.Controls.Add(self._button3)
					self.Controls.Add(self._button2)
					self.Controls.Add(self._button1)
					self.Name = "MainForm"
					self.Text = "Prog152b"
					self.Load += self.MainFormLoad
					self.ResumeLayout(False)
					self.PerformLayout()


    def Button1Click(self, sender, e):
        Heading = "Num \t\t Sum"
        self._listBox1.Items.Add(Heading)
        Num1 = self._textBox1.Text
        Num1 = int(Num1)
        l = 0
        for num in range(2, Num1+2, 2):
            if l <= Num1:
                
                l = num + l
                
                Final = str(num) + " \t\t" + str(l)
                self._listBox1.Items.Add(Final)


    def Button2Click(self, sender, e):
        self._listBox1.Clear()
        self._textBox1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()    

	def TextBox1TextChanged(self, sender, e):
		pass

	def MainFormLoad(self, sender, e):
		pass