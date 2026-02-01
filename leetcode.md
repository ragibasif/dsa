# LeetCode

## Code Templates

### Two pointers: one input, opposite ends 

```py
def fn(arr):
    left = ans = 0
    right = len(arr) - 1

    while left < right:
        # do some logic here with left and right
        if CONDITION:
            left += 1
        else:
            right -= 1
    
    return ans
```

### Two pointers: two inputs, exhaust both

```py
def fn(arr1, arr2):
    i = j = ans = 0

    while i < len(arr1) and j < len(arr2):
        # do some logic here
        if CONDITION:
            i += 1
        else:
            j += 1
    
    while i < len(arr1):
        # do logic
        i += 1
    
    while j < len(arr2):
        # do logic
        j += 1
    
    return ans
```

### Sliding window

```py
def fn(arr):
    left = ans = curr = 0

    for right in range(len(arr)):
        # do logic here to add arr[right] to curr

        while WINDOW_CONDITION_BROKEN:
            # remove arr[left] from curr
            left += 1

        # update ans
    
    return ans
```

### Build a prefix sum

```py
def fn(arr):
    prefix = [arr[0]]
    for i in range(1, len(arr)):
        prefix.append(prefix[-1] + arr[i])
    
    return prefix
```

### Efficient string building

```py
# arr is a list of characters
def fn(arr):
    ans = []
    for c in arr:
        ans.append(c)
    
    return "".join(ans)
```

### Linked list: fast and slow pointer

```py
def fn(head):
    slow = head
    fast = head
    ans = 0

    while fast and fast.next:
        # do logic
        slow = slow.next
        fast = fast.next.next
    
    return ans
```

### Reversing a linked list

```py
def fn(head):
    curr = head
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node 
        
    return prev
```

### Find number of subarrays that fit an exact criteria

```py
from collections import defaultdict

def fn(arr, k):
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in arr:
        # do logic to change curr
        ans += counts[curr - k]
        counts[curr] += 1
    
    return ans
```

### Monotonic increasing stack

The same logic can be applied to maintain a monotonic queue.

```py
def fn(arr):
    stack = []
    ans = 0

    for num in arr:
        # for monotonic decreasing, just flip the > to <
        while stack and stack[-1] > num:
            # do logic
            stack.pop()
        stack.append(num)
    
    return ans
```

### Binary tree: DFS (recursive)

```py
def dfs(root):
    if not root:
        return
    
    ans = 0

    # do logic
    dfs(root.left)
    dfs(root.right)
    return ans
```

### Binary tree: DFS (iterative)

```py
def dfs(root):
    stack = [root]
    ans = 0

    while stack:
        node = stack.pop()
        # do logic
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return ans
```

### Binary tree: BFS 

```py
from collections import deque

def fn(root):
    queue = deque([root])
    ans = 0

    while queue:
        current_length = len(queue)
        # do logic for current level

        for _ in range(current_length):
            node = queue.popleft()
            # do logic
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return ans
```

### Graph: DFS (recursive)

For the graph templates, assume the nodes are numbered from 0 to n - 1 and the graph is given as an adjacency list. Depending on the problem, you may need to convert the input into an equivalent adjacency list before using the templates.

```py
def fn(graph):
    def dfs(node):
        ans = 0
        # do some logic
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                ans += dfs(neighbor)
        
        return ans

    seen = {START_NODE}
    return dfs(START_NODE)
```

### Graph: DFS (iterative)

```py
def fn(graph):
    stack = [START_NODE]
    seen = {START_NODE}
    ans = 0

    while stack:
        node = stack.pop()
        # do some logic
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
    
    return ans
```

### Graph: BFS

```py
from collections import deque

def fn(graph):
    queue = deque([START_NODE])
    seen = {START_NODE}
    ans = 0

    while queue:
        node = queue.popleft()
        # do some logic
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    
    return ans
```

### Find top k elements with heap

```py
import heapq

def fn(arr, k):
    heap = []
    for num in arr:
        # do some logic to push onto heap according to problem's criteria
        heapq.heappush(heap, (CRITERIA, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [num for num in heap]
```

### Binary search 

```py
def fn(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            # do something
            return
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    # left is the insertion point
    return left
```

