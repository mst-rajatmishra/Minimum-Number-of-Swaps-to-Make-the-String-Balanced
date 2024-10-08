class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        unmatched_closing = 0
        
        for char in s:
            if char == '[':
                balance += 1
            else:  # char == ']'
                balance -= 1
            
            # If balance is negative, we have unmatched closing brackets
            if balance < 0:
                unmatched_closing += 1  # Count unmatched closing brackets
                balance = 0  # Reset balance
        
        # The number of swaps needed is equal to the number of unmatched closing brackets
        return (unmatched_closing + 1) // 2  # Each swap fixes two unmatched brackets

# Example Usage:
solution = Solution()
print(solution.minSwaps("][]["))  # Output: 1
print(solution.minSwaps("]]][[["))  # Output: 2
print(solution.minSwaps("[]"))  # Output: 0
print(solution.minSwaps("][][]["))  # Output: 1
print(solution.minSwaps("]]]]][[[["))  # Output: 3
print(solution.minSwaps("]]][[["))  # Output: 2
