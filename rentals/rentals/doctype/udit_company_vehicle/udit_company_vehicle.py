# Copyright (c) 2025, udit and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Udit_Company_Vehicle(Document):
	def before_save(self):
		self.set_title()
	
	def set_title(self):
		self.title = f"{self.make} - {self.model} - {self.year}"

	def show_first_name(self):
		print(f"{self.make} - {self.model} - {self.year}")	