# Problems Solved [3 : 1E, 2M]

### 1. [Leetcode 705: Design HashSet](https://leetcode.com/problems/design-hashset/) [EASY]

We used a normal list and made buckets (number being a prime : https://medium.com/swlh/why-should-the-length-of-your-hash-table-be-a-prime-number-760ec65a75d1) to imitate the functions of a hashset. We used Modulo Hash Function.

### 2. [Leetcode 155: Design MinStack](https://leetcode.com/problems/min-stack/) [MEDIUM]

We maintained a seperate pointer for storing curr_min and also maintained a seperate list for prev_mins. This helped us perform getMin() in O(1) Time Complexity.

### 3. [Leetcode 1472: Design Browser History](https://leetcode.com/problems/design-browser-history/) [MEDIUM]

We used a similar logic like Minstack to store the visited pages in an array, implemented the visit function checking if we are always inserting in end , if not pop till we reach there. (Alternative: Maintain an addnl bound variable and then just insert at curr and make it the new bound)
