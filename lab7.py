# Zachariah Derrick zcd22@nau.edu
# Adam Montano ajm2327@nau.edu

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
		
def get_contact_string(contacts, first_name, last_name):
	return contacts[f'{first_name}{last_name}']
	
def remove_contact(contacts, first_name, last_name):
	return contacts.pop(f'{first_name}{last_name}')
	
def update_contact_first_name(contacts, first_name, last_name, new_value):
	contacts[f'{first_name}{last_name}']['first_name'] = new_value
	contacts[f'{new_value}{last_name}'] = contacts.pop(f'{first_name}{last_name}')
	return contacts
	
def update_contact_last_name(contacts, first_name, last_name, new_value):
	contacts[f'{first_name}{last_name}']['last_name'] = new_value
	contacts[f'{first_name}{new_value}'] = contacts.pop(f'{first_name}{last_name}')
	return contacts
	
def update_contact_email(contacts, first_name, last_name, new_value):
	contacts[f'{first_name}{last_name}']['email'] = new_value
	return contacts
	
def update_contact_phone_number(contacts, first_name, last_name, new_value):
	contacts[f'{first_name}{last_name}']['phone_number'] = new_value
	return contacts
	
def update_contact_birthday(contacts, first_name, last_name, new_value):
	contacts[f'{first_name}{last_name}']['birthday'] = new_value
	return contacts
