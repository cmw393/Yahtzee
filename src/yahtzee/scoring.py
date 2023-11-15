from collections import Counter

class Scoring:
    def __init__(self):
        self.score_card = {}
        self.all_categories = set(["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes",
                                   "Three of a Kind", "Four of a Kind", "Full House",
                                   "Small Straight", "Large Straight", "Yahtzee", "Chance"])
    def calculate_score(self, category: str, dice_values: list) -> int:
        """
        Calculate the score for a given category and dice values.
        """
        if category not in self.all_categories:
            raise ValueError(f"Invalid category: {category}")

        # Use Python's Counter class to count occurrences of each die value
        dice_counts = Counter(dice_values)

        # Scoring logic for single-number categories (Ones, Twos, etc.)
        if category in ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"]:
            catTest = {"Ones" : 1, "Twos" : 2, "Threes" : 3, "Fours" : 4, "Fives" : 5, "Sixes" : 6}
            return  dice_counts[catTest[category]] * catTest[category] #Maps user input(category) to a int value for counter to check, then multipes by said value

        # Scoring logic for Three of a Kind and Four of a Kind
        elif category in ["Three of a Kind", "Four of a Kind"]:
            target_count = 3 if category == "Three of a Kind" else 4
            for value, count in dice_counts.items():
                if count >= target_count:
                    return value * target_count
            return 0

        # Scoring logic for Full House
        elif category == "Full House":
            unique_counts = set(dice_counts.values())
            if unique_counts == {2, 3}:
                return 25
            return 0


        # Scoring logic for Small Straight
        elif category == "Small Straight":
            sorted_values = sorted(dice_values)
            # Check for a Small Straight
            if any(sorted_values[i + 1] - sorted_values[i] != 1 for i in range(len(sorted_values) - 1)):
                return 0  # Not a Small Straight
            return 25  # Small Straight

        # Scoring logic for Large Straight
        elif category == "Large Straight":
            sorted_values = sorted(dice_values)
            # Check for a Large Straight
            if all(sorted_values[i + 1] - sorted_values[i] == 1 for i in range(len(sorted_values) - 1)):
                return 30  # Large Straight
            return 0  # Not a Large Straight

        # Scoring logic for Yahtzee
        elif category == "Yahtzee":
            for value, count in dice_counts.items():
                if count == 5:
                    return 50
            return 0

        # Scoring logic for Chance
        elif category == "Chance":
            return sum(dice_values)

        return 0  # Default case, return 0 if the category is not recognized

    def mark_score(self, category: str, score: int):
        """
        Records a score for a given category in score_card.
        """
        if category not in self.all_categories:
            raise ValueError(f"Invalid category: {category}")

        if category in self.score_card:
            raise ValueError(f"Category {category} already scored")

        self.score_card[category] = score

    def get_score_card(self) -> dict:
        """
        Returns the current score_card.
        """
        return self.score_card
    
    def is_category_used(self, category: str) -> bool:
        """
        Checks if a category has already been used.
        """
        return category in self.score_card
    
    def remaining_categories(self) -> list:
        """
        Returns a list of remaining categories.
        """
        return list(self.all_categories - set(self.score_card.keys()))
    
    def remaining_categories(self) -> list:
        """
        Returns a list of remaining categories.
        """
        used_categories = set(self.score_card.keys())
        return list(set(self.all_categories) - used_categories)

    
    def num_used_categories(self) -> int:
        """
        Returns the number of used categories.
        """
        return len(self.score_card)
    
    def is_full(self) -> bool:
        """
        Checks if the score card is full.
        """
        return len(self.score_card) == len(self.all_categories)
    def display_score_card(self):
        print("Score Card:")
        for category, score in self.score_card.items():
            print(f"{category}: {score}")