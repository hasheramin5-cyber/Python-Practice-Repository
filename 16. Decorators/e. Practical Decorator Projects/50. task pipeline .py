# A Program to build a simple task pipeline using decorators

from functools import wraps


def pipeline_step(step_name):
    def decorator(function):
        @wraps(function)
        def wrapper(data):
            print(f"Starting step: {step_name}")

            result = function(data)

            print(f"Finished step: {step_name}")

            return result

        return wrapper

    return decorator


@pipeline_step("Clean Data")
def clean_data(data):
    return [item.strip() for item in data]


@pipeline_step("Convert Data")
def convert_data(data):
    return [item.upper() for item in data]


data = [" python ", " machine learning ", " robotics "]

data = clean_data(data)
data = convert_data(data)

print("Final data:", data)


# Explanation:
# pipeline_step() creates a configurable decorator for individual processing stages.
# Each decorated function represents one step in a data processing pipeline.
# The decorator displays the name of the step before and after the function executes.
# clean_data() first removes unnecessary whitespace.
# The cleaned result is then passed to convert_data().
# convert_data() transforms the cleaned values into uppercase.
# Each function remains focused on its own task while the decorator provides common pipeline behavior.

# Real-Life Use:
# Decorator-based pipelines can be useful for data processing, ETL workflows, automation systems, machine-learning preprocessing, and multi-step application workflows.