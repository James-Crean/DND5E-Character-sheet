import os
import random


class Character():

    _alignments = {
        "LG": "Lawful Good",
        "NG": "Neutral Good",
        "CG": "Chaotic Good",
        "LN": "Lawful Neutral",
        "NN": "True Neutral",
        "CN": "Chaotic Neutral",
        "LE": "Lawful Evil",
        "NE": "Neutral Evil",
        "CE": "Chaotic Evil"
    }
    _classes = [
        "Barbarian",
        "Bard",
        "Cleric",
        "Druid",
        "Fighter",
        "Monk",
        "Paladin",
        "Ranger",
        "Rogue",
        "Sorcerer",
        "Warlock",
        "Wizard."
    ]
    _hit_dice = {
        'Sorcerer': 6,
        'Wizard': 6,
        "Bard": 8,
        "Cleric": 8,
        "Druid": 8,
        "Monk": 8,
        "Rogue": 8,
        "Warlock": 8,
        "Fighter": 10,
        "Paladin": 10,
        "Ranger": 10,
        "Barbarian": 12
    }
    _races = [
        'Dragonborn',
        'Dwarf',
        'Elf',
        'Gnome',
        'Half Elf',
        'Half Orc',
        'Halfling',
        'Human',
        'Tiefling'
    ]
    _racial_move_speed = {
        "Dragonborn": 30,
        "Gnome": 25,
        "Half Elf": 30,
        "Half Orc": 30,
        "Tiefling": 30,
        "Human": 30,
        "Halfling": 25,
        "Elf": 30,
        "Dwarf": 25
    }
    _proficiency = [None, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6] # by level. No level 0, so 0 index is None

    def __init__(self, char_name=None, char_age=None, char_race=None, char_class=None,
                 char_stats=None, char_alignment=None, char_level=None):
        assert char_name, "char_name is a required argument"
        assert char_age, "char_age is a required argument"
        assert char_race, "char_race is a required argument"
        assert char_class, "char_class is a required argument"
        assert char_stats, "char_stats is a required argument"
        assert char_alignment, "char_alignment is a required argument"
        assert char_level, "char_level is a required argument"

        self.char_name = char_name
        self.char_age = char_age
        self.char_race = char_race
        self.char_class = char_class
        self.char_stats = char_stats
        self.char_alignment = char_alignment
        self.char_level = char_level
        self.move_speed = self._racial_move_speed[char_race]
        self.hit_dice = self._hit_dice[char_class]
        self.prof_bonus = self._proficiency[char_level]

    @staticmethod
    def gather_info():
        info = {
            'char_name': None,
            'char_age': None,
            'char_race': None,
            'char_class': None,
            'char_stats': None,
            'char_alignment': None,
            'char_level': None
        }
        gather_info = True
        while(gather_info):
            info['char_name'] = _get_name()
            info['char_class'] = _get_class()
            info['char_race'] = _get_race()
            info['char_age'] = _get_age()
            keep_info = input(
                 f"Ok, so your character is {info['char_name']} who is a {info['char_age']} year old {info['char_race']} and they are a {info['char_class']}.\n"
                 f"Great choices so far! Does everything look correct to you?").capitalize()
            if keep_info.lower() in ["yes", "y"]:
                gather_info = False
        info['char_stats'] = _generate_stats()
        info['char_alignment'] = _get_alignment()
        info['char_level'] = _get_level()
        return info

    @property
    def max_hit_points(self):
        return int((self.hit_dice + self.con_save) * self.char_level)

    @property
    def str_save(self):
        return int((self.char_stats['str'] - 10) // 2)

    @property
    def dex_save(self):
        return int((self.char_stats['dex'] - 10) // 2)

    @property
    def con_save(self):
        return int((self.char_stats['con'] - 10) // 2)

    @property
    def int_save(self):
        return int((self.char_stats['int'] - 10) // 2)

    @property
    def wis_save(self):
        return int((self.char_stats['wis'] - 10) // 2)

    @property
    def cha_save(self):
        return int((self.char_stats['cha'] - 10) // 2)


    def print_sheet(self):
        with open('character.txt', 'w') as sheet:
            sheet.write(f"Character name: {self.char_name}\n")
            sheet.write(f"Race: {self.char_race}\n")
            sheet.write(f"Class: {self.char_class}\n")
            sheet.write(f"Level {self.char_level}\n")
            sheet.write(f"Age: {self.char_age}\n")
            sheet.write(f"Move speed: {self.move_speed}\n")
            sheet.write(f"Alignment: {self.char_alignment}\n")
            sheet.write(f"Hit Points: {self.max_hit_points}\n")
            sheet.write(f"Your hit dice is {self.hit_dice}\n")
            sheet.write(f"Strength = {self.char_stats['str']}\n")
            sheet.write(f"Dexterity = {self.char_stats['dex']}\n")
            sheet.write(f"Constitution = {self.char_stats['con']}\n")
            sheet.write(f"Intelligence = {self.char_stats['int']}\n")
            sheet.write(f"Wisdom = {self.char_stats['wis']}\n")
            sheet.write(f"Charisma = {self.char_stats['cha']}\n")
            sheet.write(f"Proficiency bonus = {self.prof_bonus}\n")
            sheet.write(f"Strength saving throw = {self.str_save}\n")
            sheet.write(f"Dexterity saving throw = {self.dex_save}\n")
            sheet.write(f"Constitution saving throw = {self.con_save}\n")
            sheet.write(f"Intelligence saving throw = {self.int_save}\n")
            sheet.write(f"Wisdom saving throw = {self.wis_save}\n")
            sheet.write(f"Charisma saving throw = {self.cha_save}\n")
    



def _get_name():
    name = input(
        "Hello there! My name is Otto and I am very clever.\n"
        "I'm here to help you make a Dungeons & Dragons character!\n"
        "Do not worry, I will walk you through step by step and do as much as I possibly can to ottomate the process.\n"
        "Let's start off easy, what is your characters name going to be?\n")
    clear()
    return name

def _get_age():
    age = input("How old is your character going to be?\n")
    clear()
    return age


def _get_race():
    print(
        "What kind of fantasy race are you interested in playing?\n"
        "This will affect your stats in a small way, but also can change how your character may perceive the world,\n"
        "and how the world may view them, it can also grant you cool abilities.\n"
        "But we will touch on that later, for now I can assist with the following:\n"
        f"{Character._races}\n")

    race_explain = input("Would you like Otto to quickly describe each fantasy race?\n")
    if race_explain.lower() in ["yes", "y"]:
        print(
            "Dragonborn are a bipedal race of half dragon half people, it may be easiest to think of them as 'lizard people'.\n"
            "Gnomes are short in height but big in spirit, they are often tied to nature and the fey and frequently dabble in mysticism.\n"
            "Half Elfs are children of humanity and elf-kind, not as tall as elves but taller than most humans,\n"
            "typically slender & pointed ears though not as large as a full blooded elf, similar to the character 'Link' from the video game\n"
            "series 'The Legend of Zelda'.\n"  "Half Orcs are half orc and half human and are typically stronger than a human and smarter than an orc,\n"
            "while maintaining green or grey skin from their orc heritage, it may be best to think of an orc from\n"
            "'The Lord of the Rings' series but with more brains and fairer skin.\n"
            "Tieflings are typically a blue or purple hue skinned bipedial horned creature that otherwise maintains the shape of a human,\n"
            "Otto supposes they could be likened to a demon though this is technically not true and they would not appreciate such a comparison.\n"
            "Humans are just like you, Otto hopes a further explaination is not needed.\n"  "Halflings are very similar to hobbits from the\n"
            "'lord of the rings' series.  Elves are a tall, long eared slender race similar to Legolas from 'The Lord of the Rings'.\n"
            "Dwarves are typically short and hardy, they are also similar to Gimli from 'The Lord of the Rings'.\n")
    else:
        print("Ok")

    valid_race = False
    while(not valid_race):
        # find a way to incorporate their stat alterations into player stats
        char_race = input("Please select your race: ").capitalize()
        if char_race in Character._races:
            valid_race = True
        else:
            print(f"{char_race} is not a valid race. Let's try again.\n")
    clear()
    return char_race


def _get_alignment():
    explain_alignment = input("Next we will need to pick your alignment, would you like an explanation on alignments?:\n")
    if explain_alignment.lower() in ["yes", "y"]:
        print("Lawful good is like a policeman, or for a high fantasy example, a paladin.")
        print("Neutral good is like a good citizen, they may not have a strong set of principles but they still do the right thing.")
        print("Chaotic good is a Robin Hood or Batman type character, if you can do good by breaking the law then you likely would do so.")
        print("Lawful neutral is like a lawyer, you work within the scope of laws and rules but likely to your own benefit")
        print("Neutral/Neutral, often referred to as 'True Neutral', is traditionally a self centered character.")
        print("Chaotic neutral is the type of character who just likes to cause commotion and chaos to see what happens, like a small mischievous child would.")
        print("Lawful evil is best thought of as the 'devil', operates within a set of rules in order to inflict suffering on people.")
        print("Neutral evil can be thought of as a bad sociopath, a type of entity who simply goes through life with no regard for anything but causing pain.")
        print("Chaotic evil can present as brigands or a 'Black hat' in the wild west days, they operate outside any laws in order to make the world a worse place.")
    else:
        print("Ok.")
    character_alignment = None
    while(not character_alignment):
        user_alignment = input(
            "Please enter your chosen alignment by typing the initials of the alignment you'd like, for example; Neutal/Neutral would be entered as NN:\n").upper()
        if user_alignment not in Character._alignments.keys():
            print("Please only choose two letters for your chosen alignment.")
        character_alignment = user_alignment
    return character_alignment


def _generate_stats():
    print(
        "Next up is stat rolls.\n"
        "There are several different ways of doing this, but for simplicity sake, Otto will handle the rolling for you.\n"
        "Do not worry, I am created to not give you any rolls that are too bad,\n"
        "though you will likely have at least one or two below 10, this is not only normal, it's part of the fun.\n"
        "Nobody's perfect, except for Otto of course.")
    stats = {
        'str': random.randint(7, 18),
        'dex': random.randint(7, 18),
        'con': random.randint(7, 18),
        'int': random.randint(7, 18),
        'wis': random.randint(7, 18),
        'cha': random.randint(7, 18)
    }

    print(
        f"{stats['str']} is your strength score.\n"
        "This is how physically strong you are, and typically how much damage you will deal with a melee attack.\n")

    print(
        f"{stats['dex']} is your dexterity score.\n"
        "This is how nimble you are and can help you avoid traps, or shoot a bow.\n")

    print(
        f"{stats['con']} is your constitution score.\n"
        "This dictates how physically resiliant you are.\n")

    print(
        f"{stats['int']} is your intelligence score.\n"
        "This represents how studied you are. For example, Otto has a 30 in intelligence,\n" 
        "however a normal PC will never reach that high, as I am a highly advanced A.I.\n")

    print(
        f"{stats['wis']} is your wisdom score.\n"
        "If intelligence is book smarts, wisdom is street smarts.\n"
        "Think of it like this, intelligence is knowing a knife is sharp, wisdom is knowing the sharp side points away from you.\n")

    print(
        f"{stats['cha']} is your charisma score.\n"
        "Typically it's how likeable you are perceived to be.\n")
    return stats

def _get_class():
    valid_class = False
    while(not valid_class):
        char_class = input(
        "What class do you want to play?\n"
        "This will dictate what your character can do in combat, how they interact with the monsters, and other various things.\n"
        "I can assist with the following classes:\n"
        f"{Character._classes}\n").capitalize()
        if char_class not in Character._classes:
            print("Please choose a valid class.")
        else:
            valid_class = True
    clear()
    return char_class

def _get_level():
    return int(input("What level is your campaign starting at? If unsure Otto suggests picking 1 for your level.\n"))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    # execute only if run as a script
    character_info = Character.gather_info()
    character = Character(**character_info)
    character.print_sheet()
