import re

def format_template(template, values):
    # Define a function to replace placeholders with corresponding values
    def replace_placeholder(match):
        key = match.group(1)
        return str(values.get(key, f"{{{key}}}"))

    # Use regular expressions to find placeholders and replace them
    formatted_string = re.sub(r'\{(\w+)\}', replace_placeholder, template)
    return formatted_string

# Example usage:
template_str = "Hello, {name}! You are {age} years old and live in {city}."
values_dict = {
    "name": "Alice",
    "age": 30,
    # "city" key is intentionally omitted to demonstrate leaving the placeholder as is
}

result = format_template(template_str, values_dict)
print(result)
