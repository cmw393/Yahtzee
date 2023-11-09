from typing import List

def display_dice(values: List[int], held_indices: List[int] = []):
    """
    Display the current face-up values of the dice with ASCII art.
    
    Parameters:
    - values (List[int]): A list of integers representing the current face-up values of the dice.
    - held_indices (List[int], optional): A list of integers representing the indices of dice that are held.
      Default is an empty list.
    """
    # Step 3: Define ASCII Art for Dice Faces
    dice_faces = {
        1: ["-----", "|   |", "| o |", "|   |", "-----"],
        2: ["-----", "|o  |", "|   |", "|  o|", "-----"],
        3: ["-----", "|o  |", "| o |", "|  o|", "-----"],
        4: ["-----", "|o o|", "|   |", "|o o|", "-----"],
        5: ["-----", "|o o|", "| o |", "|o o|", "-----"],
        6: ["-----", "|o o|", "|o o|", "|o o|", "-----"]
    }
    
    # Step 4: Implement ANSI Color Coding
    color_code_held = "\033[92m"  # Green text for held dice
    color_code_reset = "\033[0m"  # Reset to default color
    
    # Step 5: Construct and Display the ASCII Art
    for i, value in enumerate(values):
        # Determine if the die is held and set the color accordingly
        color = color_code_held if i in held_indices else color_code_reset
        
        # Display the ASCII art for the current die value
        if value in dice_faces:
            dice = dice_faces[value]
            for line in dice:
                print(f"{color}{line}{color}", end="  ")
            print()


