# Problems Solved [4 : E, M]

### 1. [Leetcode 34: Find First and Last Position of an Element in Sorted Array.](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) [MEDIUM]
We use a basic working of Binary Search to our advantage. Suppose we search for an element just lesser than a target value (which should not exist in the array) , we end up with low pointer pointing to first occurence and similarly if we end up querying for an element just greater than target, we will end up with low pointer pointing to the element just greater than the last occurence. If we end up returning low for both calls, and return ans as (first, second-1), we will get our answer.

### 2. [Leetcode 74: Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) [MEDIUM]
Perform Binary Search on the Matrix as if its an 1D Array. Use formula matrix[mid//col][mid%col] to calculate mid element properly.

### 3. [Leetcode 1472: Design Browser History](https://leetcode.com/problems/design-browser-history/) [MEDIUM]

We used a similar logic like Minstack to store the visited pages in an array, implemented the visit function checking if we are always inserting in end , if not pop till we reach there. (Alternative: Maintain an addnl bound variable and then just insert at curr and make it the new bound)

### 4. [Leetcode 706: Design HashMap](https://leetcode.com/problems/design-hashmap/) [EASY]
Use similar concept like HashSet i.e. bucketing or linear chaining. (Array inside Array) to imitate a hashmap.