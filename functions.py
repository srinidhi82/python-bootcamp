"""in defining function u define parameters to a function and hwne calling that 
function u can then pass same no of arguments(values)
"""
"""
2 Types of FUnctionas
1. Functions performing a task
2. FUnction performs a task and retruns a value
"""
def greet(first_name, last_name):
    print(f"Hey {first_name} {last_name}")

greet("Srini", "K")

# Function below returns a value

def get_greeting(name):
    return f"Hey {name}"

message = get_greeting("Joey")
print(message)