import statistics

temperature = [35, 35, 33, 34, 34, 35, 36, 36, 37, 38]  # in Celsius
humidity = [40, 42, 38, 35, 37, 39, 41, 43, 45, 44]    # in Percentage (%)

# ==========================================

def calculate_average(data):
    return sum(data) / len(data)

def calculate_median(data):
    return statistics.median(data)

# Temperature Calculations
avg_temp = calculate_average(temperature)
median_temp = calculate_median(temperature)

# Humidity Calculations
avg_humidity = calculate_average(humidity)
median_humidity = calculate_median(humidity)

# Display Results
print("Weather Statistics for Last 10 Days - Gandhinagar")
print("--------------------------------------------------")

print(f"Average Temperature: {avg_temp:.2f} °C")
print(f"Median Temperature: {median_temp:.2f} °C")

print(f"Average Humidity: {avg_humidity:.2f} %")
print(f"Median Humidity: {median_humidity:.2f} %")
