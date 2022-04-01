class AlarmClock:
    def __init__(self) -> None:
        self.current_time = "11:57 am"
        self.alarm_is_on = False
        self.alarm_time = ""
    def set_time(self, time):
        self.current_time = time
        print (f"Current time set to {self.current_time} ")
    def display_time(self):
        print(f"The current time is {self.current_time} ")
    def toggle_alarm(self):
        if self.alarm_is_on == False:
            self.alarm_is_on = True
            print("The alarm has been turned on.")
        else:
            self.alarm_is_on = False
            print("The alarm has been turned off")
    def set_alarm(self, time):
        self.alarm_time = time
        print (self.alarm_time)
    def display_alarm_time(self):
        print (self.alarm_time)