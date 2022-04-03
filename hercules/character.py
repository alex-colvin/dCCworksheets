from attack import Attack
from random import Random
class Character:
    def __init__(self, name, attack_power, attacks, defeat, is_enemy, health=100, ): 
        self.name = name
        self.stats = {"Health": health, "Attack Power": attack_power, "Attacks": attacks}
        self.attacks = [attacks]
        self.attack = ''
        self.defeat_ver = defeat
        self.is_enemy = is_enemy

    def attack(self, enemy, attack):
        enemy.health -= self.stats["Attack Power"]
        print(f'{enemy.name} took {attack} damage from your.')

    def receive_damage(self, enemy):
        self.health -= enemy.stats["Attack Power"]

    def choose_attack_methods(self):
        if self.is_enemy == True:
            self.attack = Random.choice(self.attacks)
        else:
            user_input=100
            max_attacks = (len(self.stats["Attacks"]) - 1)
            while user_input > max_attacks:
                n = 0
                for attack in self.stats["Attacks"]:
                    print(f"{n} : {attack}")
                    n += 1
                user_input = abs(int(input("Choose an attack by its number :")))
            print(self.stats["Attacks"][user_input])
    def display_defeat (self):
        pass

    def say_something(self, message):
        print(f"{self.name}: {message}")

    def heal():
        pass
    def play_turn(self):
        pass
    def block(self):
        pass