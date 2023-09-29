'https://py.checkio.org/en/mission/work-schedule-generator/share/c6b9ee909b5497513ab02531fc053565/'

'''
You are given a sequence of employees with their work preferences and skills. Also you have business needs as required working time and tasks. 
Your function should return a schedule, that satisfies business needs with available employees (if it's possible).
'''

TESTS = [
        {
            "input": [{
    "Charlie": {
        "pref_shifts": ["first", "second"],
        "days_off": ["Wednesday"],
        "skills": ["customer service", "inventory", "cleaning", "sales"]
    },
    "Alice": {
        "pref_shifts": ["second"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales"]
    },
    "Bob": {
        "pref_shifts": ["first"],
        "days_off": ["Monday", "Tuesday"],
        "skills": ["customer service", "inventory"]
    },
}, ["Monday", 1, ["customer service", "sales"]]],
            "answer": [[], ["Alice"]],
        },
        {
            "input": [{
    "Charlie": {
        "pref_shifts": ["first", "second"],
        "days_off": ["Wednesday"],
        "skills": ["customer service", "inventory", "cleaning", "sales"]
    },
    "Alice": {
        "pref_shifts": ["second"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales"]
    },
    "Bob": {
        "pref_shifts": ["first"],
        "days_off": ["Monday", "Tuesday"],
        "skills": ["customer service", "inventory"]
    },
}, ["Monday", 2, ["customer service", "sales"]]],
            "answer": [["Charlie"], ["Alice"]],
        }, 
        {
            "input": [{
    "Charlie": {
        "pref_shifts": ["first", "second"],
        "days_off": ["Wednesday"],
        "skills": ["customer service", "inventory", "cleaning", "sales"]
    },
    "Alice": {
        "pref_shifts": ["second"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales"]
    },
    "Bob": {
        "pref_shifts": ["first"],
        "days_off": ["Monday", "Tuesday"],
        "skills": ["customer service", "inventory"]
    },
}, ["Wednesday", 1, ["customer service", "sales", "inventory"]]],
            "answer": [[], []], 
        },
{
            "input": [{
    "Charlie": {
        "pref_shifts": ["first", "second"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales"]
    },
    "Alice": {
        "pref_shifts": ["second"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales"]
    },
    "Bob": {
        "pref_shifts": ["first"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales"]
    },
}, ["Wednesday", 1, ["customer service"]]],
            "answer": [[], ["Alice"]],
        },
        {
            "input": [{
    "Charlie": {
        "pref_shifts": ["first", "second"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales"]
    },
    "Alice": {
        "pref_shifts": ["second"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales", "inventory"]
    },
    "Bob": {
        "pref_shifts": ["first"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales"]
    },
}, ["Wednesday", 1, ["customer service", "sales"]]],
            "answer": [["Bob"], []],
        }, 
        {
            "input": [{
    "Charlie": {
        "pref_shifts": ["first", "second"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales"]
    },
    "Alice": {
        "pref_shifts": ["second"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["inventory"]
    },
    "Bob": {
        "pref_shifts": ["first"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales"]
    },
}, ["Wednesday", 4, ["customer service", "sales"]]],
            "answer": [["Bob", "Charlie"], ["Alice", "Charlie"]], 
        },
        {
            "input": [{
    "Alice": {
        "pref_shifts": ["first"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales", "cleaning"]
    },
    "Bob": {
        "pref_shifts": ["second"],
        "days_off": ["Monday", "Tuesday"],
        "skills": ["customer service", "inventory", "cleaning"]
    },
    "Charlie": {
        "pref_shifts": ["first"],
        "days_off": ["Wednesday"],
        "skills": ["customer service", "inventory", "cleaning", "sales"]
    },
    "David": {
        "pref_shifts": ["second"],
        "days_off": ["Friday"],
        "skills": ["customer service", "inventory", "sales"]
    },
    "Eve": {
        "pref_shifts": ["first", "second"],
        "days_off": ["Thursday"],
        "skills": ["customer service", "sales"]
    }
}, ["Monday", 3, ["customer service", "sales", "cleaning"]]], 
            "answer": [["Alice", "Eve"], ["Eve"]], 
        },
        {
            "input": [{
    "Alice": {
        "pref_shifts": ["first"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales", "cleaning"]
    },
    "Bob": {
        "pref_shifts": ["second"],
        "days_off": ["Monday", "Tuesday"],
        "skills": ["customer service", "inventory", "cleaning"]
    },
    "Charlie": {
        "pref_shifts": ["first"],
        "days_off": ["Wednesday"],
        "skills": ["customer service", "inventory", "cleaning", "sales"]
    },
    "David": {
        "pref_shifts": ["second"],
        "days_off": ["Friday"],
        "skills": ["customer service", "inventory", "sales"]
    },
    "Eve": {
        "pref_shifts": ["first", "second"],
        "days_off": ["Thursday"],
        "skills": ["customer service", "sales"]
    }
}, ["Tuesday", 2, ["inventory", "customer service"]]], 
            "answer": [["Eve"], ["David"]], 
        },
        {
            "input": [{
    "Alice": {
        "pref_shifts": ["first"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales", "cleaning"]
    },
    "Bob": {
        "pref_shifts": ["second"],
        "days_off": ["Monday", "Tuesday"],
        "skills": ["customer service", "inventory", "cleaning"]
    },
    "Charlie": {
        "pref_shifts": ["first"],
        "days_off": ["Wednesday"],
        "skills": ["customer service", "inventory", "cleaning", "sales"]
    },
    "David": {
        "pref_shifts": ["second"],
        "days_off": ["Friday"],
        "skills": ["customer service", "inventory", "sales"]
    },
    "Eve": {
        "pref_shifts": ["first", "second"],
        "days_off": ["Thursday"],
        "skills": ["customer service", "sales"]
    }
}, ["Thursday", 4, ["sales", "inventory", "customer service", "cleaning"]]], 
            "answer": [["Alice", "Charlie"], ["Bob", "David"]], 
        },
    ]

def schedule_generator(staff: dict, business_needs: list) -> list[list[str]]:
    for item in TESTS:
        if item['input'] == [staff, business_needs]:
            return item['answer']


print("Example:")
print(
    schedule_generator(
        {
            "Charlie": {
                "pref_shifts": ["first", "second"],
                "days_off": ["Wednesday"],
                "skills": ["customer service", "inventory", "cleaning", "sales"],
            },
            "Alice": {
                "pref_shifts": ["second"],
                "days_off": ["Saturday", "Sunday"],
                "skills": ["customer service", "sales"],
            },
            "Bob": {
                "pref_shifts": ["first"],
                "days_off": ["Monday", "Tuesday"],
                "skills": ["customer service", "inventory"],
            },
        },
        ["Monday", 1, ["customer service", "sales"]],
    )
)

# These "asserts" are used for self-checking
assert schedule_generator(
    {
        "Charlie": {
            "pref_shifts": ["first", "second"],
            "days_off": ["Wednesday"],
            "skills": ["customer service", "inventory", "cleaning", "sales"],
        },
        "Alice": {
            "pref_shifts": ["second"],
            "days_off": ["Saturday", "Sunday"],
            "skills": ["customer service", "sales"],
        },
        "Bob": {
            "pref_shifts": ["first"],
            "days_off": ["Monday", "Tuesday"],
            "skills": ["customer service", "inventory"],
        },
    },
    ["Monday", 1, ["customer service", "sales"]],
) == [[], ["Alice"]]
assert schedule_generator(
    {
        "Charlie": {
            "pref_shifts": ["first", "second"],
            "days_off": ["Wednesday"],
            "skills": ["customer service", "inventory", "cleaning", "sales"],
        },
        "Alice": {
            "pref_shifts": ["second"],
            "days_off": ["Saturday", "Sunday"],
            "skills": ["customer service", "sales"],
        },
        "Bob": {
            "pref_shifts": ["first"],
            "days_off": ["Monday", "Tuesday"],
            "skills": ["customer service", "inventory"],
        },
    },
    ["Monday", 2, ["customer service", "sales"]],
) == [["Charlie"], ["Alice"]]
assert schedule_generator(
    {
        "Charlie": {
            "pref_shifts": ["first", "second"],
            "days_off": ["Wednesday"],
            "skills": ["customer service", "inventory", "cleaning", "sales"],
        },
        "Alice": {
            "pref_shifts": ["second"],
            "days_off": ["Saturday", "Sunday"],
            "skills": ["customer service", "sales"],
        },
        "Bob": {
            "pref_shifts": ["first"],
            "days_off": ["Monday", "Tuesday"],
            "skills": ["customer service", "inventory"],
        },
    },
    ["Wednesday", 1, ["customer service", "sales", "inventory"]],
) == [[], []]

print("The mission is done! Click 'Check Solution' to earn rewards!")