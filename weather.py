import statistics

temperature = [35, 35, 33, 34, 34, 35, 36, 36, 37, 38]  # in Celsius
humidity = [40, 42, 38, 35, 37, 39, 41, 43, 45, 44]    # in Percentage (%)
aqi = [120, 135, 110, 98, 105, 115, 140, 150, 160, 130]  # AQI values

# ==========================================

def calculate_average(data):
    return sum(data) / len(data)

def calculate_median(data):
    return statistics.median(data)

def print_results(label, data, unit):
    avg = calculate_average(data)
    median = calculate_median(data)

    print(f"\n{label} Analysis")
    print("----------------------")
    print(f"Average {label}: {avg:.2f} {unit}")
    print(f"Median {label}: {median:.2f} {unit}")

# Display Results
print("Weather & AQI Statistics for Last 10 Days - Gandhinagar")
print("=========================================================")

print_results("Temperature", temperature, "°C")
print_results("Humidity", humidity, "%")
print_results("AQI", aqi, "")
