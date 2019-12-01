def parse(path):
    with (open(path, "r")) as file:
        return [int(line.strip()) for line in file.readlines()]

def fuel(mass):
    return int(mass/3)-2

def rec_fuel(mass, ack_fuel = 0):
    f = fuel(mass)
    if f < 1:
        return ack_fuel
    return rec_fuel(f, ack_fuel + f)

if __name__ == "__main__":
    module_masses = parse("day1/input")
    module_fuel = [fuel(mass) for mass in module_masses]
    fuel_fuel = [rec_fuel(f) for f in module_fuel]

    print("a) " + str(sum(module_fuel)))
    print("b) " + str(sum(module_fuel + fuel_fuel)))