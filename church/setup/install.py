import os
import json

import frappe

church_data_list = [
	"role.json",
	"role_profile.json",
	"church_bible_book.json",
	"church_bible_translation.json",
	"church_event_attendance_type.json",
	"church_event_type.json",
	"church_missionary_support_frequency.json",
	"church_payment_type.json",
	"church_person_relation_type.json",
	"church_member_status.json",
	"church_prayer_request_status.json",
	"church_prayer_request_type.json",
	"church_role_type.json",
	"custom_docperm.json",
	"custom_html_block.json",
	"dashboard_chart.json",
	"form_tour.json",
	"module_onboarding.json",
	"module_profile.json",
	"onboarding_step.json",
	"web_page.json",
	"website_settings.json",
	"church_fund.json"
]

def church_data():

	for church_data_file in church_data_list:

		with open(os.path.join(os.path.dirname(__file__), "data", church_data_file), 'r') as initial_data_file:
			data = json.load(initial_data_file)

			for _, record in enumerate(data, start = 1):
				doc = frappe.get_doc(**record)

				dt = record["doctype"]
				name = record["name"]

				if not name:
					doc.insert()
				else:
					try:
						doc = frappe.get_doc(dt, name)

						for key, value in record.items():
							setattr(doc, key, value)

						doc.save()
					except frappe.DoesNotExistError:
						doc.insert()

			frappe.db.commit()
