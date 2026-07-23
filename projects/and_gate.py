# AND Gate using Python

def and_gate(a, b):
    return a & b

print("AND Gate Truth Table")
print("----------------------")
print("A B | Output")

for a in [0, 1]:
    for b in [0, 1]:
        print(a, b, "|", and_gate(a, b))s