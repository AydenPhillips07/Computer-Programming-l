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
					self.SuspendLayout()
					# 
					# button1
					# 
					self._button1.BackColor = System.Drawing.Color.SeaShell
					self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._button1.ForeColor = System.Drawing.Color.Red
					self._button1.Location = System.Drawing.Point(12, 435)
					self._button1.Name = "button1"
					self._button1.Size = System.Drawing.Size(214, 147)
					self._button1.TabIndex = 1
					self._button1.Text = "Calculate"
					self._button1.UseVisualStyleBackColor = False
					self._button1.Click += self.Button1Click
					# 
					# button2
					# 
					self._button2.BackColor = System.Drawing.Color.SeaShell
					self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._button2.ForeColor = System.Drawing.Color.Red
					self._button2.Location = System.Drawing.Point(704, 435)
					self._button2.Name = "button2"
					self._button2.Size = System.Drawing.Size(214, 147)
					self._button2.TabIndex = 2
					self._button2.Text = "Exit"
					self._button2.UseVisualStyleBackColor = False
					self._button2.Click += self.Button2Click
					# 
					# button3
					# 
					self._button3.BackColor = System.Drawing.Color.SeaShell
					self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._button3.ForeColor = System.Drawing.Color.Red
					self._button3.Location = System.Drawing.Point(355, 435)
					self._button3.Name = "button3"
					self._button3.Size = System.Drawing.Size(214, 147)
					self._button3.TabIndex = 3
					self._button3.Text = "Clear"
					self._button3.UseVisualStyleBackColor = False
					self._button3.Click += self.Button3Click
					# 
					# listBox1
					# 
					self._listBox1.BackColor = System.Drawing.Color.DeepSkyBlue
					self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._listBox1.ForeColor = System.Drawing.Color.Red
					self._listBox1.FormattingEnabled = True
					self._listBox1.ItemHeight = 25
					self._listBox1.Location = System.Drawing.Point(12, 12)
					self._listBox1.Name = "listBox1"
					self._listBox1.Size = System.Drawing.Size(906, 404)
					self._listBox1.TabIndex = 4
					# 
					# MainForm
					# 
					self.BackColor = System.Drawing.Color.Maroon
					self.ClientSize = System.Drawing.Size(948, 594)
					self.Controls.Add(self._listBox1)
					self.Controls.Add(self._button3)
					self.Controls.Add(self._button2)
					self.Controls.Add(self._button1)
					self.Name = "MainForm"
					self.Text = "prog122b"
					self.ResumeLayout(False)


    def TextBox1TextChanged(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        heading = "Hours\t\tPay\t"
        self._listBox1.Items.Add(heading)
        for num in range(1, 40+1):
            pay1 = num * 4
            msg = str(num) + "\t\t" + str(pay1)
            self._listBox1.Items.Add(msg)

    def Button3Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button2Click(self, sender, e):
        Application.Exit()   