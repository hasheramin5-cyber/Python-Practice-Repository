# A Program to handle an exception inside a generator

def message_generator():
    try:
        while True:
            message = yield
            print("Message:", message)

    except ValueError:
        print("Invalid message received.")


messages = message_generator()

next(messages)

messages.send("Hello")
messages.send("Python")

messages.throw(ValueError)


# Explanation:
# The throw() method allows an exception to be sent into a generator at its current paused position.
# The generator waits at the yield statement for a value.
# The send() method normally resumes the generator with a value.
# The throw() method instead resumes it by raising an exception.
# The generator contains a try-except block that catches the ValueError exception.
# When throw(ValueError) is called, the exception enters the generator and is handled by the except block.

# Real-Life Use:
# throw() can be useful when a generator needs to handle errors or external events while processing a data stream.