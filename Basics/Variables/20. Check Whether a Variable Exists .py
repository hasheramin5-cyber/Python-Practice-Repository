# Checking Whether a Variable Exists in the Current Scope

name = "Hasher"

if "name" in locals():
    print("Variable exists.")
else:
    print("Variable does not exist.")
    
# Explaining the code:
# The code checks if the variable 'name' exists in the current local scope using the locals() function. If it exists, it prints "Variable exists." Otherwise, it prints "Variable does not exist."