### Binary search: duplicate elements, left-most insertion point

```py
def fn(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left
```

### Binary search: duplicate elements, right-most insertion point

```py
def fn(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1

    return left
```

### Binary search: for greedy problems

If looking for a minimum:

```py
def fn(arr):
    def check(x):
        # this function is implemented depending on the problem
        return BOOLEAN

    left = MINIMUM_POSSIBLE_ANSWER
    right = MAXIMUM_POSSIBLE_ANSWER
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1
    
    return left
```

If looking for a maximum:

```py
def fn(arr):
    def check(x):
        # this function is implemented depending on the problem
        return BOOLEAN

    left = MINIMUM_POSSIBLE_ANSWER
    right = MAXIMUM_POSSIBLE_ANSWER
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    
    return right
```

### Backtracking

```py
def backtrack(curr, OTHER_ARGUMENTS...):
    if (BASE_CASE):
        # modify the answer
        return
    
    ans = 0
    for (ITERATE_OVER_INPUT):
        # modify the current state
        ans += backtrack(curr, OTHER_ARGUMENTS...)
        # undo the modification of the current state
    
    return ans
```

### Dynamic programming: top-down memoization

```py
def fn(arr):
    def dp(STATE):
        if BASE_CASE:
            return 0
        
        if STATE in memo:
            return memo[STATE]
        
        ans = RECURRENCE_RELATION(STATE)
        memo[STATE] = ans
        return ans

    memo = {}
    return dp(STATE_FOR_WHOLE_INPUT)
```


To convert a top-down solution to a bottom-up one:

1. Initialize an array `dp` that is sized according to the state variables. For example, let's say the input to the problem was an array `nums` and an integer `k` that represents the maximum number of actions allowed. Your array `dp` would be 2D with one dimension of length `nums.length` and the other of length `k`. In the top-down approach, we had a function `dp`. We want these two to be equivalent. For example, the value of `dp(4, 6)` can now be found in `dp[4][6]`.

2. Set your base cases, same as the ones you are using in your top-down function. In the example we just looked at, we had `dp(0)` = `dp(1)` = `0`. We can initialize our `dp` array values to 0 to implicitly set this base case. As you'll see soon, other problems will have more complicated base cases.

3. Write a for-loop(s) that iterate over your state variables. If you have multiple state variables, you will need nested for-loops. These loops should **start iterating from the base cases and end at the answer state**.

4. Now, each iteration of the inner-most loop represents a given state, and is equivalent to a function call to the same state in top-down. Copy-paste the logic from your function into the for-loop and change the function calls to accessing your array. All `dp(...)` changes into `dp[...]`.

5. We're done! `dp` is now an array populated with the answer to the original problem for all possible states. Return the answer to the original problem, by changing `return dp(...)` to `return dp[...]`.



```py
def fn(arr, k):
    # 1. Initialize dp array (sized to state variables)
    # Using 'n' and 'k' as example dimensions
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # 2. Set base cases (if not already handled by initialization)
    # Example: dp[0][j] = some_value 

    # 3. Iterate over state variables
    # Start from base cases and move toward the target state
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            
            # 4. Copy-paste recurrence logic
            # Change dp(state) function calls to dp[state] lookups
            dp[i][j] = RECURRENCE_RELATION_LOGIC
            
    # 5. Return the final state
    return dp[n][k]
```

Changes made:

- Storage: Replaced the `memo` dictionary with a pre-allocated 2D array `dp`.
- Direction: Replaced recursion with nested `for` loops that build the solution from the "bottom" (simplest cases) "up" (final answer).
- Access: Instead of calling `dp(i, j)`, you now access `dp[i][j]`.

### Build a trie

```py
# note: using a class is only necessary if you want to store data at each node.
# otherwise, you can implement a trie using only hash maps.
class TrieNode:
    def __init__(self):
        # you can store data at nodes if you wish
        self.data = None
        self.children = {}

def fn(words):
    root = TrieNode()
    for word in words:
        curr = root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        # at this point, you have a full word at curr
        # you can perform more logic here to give curr an attribute if you want
    
    return root
```

### Dijkstra's algorithm

