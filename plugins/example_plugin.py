"""
Loom plugin example.

Any .py file dropped in /plugins can define functions here, then be called
from a recipe's action via:

    {"action_type": "run_python_callable",
     "action_config": {"plugin": "example_plugin", "function": "say_hello", "kwargs": {"name": "Daniel"}}}
"""


def say_hello(name="world"):
    message = f"Hello, {name}! This came from a Loom plugin."
    print(message)
    return message
