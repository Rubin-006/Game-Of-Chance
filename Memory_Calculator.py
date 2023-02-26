
#Function calculates actual Memory size of your USB Flash Drive

def Memory_calc(size):
    size = size.replace("GB","")
    num = int(size)
    actual_size = num*0.93
    return f"{actual_size} GB" if actual_size > 1 else f"{actual_size*1000 }MB"


print(Memory_calc("2GB"))