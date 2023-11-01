import math
import datetime

class XORShift:
    """
    XORShift pseudo-random number generator class.
    """

    def __init__(self, seed = datetime.datetime.now().microsecond):
        """
        Initialize the XORShift generator with an optional seed value.

        :param seed: (int) Seed value for the generator (default is the current microsecond).
        """
        self.state = seed

    def xorshift(self):
        """
        Perform a single XORShift operation on the internal state.

        :return: (int) The next pseudo-random number in the sequence.
        """
        self.state ^= (self.state << 13) & 0xFFFFFFFF
        self.state ^= (self.state >> 17) & 0xFFFFFFFF
        self.state ^= (self.state << 5) & 0xFFFFFFFF
        return self.state

    def rand(self):
        """
        Generate a random float value between 0 and 1.

        :return: (float) A random float in the range [0, 1).
        """
        return self.xorshift() / 0x100000000

    def randint(self, mn: int, mx: int):
        """
        Generate a random integer within a specified range.

        :param mn: (int) Minimum value (inclusive).
        :param mx: (int) Maximum value (exclusive).

        :return: (int) A random integer in the range [mn, mx).
        """
        return math.floor(self.rand() * (mx - mn)) + mn

    def shuffle(self, arr):
        """
        Shuffle the elements of a given list in place.

        :param arr: (list) The list to be shuffled.
        """
        n = len(arr)
        for i in range(n):
            pos = self.randint(0, n)
            arr[i], arr[pos] = arr[pos], arr[i]

    def choice(self, arr):
        """
        Choose a random element from a given list.

        :param arr: (list) The list from which to choose.

        :return: (any) A randomly selected element from the input list.
        """
        return arr[self.randint(0, len(arr))]
