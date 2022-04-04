from random import Random
import random
class Character:
    def __init__(self, name, attack_power, attacks, defeat, is_enemy, health=100, ): 
        self.name = name
        self.stats = {"Health": health, "Attack Power": attack_power, "Attacks": attacks}
        self.attack_choice = ''
        self.defeat_ver = defeat
        self.is_enemy = is_enemy

    def choose_attack_methods(self):
        if self.is_enemy == True:
            self.attack_choice = random.choice(list(self.stats['Attacks']))
        else:
            user_input=100
            max_attacks = len(self.stats["Attacks"]) - 1
            while user_input > max_attacks:
                n = 0
                for attack in self.stats["Attacks"]:
                    print(f"{n} : {attack}")
                    n += 1
                user_input = abs(int(input("Choose an attack by its number :")))
            print("You chose " + self.stats["Attacks"][user_input] + ".")
            self.attack_choice = self.stats["Attacks"][user_input]
    def attack(self, player):
        self.choose_attack_methods()
        player.stats["Health"] -= self.stats["Attack Power"]
        print(f'{self.name} delivered {self.stats["Attack Power"]} damage to {player.name} with a {self.attack_choice}.')
        print(f"{player.name} Health : " + str(player.stats["Health"]))
        self.attack_choice = ''
    # can probably take this out
    # def receive_damage(self, enemy):
    #     self.health -= enemy.stats["Attack Power"]

    
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