# Copyright (c) 2025, udit and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Udit_Company_Vehicle(WebsiteGenerator):
	def before_save(self):
		self.set_title()
	
	def set_title(self):
		self.title = f"{self.make} - {self.model} - {self.year}"

	def show_first_name(self):
		print(f"{self.make} - {self.model} - {self.year}")	