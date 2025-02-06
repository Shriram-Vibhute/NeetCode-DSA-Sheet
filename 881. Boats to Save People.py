class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        counter = 0
        while left <= right:
            remain = limit - people[right]
            right -= 1
            counter += 1
            if people[left] <= remain and left <= right:
                left += 1
        return counter