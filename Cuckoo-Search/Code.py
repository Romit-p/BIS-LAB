def solar_power(v):
    i = 8 - 0.02 * v
    return v * i

def cuckoo_search():
    nests = [20, 40, 60, 80, 90]
    best_power = 0
    best_voltage = 0

    print("Solar Energy Optimization using Cuckoo Search\n")

    for iteration, voltage in enumerate(nests, 1):
        power = solar_power(voltage)

        if power > best_power:
            best_power = power
            best_voltage = voltage

        print("Iteration", iteration, ": Power =", round(best_power), "W")

    print("\nFinal Result:")
    print("Optimal Voltage =", best_voltage, "V")
    print("Maximum Power =", round(best_power), "W")
    print("Optimization completed.")

cuckoo_search()