```py
from math import inf
from heapq import *

distances = [inf] * n
distances[source] = 0
heap = [(0, source)]

while heap:
    curr_dist, node = heappop(heap)
    if curr_dist > distances[node]:
        continue
    
    for nei, weight in graph[node]:
        dist = curr_dist + weight
        if dist < distances[nei]:
            distances[nei] = dist
            heappush(heap, (dist, nei))
```

## Stages of an interview

Most algorithmic interview rounds are between 45 - 60 minutes. The interviews can be broken down into stages, and at each stage, there are multiple things you should do to maximize your chances of success. Let's break it down.

### 1. Introductions

At the start of the interview, most of the time your interviewer will briefly introduce themselves and their role at the company, then ask you to introduce yourself.

- Prepare and rehearse a brief introduction of yourself. It should summarize your education, work experience, and interests in 30-60 seconds.
- Smile and speak with a confident voice.
- When the interviewer is talking about their work at the company, pay attention - it will help to ask questions about it later.
- If the interviewer mentioned anything that you are also interested in, whether it be their work or a hobby, mention it.

2. Problem statement

After introductions, your interviewer will give you a problem statement. If you're working in a shared text editor, they will most likely paste the problem description along with a test case into the editor, and then read the question to you.

- Make sure you fully understand the problem. After the interviewer has read the problem over, confirm what the problem is asking by paraphrasing it back to them.

- Ask clarifying questions regarding the input, for example:
    - Will the input only have integers, or could there be other types?
    - Will the input be sorted or unsorted?
    - Is the input guaranteed to have elements or could it be empty?
    - What should I do if an invalid input is given?

- Ask about the expected input size. Sometimes, the interviewer will be vague, but if they do give you a range, it can be a clue. For example, if `n` is very small, it is likely backtracking. If `n` is around `100 - 1000`, an `O(n²)` solution might be optimal. If `n` is very large, then you might need to do better than `O(n)`.

- The interviewer will likely give you one or two example test cases. Quickly walk through one to confirm that you understand the problem.

> Asking clarifying questions not only helps you better understand the problem but also shows attention to detail and being considerate of things like edge cases.

3. Brainstorming DS&A

Try to figure out what data structure or algorithm is applicable. Break the problem down and try to find common patterns that you've learned. Figure out what the problem needs you to do, and think about what data structure or algorithm can accomplish it with a good time complexity.

Think out loud. It will show your interviewer that you are good at considering tradeoffs. If the problem involves looking at subarrays, then be vocal about considering a sliding window because every window represents a subarray. Even if you're wrong, the interviewer will still appreciate your thought process.

The best way to train this skill is to practice LeetCode problems.

> By thinking out loud, you also open the door for the interviewer to give you hints and point you in the right direction.

Once you have decided on what data structures/algorithms to use, you now need to construct your actual algorithm. Before coding, you should think of the rough steps of the algorithm, explain them to the interviewer, and make sure they understand and agree that it is a reasonable approach. Usually, if you are on the wrong path, they will subtly hint at it.

> It is **extremely** important that you are receptive to what the interviewer says at this stage. Remember: they know the optimal solution. If they are giving you a hint, it is because they want you to succeed. Don't be stubborn and be ready to explore the ideas they give you.

4. Implementation

Once you have come up with an algorithm and gotten the interviewer on board, it is time to start writing code.

- If you intend on using a library or module like Python's collections for example, make sure the interviewer is ok with it before importing it.
- As you implement, explain your decision-making. For example, if you are solving a graph problem, when you declare a set `seen`, explain that it is to prevent visiting the same node more than once, thus also preventing cycles.
- Write clean code. Every major programming language has a convention for how code should be written. Make sure you know the basics of the language that you plan to be using. Google provides a summary for all major languages. The most important sections are case conventions, indentations, spacing, and global variables.
- Avoid duplicated code. For example, if you are doing a DFS on a matrix, loop over a directions array `[(0, 1), (1, 0), (0, -1), (-1, 0)]` instead of writing the same logic 4 times for each direction. If you find yourself writing similar code in multiple places, consider creating a function or simplifying it with a loop.
- Don't be scared of using helper functions. They make your code more modular, which is very important in real software engineering. It might also make potential follow-ups easier.

Don't panic if you get stuck or realize that your original plan might not work. Communicate your concerns with your interviewer. It makes their life a lot harder if you are struggling in silence.

