from models.user import User


u = User(email='omar@email', username='atcocoder', phone_number='3588208', whatsapp='3588208', password_hash='secret')

print(u.to_dict())
