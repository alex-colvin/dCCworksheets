from cellphone import Cell_Phone
my_phone = Cell_Phone("Samsung Galaxy Note 20 Ultra")
# 1. Print the cell phone’s contacts to the terminal
print(my_phone.contacts)
# 2. Send two new messages to the phone through the receive text message method
my_phone.receive_text_message("john", "what's for dinner")
my_phone.receive_text_message("jill", "want to hang out later?")
# 3. Print the cell phone’s messages to the terminal
print(my_phone.messages)
# 4. Call the create text message method to create a new message
my_phone.create_text_message("john", "pizza")
# 5. Toggle the cell phones ringer to vibrate
my_phone.toggle_vibrate_settting()
my_phone.toggle_vibrate_settting()
# 6. Print the cell phone’s current ringer/vibrate setting to the terminal 
print(my_phone.on_vibrate)