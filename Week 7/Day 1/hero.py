# Define the Hero class
class Hero:
    # Initialize our class and automatically create i think its called a instance
    def __init__(self, superhero_name, secret_identity, superpower, arch_enemy):
        self.superhero_name = superhero_name
        self.secret_identity = secret_identity
        self.superpower = superpower
        self.arch_enemy = arch_enemy
        self.lair = None

    # Function to list information on the super hero
    def describe_min(self):
        return (f"Superhero : {self.superhero_name}\n"
                f"Identity : {self.secret_identity}\n"
                f"Superpower : {self.superpower}\n"
                f"Arch Enemy : {self.arch_enemy}\n"
                f"Lair :  {self.lair}")

    # Function to lets say introduce the hero based on the information
    def describe_detail(self):
        return (f"As {self.superhero_name}, they wield the extraordinary power of {self.superpower}.\n"
                f"However, behind the mask lies {self.secret_identity}, living with the burden of this dual identity.\n"
                f"As if this wasn't enough, they face an unending struggle against their greatest foe, {self.arch_enemy}.")
    
    # Function to transform the a hero
    def transform(self):
        print(f"{self.secret_identity} has transformed into {self.superhero_name}!")

    # Function to the hero's lair
    def set_lair(self, lair):
        self.lair = lair

    # Function to get the heros lair
    def get_lair(self):
        return self.lair

    # Function to shed some light on the lair
    def describe_lair(self):
        if self.lair:
            return f"{self.superhero_name}'s secret lair is located at {self.lair}."
        else:
            return f"{self.superhero_name} does not have a secret lair."