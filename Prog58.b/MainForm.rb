require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

def int(text)     return text.to_i end
def float(text)   return text.to_f end
def str(text)     return text.to_s end
def list(obj)     return obj.to_a  end
def len(arr)      return arr.length end
def input(msg="") print msg; return gets end
def print(*args)  Kernel.print(*args, "\n") end
def round(x, y)   return float((x * 10**y).round) / 10**y end
def range(*args)  if len(args) == 1 then 
    return  list((0...args[0]).step(1)); elsif len(args) == 2 then 
    return  list((args[0]...args[1]).step(1)); elsif len(args) == 3 then 
    return  list((args[0]...args[1]).step(args[2])) end; end
class MyRandom;   def randint(min, max) return rand(max-min) + min; end; 
    def random() return rand() end; 
    def shuffle(arr) return arr.shuffle end; 
    def choice(arr) return arr[randint(0, len(arr))] end; 
end; $random = MyRandom.new(); $math = Math
MessageBox = System::Windows::Forms::MessageBox

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@textBox2 = System::Windows::Forms::TextBox.new()
		@textBox3 = System::Windows::Forms::TextBox.new()
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		@label5 = System::Windows::Forms::Label.new()
		@label6 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@button1.Location = System::Drawing::Point.new(25, 255)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(92, 46)
		@button1.TabIndex = 0
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		@button2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@button2.Location = System::Drawing::Point.new(145, 255)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(92, 46)
		@button2.TabIndex = 1
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		@button3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@button3.Location = System::Drawing::Point.new(269, 255)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(92, 46)
		@button3.TabIndex = 2
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = false
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		@label1.BorderStyle = System::Windows::Forms::BorderStyle.Fixed3D
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@label1.Location = System::Drawing::Point.new(25, 9)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(183, 68)
		@label1.TabIndex = 3
		@label1.Text = "Enter A, B, and C."
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		@textBox1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox1.Location = System::Drawing::Point.new(227, 39)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(134, 38)
		@textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		@textBox2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox2.Location = System::Drawing::Point.new(384, 39)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(134, 38)
		@textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		@textBox3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox3.Location = System::Drawing::Point.new(542, 39)
		@textBox3.Name = "textBox3"
		@textBox3.Size = System::Drawing::Size.new(134, 38)
		@textBox3.TabIndex = 6
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		@label2.BorderStyle = System::Windows::Forms::BorderStyle.Fixed3D
		@label2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label2.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@label2.Location = System::Drawing::Point.new(449, 122)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(282, 92)
		@label2.TabIndex = 7
		@label2.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		@label3.BorderStyle = System::Windows::Forms::BorderStyle.Fixed3D
		@label3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@label3.Location = System::Drawing::Point.new(94, 122)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(282, 92)
		@label3.TabIndex = 8
		@label3.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		@label4.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		@label4.BorderStyle = System::Windows::Forms::BorderStyle.Fixed3D
		@label4.Font = System::Drawing::Font.new("Microsoft Sans Serif", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label4.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@label4.Location = System::Drawing::Point.new(239, 0)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(112, 36)
		@label4.TabIndex = 9
		@label4.Text = "A"
		@label4.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		@label5.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		@label5.BorderStyle = System::Windows::Forms::BorderStyle.Fixed3D
		@label5.Font = System::Drawing::Font.new("Microsoft Sans Serif", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label5.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@label5.Location = System::Drawing::Point.new(395, 0)
		@label5.Name = "label5"
		@label5.Size = System::Drawing::Size.new(112, 36)
		@label5.TabIndex = 10
		@label5.Text = "B"
		@label5.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		@label6.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		@label6.BorderStyle = System::Windows::Forms::BorderStyle.Fixed3D
		@label6.Font = System::Drawing::Font.new("Microsoft Sans Serif", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label6.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@label6.Location = System::Drawing::Point.new(552, 0)
		@label6.Name = "label6"
		@label6.Size = System::Drawing::Size.new(112, 36)
		@label6.TabIndex = 11
		@label6.Text = "C"
		@label6.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.ControlDarkDark
		self.ClientSize = System::Drawing::Size.new(835, 313)
		self.Controls.Add(@label6)
		self.Controls.Add(@label5)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@textBox3)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@label1)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "Prog58.b"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Button1Click(sender, e)
		A = int(@textBox1.Text)
		B = int(@textBox2.Text)
		C = int(@textBox3.Text)
		posroot = (-B + $math.sqrt(B**2 - 4 * A * C)/ 2 * A)
		negroot = (-B - $math.sqrt(B**2 - 4 * A * C)/ 2 * A)
		@label2.Text = "Postive Root: " + str(posroot)
		@label3.Text = "Negative Root: " + str(negroot)
	end

	def Button2Click(sender, e)
		@label2.Text = ""
		@label3.Text = ""
		@textBox1.Text = ""
		@textBox2.Text = ""
		@textBox3.Text = ""
	end

	def Button3Click(sender, e)
		Application.Exit()
	end
end

