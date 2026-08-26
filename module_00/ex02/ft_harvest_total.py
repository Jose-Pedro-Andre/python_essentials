def ft_harvest_total():
    n1  = 0;
    for i in range(1, 4):
        n1 =  n1 + int(input(f"Day {i} harvest: "))
    print(f'Total harvest: {n1}')

# ft_harvest_total()