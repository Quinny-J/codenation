# Store dinos in a list
dinosaurs = [
    "Triceratops",
    "Velociraptor",
    "Anklyosaurus",
    "Archaeopteryx",
    "Tyrannosaurus Rex",
    "Stegosaurus",
    "Iguanodon"
]

# Store detected saurus's 
saurus_dinosaurs = []

for dino in dinosaurs:
    if "saurus" in dino:
        saurus_dinosaurs.append(dino)

saurus_dinosaurs = [dino for dino in dinosaurs if "saurus" in dino] # Tongue twister

print(saurus_dinosaurs)

