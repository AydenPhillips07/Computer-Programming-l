require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@label1 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		@label5 = System::Windows::Forms::Label.new()
		@label6 = System::Windows::Forms::Label.new()
		@label7 = System::Windows::Forms::Label.new()
		@label8 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::SystemColors.MenuHighlight
		@label1.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@label1.Location = System::Drawing::Point.new(88, 45)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(105, 42)
		@label1.TabIndex = 0
		@label1.Click { |sender, e| self.Label1Click(sender, e) }
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::SystemColors.MenuHighlight
		@label2.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@label2.Location = System::Drawing::Point.new(88, 107)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(105, 42)
		@label2.TabIndex = 1
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::SystemColors.MenuHighlight
		@label3.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@label3.Location = System::Drawing::Point.new(88, 166)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(105, 42)
		@label3.TabIndex = 2
		# 
		# label4
		# 
		@label4.BackColor = System::Drawing::SystemColors.MenuHighlight
		@label4.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@label4.Location = System::Drawing::Point.new(88, 230)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(105, 42)
		@label4.TabIndex = 3
		# 
		# label5
		# 
		@label5.BackColor = System::Drawing::SystemColors.MenuHighlight
		@label5.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@label5.Location = System::Drawing::Point.new(199, 45)
		@label5.Name = "label5"
		@label5.Size = System::Drawing::Size.new(105, 42)
		@label5.TabIndex = 4
		# 
		# label6
		# 
		@label6.BackColor = System::Drawing::SystemColors.MenuHighlight
		@label6.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@label6.Location = System::Drawing::Point.new(199, 107)
		@label6.Name = "label6"
		@label6.Size = System::Drawing::Size.new(105, 42)
		@label6.TabIndex = 5
		# 
		# label7
		# 
		@label7.BackColor = System::Drawing::SystemColors.MenuHighlight
		@label7.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@label7.Location = System::Drawing::Point.new(199, 166)
		@label7.Name = "label7"
		@label7.Size = System::Drawing::Size.new(105, 42)
		@label7.TabIndex = 6
		# 
		# label8
		# 
		@label8.BackColor = System::Drawing::SystemColors.MenuHighlight
		@label8.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@label8.Location = System::Drawing::Point.new(199, 230)
		@label8.Name = "label8"
		@label8.Size = System::Drawing::Size.new(105, 42)
		@label8.TabIndex = 7
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::SystemColors.ActiveCaption
		@button1.Location = System::Drawing::Point.new(517, 45)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(150, 49)
		@button1.TabIndex = 8
		@button1.Text = "Show"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.Location = System::Drawing::Point.new(517, 146)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(150, 42)
		@button2.TabIndex = 9
		@button2.Text = "Hide"
		@button2.UseVisualStyleBackColor = true
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		self.ClientSize = System::Drawing::Size.new(829, 319)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label8)
		self.Controls.Add(@label7)
		self.Controls.Add(@label6)
		self.Controls.Add(@label5)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "Schedule"
		self.ResumeLayout(false)
	end

	def Button2Click(sender, e)
		@label1.Text = ""
		@label2.Text = ""
		@label3.Text = ""
		@label4.Text = ""
		@label5.Text = ""
		@label6.Text = ""
		@label7.Text = ""
		@label8.Text = ""
	end

	def Label1Click(sender, e)
		
	end

	def Button1Click(sender, e)
		@label1.Text = "1. Geometry Honors"
		@label2.Text = "2. Band"
		@label3.Text = "3. Computer Programming"
		@label4.Text = "4. English"
		@label5.Text = "5. Gym"
		@label6.Text = "6. Automotive"
		@label7.Text = "7. US History"
		@label8.Text = "8. Chemistry Honors"
	end
end

