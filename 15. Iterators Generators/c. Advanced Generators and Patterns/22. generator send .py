# A Program to send values into a generator

def calculator():
    number = 0

    while True:
        value = yield number
        number += value


calculator_generator = calculator()

print(next(calculator_generator))
print(calculator_generator.send(5))
print(calculator_generator.send(10))
print(calculator_generator.send(20))


# Explanation:
# A generator can receive values from outside using the send() method.
# The yield expression pauses the generator and can also receive a value when execution resumes.

# The first next() starts the generator and reaches:

# value = yield number

# At this point, the generator pauses and returns 0.
# When send(5) is called, the value 5 is assigned to value.
# The generator then adds 5 to number and yields the new result.
# The same process continues when send(10) and send(20) are called.
# This makes generators capable of receiving information while they are producing information.

# Real-Life Use:
# send() can be useful for building stateful generators, interactive data processors, and streaming calculations.