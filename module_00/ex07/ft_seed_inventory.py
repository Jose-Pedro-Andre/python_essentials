def  ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type[0].upper() + seed_type[1:]
    if unit.find("packets") == 0:
        print(f'{seed_type} seeds: {quantity} {unit} available')
    elif unit.find("grams") == 0:
        print(f'{seed_type} seeds: {quantity} {unit} total')
    elif unit.find("area") == 0:
        print(f'{seed_type} seed: covers {quantity} square metters')
    else:
        print("Unknown unit type")
        
ft_seed_inventory("tomato", 12, "packet")