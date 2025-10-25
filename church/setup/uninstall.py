import frappe

def church_data():
	# custom docperm
	custom_docperm_to_delete = frappe.get_list(
            "Custom DocPerm",
            filters={"role": ["in", ["Church User", "Church Manager"]]},
            pluck="name"
        )

	for doc_name in custom_docperm_to_delete:
		frappe.delete_doc("Custom DocPerm", doc_name)

	# custom html block
	frappe.delete_doc("Custom HTML Block", "Church Cover Photo")

	# dashboard chart
	dashboard_charts = [
		"Church Persons Count",
		"Church Members Count (New by Month)",
		"Church Prayer Request Count (Active)",
		"Church Prayer Requests (Answered)",
		"Church Prayer Request Count (Active)",
		"Church Prayer Requests (Answered)",
		"Church Fund Balances",
		"Church Collections Sum"
	]
	for dashboard_chart in dashboard_charts:
		frappe.delete_doc("Dashboard Chart", dashboard_chart)

	# module onboarding
	frappe.delete_doc("Module Onboarding", "Church")

	# module profile
	frappe.delete_doc("Module Profile", "Church")

	# onboarding step
	onboarding_steps = [
		"Church Family",
		"Church Person",
		"Church Manager",
		"Church Event",
		"Church Prayer Request",
		"Church Information",
	]
	for onboarding_step in onboarding_steps:
		frappe.delete_doc("Onboarding Step", onboarding_step)

	# form tour (pause cleaning the form tour, json files are auto generated)
	# form_tours = ["Church Person", "Church Manager", "Church Information"]
	# for form_tour in form_tours:
	# 	frappe.delete_doc("Form Tour", form_tour)

	# role profile
	role_profiles = ["Church User", "Church Manager"]
	for role_profile in role_profiles:
		frappe.delete_doc("Role Profile", role_profile)

	# role
	roles = ["Church User", "Church Manager"]
	for role in roles:
		frappe.delete_doc("Role", role)

	# website settings
	frappe.delete_doc("Website Settings", "Website Settings")

	frappe.db.commit()
