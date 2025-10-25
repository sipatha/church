import os
import json

import frappe

initial_data_list = [
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

def import_initial_data():

	for initial_data in initial_data_list:

		with open(os.path.join(os.path.dirname(__file__), "data", initial_data), 'r') as initial_data_file:
			data = json.load(initial_data_file)

			for _, record in enumerate(data, start = 1):
				doc = frappe.get_doc(**record)

				doc.insert()

			frappe.db.commit()
