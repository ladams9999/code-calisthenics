import re

class Solution:
    def isValid(self, word: str) -> bool:
        return False if re.match(r"^(?=.*[aeiouAEIOU])(?=.*[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ])(?=.{3,})[a-zA-Z0-9]+$", word) is None else True
    

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    word = "234Adas"
    print(f"Should be True: {solution.isValid(word)}")

    # Example 2
    word = "b3"
    print(f"Should be False: {solution.isValid(word)}")

    # Example 3
    word = "a3$e"
    print(f"Should be False: {solution.isValid(word)}")
    