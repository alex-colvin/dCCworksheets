hercules_attacks = ["THUNDER STOMP", "POWER PUNCH", "HERCULEAN HEADBUTT"]
self = {"Health": 100, "Attack Power": 10, "Attacks": hercules_attacks}

print(self["Attacks"][1])

user_input=100
max_attacks = (len(self["Attacks"]) - 1)
while user_input > max_attacks:
    n = 0
    for attack in self["Attacks"]:
        print(f"{n} : {attack}")
        n += 1
    user_input = abs(int(input("Choose an attack by its number :")))
print(self["Attacks"][user_input])