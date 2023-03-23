class Solution(object):
    def fizzBuzz(self, val):
        index = 1
        arr = []
        while index <= val:
            if index % 3 == 0 and index % 5 == 0:
                arr.append("FizzBuzz")
            elif index %3 == 0:
                arr.append("Fizz")
            elif index %5 == 0:
                arr.append("Buzz")
            else:
                arr.append(str(index))
            index += 1
        return arr
