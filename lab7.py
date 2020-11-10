def new_contact_store():
	return {}
	
def add_new_contact(contacts, first_name, last_name, email, phone_number, birthday):
	contact_info = {
		'first_name': first_name,
		'last_name': last_name,
		'email': email,
		'phone_number': phone_number,
		'birthday': birthday
	}
	contacts[f'{first_name}{last_name}'] = contact_info
	
	return contacts
	
def has_contact(contacts, first_name, last_name):
	try:
		attempt = contacts[f'{first_name}{last_name}']
		return True
	except:
		return False
		
