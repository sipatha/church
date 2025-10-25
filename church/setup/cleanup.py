import frappe

def gender():
	existing_genders = frappe.db.get_all("Gender")

	for existing_gender in existing_genders:
		if existing_gender.name not in ["Male", "Female", "Unknown"]:
			frappe.delete_doc("Gender", existing_gender.name, force=True)

	frappe.db.commit()
