# from person import Person

# q = Person("Q", "21", "Unmeasured")

# print(f"Thanks for registering the user '{q.name}'")
# print(f"""
# Inputted Data For '{q.name}'
# --------------------------
# - {q.name}
# - {q.age}
# - {q.height}
# """)


# Import hero class 
from hero import Hero

# Lets create four heros via the Hero class
# superhero_name, secret_identity, superpower. arch_enemy
hero_spiderman = Hero(
    superhero_name="Spider-Man",
    secret_identity="Peter Parker",
    superpower="superhuman agility, strength, and the ability to cling to walls; Spider-Sense",
    arch_enemy="Green Goblin"
)

hero_ironman = Hero(
    superhero_name="Iron Man",
    secret_identity="Tony Stark",
    superpower="genius-level intellect, powered armor suit with advanced weaponry",
    arch_enemy="Mandarin"
)

hero_cpt = Hero(
    superhero_name="Captain America",
    secret_identity="Steve Rogers",
    superpower="enhanced strength, agility, and durability from the Super Soldier Serum",
    arch_enemy="Red Skull"
)

hero_thor = Hero(
    superhero_name="Thor",
    secret_identity="Thor Odinson",
    superpower="godlike strength, control over lightning, and wielding the enchanted hammer Mjolnir",
    arch_enemy="Loki"
)

# Descriptions
print(f"""
Detailed Description\n
------------------------\n
      
{hero_spiderman.describe_detail()}\n
{hero_ironman.describe_detail()}\n 
{hero_cpt.describe_detail()}\n
{hero_thor.describe_detail()}\n 
""")

print(f"""
Minimal Description\n
------------------------\n
      
{hero_spiderman.describe_min()}\n
{hero_ironman.describe_min()}\n 
{hero_cpt.describe_min()}\n
{hero_thor.describe_min()}\n 
""")


hero_spiderman.set_lair("The Spider's Den in Queens")
hero_ironman.set_lair("Stark Tower in New York City")
hero_cpt.set_lair("The Avengers Compound in New York City")
hero_thor.set_lair("Asgard")

print(f"""
Minimal Description\n
------------------------\n
      
{hero_spiderman.describe_min()}\n
{hero_ironman.describe_min()}\n 
{hero_cpt.describe_min()}\n
{hero_thor.describe_min()}\n 
""")

print(f"{hero_spiderman.describe_lair()}")
print(f"{hero_ironman.describe_lair()}")
print(f"{hero_cpt.describe_lair()}")
print(f"{hero_thor.describe_lair()}")