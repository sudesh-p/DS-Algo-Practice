class Solution:
    def switchCase(self, choice, arr):
        match choice:
            case 1:
                return 3.1415 * arr[0] * arr[0]
            case 2:
                return arr[0]*arr[1]
            case _:
                pass

choice = 1
arr = [5]
print(Solution().switchCase(choice,arr))