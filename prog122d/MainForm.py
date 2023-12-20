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
					self._button1.BackColor = System.Drawing.Color.DeepSkyBlue
					self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._button1.ForeColor = System.Drawing.Color.Crimson
					self._button1.Location = System.Drawing.Point(26, 433)
					self._button1.Name = "button1"
					self._button1.Size = System.Drawing.Size(200, 152)
					self._button1.TabIndex = 0
					self._button1.Text = "Calculate"
					self._button1.UseVisualStyleBackColor = False
					self._button1.Click += self.Button1Click
					# 
					# button2
					# 
					self._button2.BackColor = System.Drawing.Color.DeepSkyBlue
					self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._button2.ForeColor = System.Drawing.Color.Crimson
					self._button2.Location = System.Drawing.Point(396, 433)
					self._button2.Name = "button2"
					self._button2.Size = System.Drawing.Size(200, 152)
					self._button2.TabIndex = 1
					self._button2.Text = "Clear"
					self._button2.UseVisualStyleBackColor = False
					self._button2.Click += self.Button2Click
					# 
					# button3
					# 
					self._button3.BackColor = System.Drawing.Color.DeepSkyBlue
					self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._button3.ForeColor = System.Drawing.Color.Crimson
					self._button3.Location = System.Drawing.Point(744, 433)
					self._button3.Name = "button3"
					self._button3.Size = System.Drawing.Size(200, 152)
					self._button3.TabIndex = 2
					self._button3.Text = "Exit"
					self._button3.UseVisualStyleBackColor = False
					self._button3.Click += self.Button3Click
					# 
					# listBox1
					# 
					self._listBox1.BackColor = System.Drawing.Color.Red
					self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._listBox1.FormattingEnabled = True
					self._listBox1.ItemHeight = 25
					self._listBox1.Location = System.Drawing.Point(26, 13)
					self._listBox1.Name = "listBox1"
					self._listBox1.Size = System.Drawing.Size(918, 404)
					self._listBox1.TabIndex = 3
					# 
					# MainForm
					# 
					self.BackColor = System.Drawing.Color.DeepSkyBlue
					self.ClientSize = System.Drawing.Size(956, 597)
					self.Controls.Add(self._listBox1)
					self.Controls.Add(self._button3)
					self.Controls.Add(self._button2)
					self.Controls.Add(self._button1)
					self.Name = "MainForm"
					self.Text = "prog122c"
					self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        heading = "X\t\tY"
        self._listBox1.Items.Add(heading)
        for x in range(-12, 16+1):
            Y = x**6 - 3 * x**5 - 93 * x**4 + 87 * x**3 + 1596 * x**2 - 1389 * x - 2800
            msg = str(x) + "\t\t" + str(Y)
            self._listBox1.Items.Add(msg)

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()   