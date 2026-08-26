def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    day = 0;

    while day < days:
        day += 1
        print(f'Day {day}')
    print("Harvest time!")

# ft_count_harvest_iterative()