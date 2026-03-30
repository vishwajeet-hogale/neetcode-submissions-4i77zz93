class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        n =  len(people)
        i, j = 0, n - 1
        boats = 0
        nums = people.copy()
        while i <= j:
            boats += 1
            if i< j and nums[i] + nums[j] <= limit:
                
                i += 1
                j -= 1
                continue

            if j >=0 and nums[j] <= limit:
                # boats += 1
                j -= 1
                continue

            if i<n and nums[i] <= limit:
                # boats += 1
                i += 1
                continue

            

        return boats

             
        