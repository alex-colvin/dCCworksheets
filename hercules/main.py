from character import Character
narrator = Character("narrator", 100, 0, False, 100)
print("You are Hercules, the greatest of the Greek Heroes! You have just completed your quest to Hades to retrieve the elusive Emerald of Enchantment, stolen by the two-headed slimy slithering serpent Segra. After weeks in sweltering sulfur filled caverns, you return home only to find out that you have been tasked by King Eurystheus to slay the vicious Nemean Lion, defeat the impossible nine-headed Lernaean Hydra, and capture the guard dog of the underworld—Cerberus. While you were away, these three villains laid seige to the city, kidnapped the fair maiden Heleneus, and stole the orb of tranquility from the Kings underground vault.")
hercules_attacks = ["THUNDER STOMP", "POWER PUNCH", "HERCULEAN HEADBUTT"]
nemean_attacks = ["SCRATCH", "BITE", "ROAR"]
hydra_attacks = ["WATER JET", "TAIL WHIP", "NINE HEADED BITE"]
# maybe add function to block or telegraph moves...nine headed bite could strike as  nine 5 pts attacks
cerberus_attacks = ["TRIPLE BITE", "SCRATCH", "HOWL FROM HADES"]
hercules = Character("Hercules", 10, hercules_attacks, 'defeated', False)
nemean_lion = Character("Nemean Lion", 10, nemean_attacks, 'slayed', True, 30)
lernaean_hydra = ("Lernaean Hydra", 20, hydra_attacks, 'defeated, True', 50)
hercules.choose_attack_methods()
hercules.attack(nemean_lion)
nemean_lion.attack(hercules)
print(hercules.stats["Health"])





# Features:
# As a developer, I want to make at least five commits on GitHub with descriptive 
# messages.
# As a user, I want an engaging story to be told using print() statements.
# As a user, I want Hercules (and each enemy), to have health, attack power, and a
# List of attack names saved in a Dictionary.
# As a user, I want the ability to select Hercules’ attack using a menu prompt.
# As a user, I want the foe’s attack to be chosen at random.

# As a user, I want the results of each attack to be logged in the terminal.
# As a developer, I want to use an Attack() function that will terminate when 
# Hercules or an enemy’s health reaches zero.
# As a developer, I want my RunGame() function to call my other functions in a 
# logical order that will determine game flow.
# As a developer, I want all of my functions to have a Single 
# Responsibility. Remember, each function should do just one thing

# Classes
    # Character 
        #instance variables
            # health
            # attack power
            # list of attack names in a dictionary "attack name" : "damage points"
            # slay, defeat, and capture are different win verbs so 'defeated quote' or something like that
            # is_enemy
        #methods
            # update_health
            # attack 
            # choose_attack_methods
            # display_defeat
    # Attacks
        #instance variables
            # name
            # damage
            # maybe be place the attack dicitonary here
        # methods
            # damage_opponent 