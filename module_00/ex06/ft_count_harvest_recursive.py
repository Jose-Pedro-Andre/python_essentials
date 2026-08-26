

days = 0;

def  ft_helper(day:int, iter:int):
    if  day == 0:
        return 0
    print(f'Day {iter}')
    return ft_helper(day - 1, iter + 1)

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    ft_helper(days, 1)
    print("Harvest time!")
    
# ft_count_harvest_recursive()