require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		@label5 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.ForeColor = System::Drawing::SystemColors.MenuHighlight
		@button1.Location = System::Drawing::Point.new(181, 251)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(96, 43)
		@button1.TabIndex = 0
		@button1.Text = "Show"
		@button1.UseVisualStyleBackColor = true
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.ForeColor = System::Drawing::SystemColors.MenuHighlight
		@button2.Location = System::Drawing::Point.new(444, 251)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(96, 43)
		@button2.TabIndex = 1
		@button2.Text = "Hide"
		@button2.UseVisualStyleBackColor = true
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::SystemColors.Control
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(77, 26)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(142, 44)
		@label1.TabIndex = 2
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::SystemColors.Control
		@label2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label2.Location = System::Drawing::Point.new(327, 26)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(142, 44)
		@label2.TabIndex = 3
		@label2.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::SystemColors.Control
		@label3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.Location = System::Drawing::Point.new(573, 26)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(142, 44)
		@label3.TabIndex = 4
		@label3.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		@label4.BackColor = System::Drawing::SystemColors.Control
		@label4.Font = System::Drawing::Font.new("Microsoft Sans Serif", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label4.Location = System::Drawing::Point.new(207, 132)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(142, 44)
		@label4.TabIndex = 5
		@label4.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		@label5.BackColor = System::Drawing::SystemColors.Control
		@label5.Font = System::Drawing::Font.new("Microsoft Sans Serif", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label5.Location = System::Drawing::Point.new(456, 132)
		@label5.Name = "label5"
		@label5.Size = System::Drawing::Size.new(142, 44)
		@label5.TabIndex = 6
		@label5.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.ActiveCaption
		self.ClientSize = System::Drawing::Size.new(833, 306)
		self.Controls.Add(@label5)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "PhoneNumbers"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "Culver's 608-554-3712"
		@label2.Text = "Xbox 800-469-9269"
		@label3.Text = "Insomniac Games 818-729-2400"
		@label4.Text = "McDonalds 608-752-7521"
		@label5.Text = "Dixie's Crossroads 321-268-5000"
	end

	def Button2Click(sender, e)
		@label1.Text = ""
		@label2.Text = ""
		@label3.Text = ""
		@label4.Text = ""
		@label5.Text = ""
	end
end

