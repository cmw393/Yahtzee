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
            " |       | ",
            "  -------  "],

        2: ["  _______  ",
            " | •     | ",
            " |       | ",
            " |     • | ",
            "  -------  "],

        3: ["  _______  ",
            " | •     | ",
            " |   •   | ",
            " |     • | ",
            "  -------  "],

        4: ["  _______  ",
            " | •   • | ",
            " |       | ",
            " | •   • | ",
            "  -------  "],

        5: ["  _______  ",
            " | •   • | ",
            " |   •   | ",
            " | •   • | ",
            "  -------  "],

        6: ["  _______  ",
            " | •   • | ",
            " | •   • | ",
            " | •   • | ",
            "  -------  "]
    }
    lines_per_die_face = 5

    # ANSI Color Coding
    color_code_held = "\033[92m"  # Green text for held dice
    color_code_reset = "\033[0m"  # Reset to default color

    # Display the ASCII art for each die
    for l in range(lines_per_die_face):
        for i, value in enumerate(values):
            # Determine if the die is held and set the color accordingly
            color = color_code_held if i in held_indices else color_code_reset
            if value in dice_faces:
                dice = dice_faces[value]
                print(f"{color}{dice[l]}{color_code_reset}", end='')
        print()