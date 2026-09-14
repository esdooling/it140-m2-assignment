"""TODO: Replace with a one-line summary of the program's purpose (<73 chars).

Input:
    TODO: Replace with a major input, including its type and source.
    TODO: Replace with another major input, or delete this TODO line.
    TODO: Replace with another major input, or delete this TODO line.

Process:
    TODO: Replace with a major processing step.

Output:
    TODO: Replace with a major output, including its type and destination.

Typical usage example:
    TODO: Replace with the input prompt and original name-input example.
    TODO: Replace with the input prompt and original age-input example.
    TODO: Replace with the resulting output from those inputs.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""
    name = input("What is your name? ")
    age = int(input("How old are you? "))

    BIRTH_YEAR = CURRENT_YEAR - age
    print(f"Hello {name}! You were born in {BIRTH_YEAR}.")

# === Main Guard ===
if __name__ == "__main__":
    main()
