# A Program to simulate sensor data using a generator

def sensor_data():
    readings = [22.5, 23.1, 22.8, 24.2, 25.0]

    for reading in readings:
        yield reading


def high_temperature(readings):
    for reading in readings:
        if reading > 24:
            yield reading


readings = sensor_data()
high_readings = high_temperature(readings)

for reading in high_readings:
    print("High temperature:", reading)


# Explanation:
# The sensor_data() generator simulates values coming from a temperature sensor.
# Instead of returning all readings at once, it produces each reading through yield.
# The high_temperature() generator receives the readings and filters values greater than 24.
# Both stages work together as a lazy processing pipeline.
# A real sensor could replace the sample readings while the overall generator structure could remain similar.

# Real-Life Use:
# This pattern is useful for IoT systems, monitoring systems, sensor streams, and applications that process readings continuously.