One strategy is to first implement a brute force solution **while acknowledging** that it is a suboptimal solution. Once it is completed, analyze each part of the algorithm, figure out what steps are "slow", and try to think about how it can be sped up. Engage your interviewer and include them in the discussion - they want to help.

5. Testing & debugging

Once you have finished coding, your interviewer will likely want to test your code. Depending on the company, there are a few different environments your interview might be taking place in:

- Built-in test cases, code is run
    - These platforms are similar to LeetCode. There will be a wide variety of test cases - small inputs, huge inputs, inputs that test edge cases.
    - This environment puts the most stress on your code because a non-perfect solution will be exposed.
    However, it also puts the least stress on creating your own tests, since they are already built-in.

- Write your own test cases, code is run
    - These platforms are usually shared text editors that support running code. The interviewer will want you to write your own test cases.
    - To actually test the code, you should write in the outermost scope of the code, wherever the code will get run first. Assuming you solved the problem in a function (like on LeetCode), you can call your function with the test cases you wrote and print the results to the console.
    - When writing your own tests, make sure to try a variety. Include edge cases, intuitive inputs, and possibly invalid inputs (if the interviewer wants you to handle that case).

- Write your own test cases, code is not run
    - These platforms will just be shared text editors that do not support running code. The interviewer will want you to write your own test cases and walk through them manually.
    - To "test" the code, you will have to go through the algorithm manually with each test case. Try to condense trivial parts - for example, if you're creating a prefix sum, don't literally walk through the for loop with every element. Say something along the lines of "after this for loop, we will have a prefix sum which will look like ...".
    - As you are walking through the code, write (in the editor, outside your function somewhere) the variables used in the function and continuously update them.

Regardless of the scenario, if it turns out your code has an error, don't panic! If the environment supports running code, put print statements in relevant locations to try to identify the issue. Walk through a test case manually (as you would if you have an environment without runtime support) with a small test case. As you do it, talk about what the expected values of the variables should be and compare them with what they actually are. Again, the more vocal you are, the easier it is for the interviewer to help you.

6. Explanations and follow-ups

After coding the algorithm and running through test cases, be prepared to answer questions regarding your algorithm. Questions you should always expect and be ready for include:

- What is the time and space complexity of the algorithm?
    - You should speak in terms of the worst-case scenario. However, if the worst case is rare and the average case has a significantly faster runtime, you should also mention this.
- Why did you choose to do ...?
    - This could be your choice of data structure, choice of algorithm, choice of for loop configurations, etc. Be prepared to explain your thought process.
- Do you think that the algorithm could be improved in terms of time or space complexity?
    - If the problem needs to look at every element in the input (let's say the input isn't sorted and you needed to find the max element), then you probably can't do better than `O(n)`. Otherwise, you probably can't do better than `O(log n)`.
    - If the interviewer asks this, the answer is usually yes. Be careful about asserting that your algorithm is optimal - it's ok to be wrong, but it's not ok to be confidently wrong.

If there is time remaining in the interview, you may be asked an entirely new question. In that case, restart from step 2 (Problem statement). However, you may also be asked follow-ups to the question you already solved. The interviewer might introduce new constraints, ask for an improved space complexity, or any other number of things.

> This section is why it is important to actually understand solutions and not just memorize them.

7. Outro

The interviewer will usually reserve a few minutes at the end of the interview to allow you to ask questions about them or the company. You will rarely be able to improve the outcome of the interview at this point, but you can certainly make it worse.

Interviews are a two-way street. You should use this time as an opportunity to also get to know the company and see if you would like to work there. You should prepare some questions before the interview, such as:

- What does an average day look like?
- Why did you decide to join this company instead of another one?
- What is your favorite and least favorite thing about the job?
- What kind of work can I expect to work on?

All big companies will have their own tech blog. A great way to demonstrate your interest in the company is to read some blog posts and compile a list of questions regarding why the company makes the decisions they do.

Be interested, keep smiling, listen to the interviewer's responses, and ask follow-up questions to show that you understand their answers.

If you don't have quality questions or appear bored/uninterested, it could give a bad signal to the interviewer. It doesn't matter how well you did on the technical portion if the interviewer doesn't like you in the end.


