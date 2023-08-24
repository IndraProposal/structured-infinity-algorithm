class StructuredInfinity:
    def __init__(self, start=1):
        self.current = start

    def next(self):
        """Returns the next number in the infinite sequence."""
        result = self.current
        self.current += 1
        return result

    def concatenate(self, n):
        """Returns the concatenation of the first n numbers in the sequence."""
        return ''.join(str(self.next()) for _ in range(n))

    def reset(self):
        """Resets the sequence to the beginning."""
        self.current = 1

    def explore_structure(self, n):
        """Prints the structure of the infinite sequence up to n numbers."""
        self.reset()
        for _ in range(n):
            print(self.next())

# Example usage
infinity = StructuredInfinity()
print("Concatenation of first 10 numbers:", infinity.concatenate(10))
infinity.explore_structure(10)
