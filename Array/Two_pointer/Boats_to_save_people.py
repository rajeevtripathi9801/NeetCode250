from typing import List 

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        result = 0
        l, r = 0, len(people) - 1

        while l <= r:
            remain = limit - people[r]
            r-= 1
            result+= 1

            if l<=r and remain >= people[l]:
                l+= 1
        
        return result

"""
## Step 1: Sort the Array
[1, 3, 2, 3]  --->[1, 2, 3, 3]

We use two pointers:
left  → lightest person
right → heaviest person

Initial State:
left = 0  (weight = 1)
right = 3 (weight = 3)
boats = 0
--
## Iteration 1
Try pairing:
1 + 3 = 4 > 3 ❌
Can not pair.
Heaviest person goes alone.
Boat 1 → [3]

Update:
right = 2
boats = 1

Remaining people:
[1, 2, 3]

---

## Iteration 2

left = 0 (1)
right = 2 (3)

Try pairing:
1 + 3 = 4 > 3 ❌

Cannot pair.
Heaviest goes alone.

Boat 2 → [3]

Update:
right = 1
boats = 2

Remaining people:
[1, 2]

---

## Iteration 3

left = 0 (1)
right = 1 (2)

Try pairing:
1 + 2 = 3 ≤ 3 ✅

Valid pair.

Boat 3 → [1, 2]

Update:
left = 1
right = 0
boats = 3

Pointers crossed → stop.

---

## Final Boats

Boat 1 → [3]  
Boat 2 → [3]  
Boat 3 → [1, 2]

---

## Final Answer

Minimum boats required = **3**

---"""
if __name__=="__main__":
    obj = Solution()
    nums = [1, 2]
    limit = 3
    result = obj.numRescueBoats(nums, limit)
    print(result)