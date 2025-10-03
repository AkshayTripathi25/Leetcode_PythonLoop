def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(power="Lazar",name="Dracula")
print_kwargs(name="Goku", power="Kamehameha", age=24)
print_kwargs(name="Vegeta", power="Final Flash", age=28, wife="Bulma")