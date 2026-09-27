# A Program to observe the state of a generator

def count_numbers():
    print("Starting generator")

    yield 1

    print("Resuming generator")

    yield 2

    print("Resuming generator again")

    yield 3


counter = count_numbers()

print(next(counter))
print(next(counter))
print(next(counter))


# Explanation:
# A generator remembers its execution state whenever it reaches a yield statement.
# The first next() starts the generator and executes statements until the first yield.
# The generator then pauses while remembering its current position.
# The second next() resumes execution from the statement after the previous yield and continues until the next yield.
# The third next() repeats the same process.
# This pause-and-resume behavior is one of the most important characteristics of generators.

# Real-Life Use:
# Generator state is useful when processing large streams where work needs to be paused and resumed without restarting the task.