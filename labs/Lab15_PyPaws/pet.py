"""
pet.py  -  STEP 1 and STEP 2

The Pet class is the blueprint for every animal in the PyPaws Shelter.
"""


def keep_in_range(value, low=0, high=100):
    """Return value, but never lower than low or higher than high.
    (Already done for you! You will use it in Step 2.)

    keep_in_range(130)  ->  100
    keep_in_range(-5)   ->  0
    keep_in_range(42)   ->  42
    """
    return max(low, min(high, value))


class Pet:
    """A shelter pet with a hunger level and a happiness level (both 0-100)."""

    # A CLASS attribute: one dictionary shared by every Pet.
    SOUNDS = {
        "cat": "Meow!",
        "dog": "Woof woof!",
        "hamster": "Squeak squeak!",
        "rabbit": "*thump thump*",
        "parrot": "Hello! Hello! Pretty bird!",
        "snake": "Hissssss...",
        "turtle": "...",
    }

    # ---------------------------------------------------------------
    # STEP 1: build the pet
    # ---------------------------------------------------------------
    def __init__(self, name, species, age, hunger=50, happiness=50):
        # Instance attributes: every pet keeps its own values.
        self.name = name
        self.species = species
        self.age = age
        self.hunger = hunger
        self.happiness = happiness
        self.adopted = False        # every pet starts out waiting for a home

    def __str__(self):
        # Example: Mochi the cat (age 3) | hunger 40 | happiness 75
        return f"{self.name} the {self.species} (age {self.age}) | hunger {self.hunger} | happiness {self.happiness}"

    def speak(self):
        """Return the sound this pet makes. (Already done for you!)"""
        sound = self.SOUNDS.get(self.species, "*stares at you*")
        return f"{self.name} says: {sound}"

    # ---------------------------------------------------------------
    # STEP 2: give the pet some behavior (methods)
    # ---------------------------------------------------------------
    def feed(self, amount=20):
        """Feeding makes the pet less hungry (never below 0)."""
        self.hunger = keep_in_range(self.hunger - amount)
        return f"{self.name} munches happily. Hunger is now {self.hunger}."

    def play(self, minutes=10):
        """Playing makes the pet happier, but also a little hungrier."""
        self.happiness = keep_in_range(self.happiness + minutes * 2)
        self.hunger = keep_in_range(self.hunger + 5)
        return f"You played with {self.name} for {minutes} minutes! Happiness is now {self.happiness}."

    def mood(self):
        """Return the pet's mood based on its happiness."""
        if self.happiness >= 70:
            return "happy (^_^)"
        elif self.happiness >= 40:
            return "okay (-_-)"
        else:
            return "sad (T_T)"
