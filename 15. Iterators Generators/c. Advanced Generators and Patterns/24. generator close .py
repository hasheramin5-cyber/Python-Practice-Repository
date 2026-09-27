# A Program to close a generator

def data_generator():
    try:
        while True:
            value = yield
            print("Received:", value)

    except GeneratorExit:
        print("Generator closed.")


data = data_generator()

next(data)

data.send("Python")
data.send("Generator")

data.close()


# Explanation:
# The close() method stops a generator before it naturally reaches the end of its execution.
# The generator is paused at the yield statement while waiting for another value.
# Calling close() raises GeneratorExit inside the generator.
# The GeneratorExit exception can be handled using a try-except block.
# After the generator is closed, it cannot continue producing values normally.

# Real-Life Use:
# close() is useful when a generator controls resources or processes a stream that needs to be stopped early.