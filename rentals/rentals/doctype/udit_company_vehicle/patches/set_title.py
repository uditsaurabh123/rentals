import frappe
def execute():
    vehicles = frappe.db.get_all("Udit_Company_Vehicle",fields=["name"])
    for v in vehicles:
        vehicle = frappe.get_doc("Udit_Company_Vehicle",v)
        vehicle.set_title()
        vehicle.save()
    frappe.db.commit()   

