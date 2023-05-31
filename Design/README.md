# Problems Solved [6 : 3E, 3M]

### 1. [Leetcode 705: Design HashSet](https://leetcode.com/problems/design-hashset/) [EASY]

We used a normal list and made buckets (number being a prime : https://medium.com/swlh/why-should-the-length-of-your-hash-table-be-a-prime-number-760ec65a75d1) to imitate the functions of a hashset. We used Modulo Hash Function.

### 2. [Leetcode 155: Design MinStack](https://leetcode.com/problems/min-stack/) [MEDIUM]

We maintained a seperate pointer for storing curr_min and also maintained a seperate list for prev_mins. This helped us perform getMin() in O(1) Time Complexity.

### 3. [Leetcode 1472: Design Browser History](https://leetcode.com/problems/design-browser-history/) [MEDIUM]

We used a similar logic like Minstack to store the visited pages in an array, implemented the visit function checking if we are always inserting in end , if not pop till we reach there. (Alternative: Maintain an addnl bound variable and then just insert at curr and make it the new bound)

### 4. [Leetcode 706: Design HashMap](https://leetcode.com/problems/design-hashmap/) [EASY]
Use similar concept like HashSet i.e. bucketing or linear chaining. (Array inside Array) to imitate a hashmap.

### 5. [Leetcode 232: Design Queue Using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) [EASY]
Whenever we Pop we push all the elements except last one into the other stack. Push normally at 0th position in the first stack.

### 6. [Leetcode 1396: Design Underground System](https://leetcode.com/problems/design-underground-system/) [MEDIUM]

We used three hashmaps, one to store travels, another to store the time required for a route and lastly another for maintaining count of the passengers who travelled on a particular route.