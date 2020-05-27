def tetration(value1, value2):
    current_power = value2

    for i in range(1,value1-1):
        current_power **= value2

    return value2**current_power
