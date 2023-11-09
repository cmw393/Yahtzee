from typing import List

def display_dice(values: List[int], held_indices: List[int] = []):
    """
    Display the current face-up values of the dice with updated ASCII art.
    
    Parameters:
    - values (List[int]): A list of integers representing the current face-up values of the dice.
    - held_indices (List[int], optional): A list of integers representing the indices of dice that are held.
      Default is an empty list.
    """
    # Updated ASCII Art for Dice Faces
    dice_faces = {
        1: ["  _______  ",
            " |       | ",
            " |   •   | ",
            " |_______| "],

        2: ["  _______  ",
            " | •     | ",
            " |       | ",
            " |____•__| "],

        3: ["  _______  ",
            " | •     | ",
            " |   •   | ",
            " |____•__| "],

        4: ["  _______  ",
            " | •   • | ",
            " |       | ",
            " | •___• | "],

        5: ["  _______  ",
            " | •   • | ",
            " |   •   | ",
            " | •___• | "],

        6: ["  _______  ",
            " | •   • | ",
            " | •   • | ",
            " | •___• | "]
    }

    # ANSI Color Coding
    color_code_held = "\033[92m"  # Green text for held dice
    color_code_reset = "\033[0m"  # Reset to default color

    # Display the ASCII art for each die
    for i, value in enumerate(values):
        # Determine if the die is held and set the color accordingly
        color = color_code_held if i in held_indices else color_code_reset

        # Display the ASCII art for the current die value
        if value in dice_faces:
            dice = dice_faces[value]
            for line in dice:
                print(f"{color}{line}{color}")
            print()



