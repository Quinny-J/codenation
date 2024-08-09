from person import Person

q = Person("Q", "21", "Unmeasured")

print(f"Thanks for registering the user '{q.name}'")
print(f"""
Inputted Data For '{q.name}'
--------------------------
- {q.name}
- {q.age}
- {q.height}
""")

old_name = q.name
q.set_new_name("Quinny")

print(f"Thanks for updating the user '{old_name}'")
print(f"""
Updated Data For {old_name}
--------------------------
- {q.name}
- {q.age}
- {q.height}
""")

q.set_job("dev")
