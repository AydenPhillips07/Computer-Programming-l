﻿require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@label1 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::SystemColors.ActiveCaption
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(177, 44)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(413, 150)
		@label1.TabIndex = 0
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		@button1.ForeColor = System::Drawing::SystemColors.ButtonFace
		@button1.Location = System::Drawing::Point.new(221, 214)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(95, 50)
		@button1.TabIndex = 1
		@button1.Text = "Show"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		@button2.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@button2.Location = System::Drawing::Point.new(451, 214)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(100, 52)
		@button2.TabIndex = 2
		@button2.Text = "Hide"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		self.ClientSize = System::Drawing::Size.new(819, 327)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "CraigRules"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "Go Cougars"
	end

	def Button2Click(sender, e)
		@label1.Text = ""
	end
end

