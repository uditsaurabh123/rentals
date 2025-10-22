# Copyright (c) 2025, udit and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

class Udit_Company_RideBookings(Document):
    def validate(self):
        self.update_total_amount()        
     
    def update_total_amount(self): 
        total_amount=0
        for route in ( self.items or [] ):
            total_amount += route.distance_in_km * self.rate 
            self.total_amount = total_amount