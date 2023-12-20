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
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@textBox2 = System::Windows::Forms::TextBox.new()
		@textBox3 = System::Windows::Forms::TextBox.new()
		@textBox4 = System::Windows::Forms::TextBox.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 9.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(99, 262)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(103, 56)
		@button1.TabIndex = 0
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = true
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 9.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(364, 262)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(103, 56)
		@button2.TabIndex = 1
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = true
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 9.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.Location = System::Drawing::Point.new(641, 262)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(103, 56)
		@button3.TabIndex = 2
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = true
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::SystemColors.Control
		@label1.BorderStyle = System::Windows::Forms::BorderStyle.Fixed3D
		@label1.Location = System::Drawing::Point.new(12, 9)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(137, 66)
		@label1.TabIndex = 3
		@label1.Text = "Enter 4 Numbers"
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::SystemColors.Control
		@label2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label2.Location = System::Drawing::Point.new(168, 113)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(501, 42)
		@label2.TabIndex = 4
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::SystemColors.Control
		@label3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.Location = System::Drawing::Point.new(168, 172)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(501, 42)
		@label3.TabIndex = 5
		# 
		# textBox1
		# 
		@textBox1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 18, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox1.Location = System::Drawing::Point.new(185, 12)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(126, 35)
		@textBox1.TabIndex = 6
		# 
		# textBox2
		# 
		@textBox2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 18, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox2.Location = System::Drawing::Point.new(342, 12)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(125, 35)
		@textBox2.TabIndex = 7
		# 
		# textBox3
		# 
		@textBox3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 18, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox3.Location = System::Drawing::Point.new(185, 55)
		@textBox3.Name = "textBox3"
		@textBox3.Size = System::Drawing::Size.new(126, 35)
		@textBox3.TabIndex = 8
		# 
		# textBox4
		# 
		@textBox4.Font = System::Drawing::Font.new("Microsoft Sans Serif", 18, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox4.Location = System::Drawing::Point.new(342, 55)
		@textBox4.Name = "textBox4"
		@textBox4.Size = System::Drawing::Size.new(125, 35)
		@textBox4.TabIndex = 9
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.Highlight
		self.ClientSize = System::Drawing::Size.new(831, 330)
		self.Controls.Add(@textBox4)
		self.Controls.Add(@textBox3)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "prog54b"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Button1Click(sender, e)
		Num1 = int(@textBox1.Text)
		Num2 = int(@textBox2.Text)
		Num3 = int(@textBox3.Text)
		Num4 = int(@textBox4.Text)
		
		Sum = Num1 + Num2 + Num3 + Num4
		@label2.Text = "The sum of the four numbers is: " + str(Sum)
		
		Average = Sum / 4.0
		@label3.Text = "The average of the four numbers is: " + str(Average)
	end

	def Button3Click(sender, e)
		Application.Exit()
	end

	def Button2Click(sender, e)
		@textBox1.Text = ""
		@textBox2.Text = ""
		@textBox3.Text = ""
		@textBox4.Text = ""
		@label2.Text = ""
		@label3.Text = ""
	end
end

