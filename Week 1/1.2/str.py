"""This file creates a simple String class equivalent."""

class StringClass:

    def __init__(self, value: str):
        self.value = value

    def __add__(self, other: str):
        # When two strings are added, we concatenate them and return it
        return StringClass(self.value + other)

    def __sub__(self, other: str):
        # Cannot substract strings
        raise Exception(f"Strings cannot be subtracted from one another!")

    def __len__(self):
        return len(self.value)

    def split(self, sep: str = ' '):
        # This can be done recursively or iteratively
        # This splits a string depending on the separator - by default, it should work on whitespace
        assert sep in {' ', ','}, "Separator provided is not supported in class!" # Negative space programming by Primagen
        # If no separator is found in the list, just return the string value (not object)
        if sep not in self.value:
            return self.value
        # Output is a list and must keep a track of when separator is seen
        split_list = []
        running_characters = StringClass(value="")
        for char in self.value: # or i = 0; while i <= len(self.value); i += 1 but this requires integer addition
            if char != sep:
                # Now add the character to the running list of characters
                running_characters += char
            else:
                # Separator is found, so we add the running characters into a list and restart
                split_list.append(running_characters.value)
                running_characters = StringClass(value="")
        # This looks at the final potential remaining characters
        if len(running_characters.value) > 0:
            split_list.append(running_characters.value)
        return split_list

        # Note: We are cheating by using the .append from a list but it is fine as we are not recreating the list class

# To specify a seperator, use input() for user interaction
obj_a = StringClass(value='Hi there !')
obj_b = StringClass(value='I am John.')
c = obj_a.split(sep= ' ')
print(c)
print(obj_a - obj_b)

# Challenge: See if you can implement the 'split' method recursively?