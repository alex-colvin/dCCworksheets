class Cell_Phone:
    def __init__(self, model) -> None:
        self.model = model
        self.number = "910-555-5555"
        self.contacts = {"john" : "919-555-5500", "jack" : "919-555-5554", "jill" : "910-555-5553"}
        self.messages = []
        self.on_vibrate = False
    def receive_text_message (self, contact, message):
        print(f"New message from: {contact}. Message: {message}")
        self.messages.append(message) 
    def toggle_vibrate_settting (self):
        if self.on_vibrate == False:
            self.on_vibrate = True
            print("buzz")
        else:
            self.on_vibrate = False
            print("Vibrate turned off.")
    def create_text_message (self, to, message):
        print(f"To: {to}. Message: {message}")