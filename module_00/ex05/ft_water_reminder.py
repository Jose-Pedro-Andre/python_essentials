def ft_water_reminder():
    days = int(input("Days since last watering: "))
    if days > 2:
        print("Water the plant!")
        return True
    print("Plants are fine.")
    return False

# ft_water_reminder()