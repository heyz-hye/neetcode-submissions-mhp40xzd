class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        neet = sorted(nums)
        gist = []

        for index, i in enumerate(neet):
            # Skip duplicates for the fixed number 'i'
            if index > 0 and i == neet[index - 1]:
                continue
                
            left = index + 1
            right = len(neet) - 1
            
            # Correct condition: stop before pointers cross
            while left < right:
                 # Calculate the total sum of all three elements
                 total_sum = i + neet[left] + neet[right]
                 
                 if total_sum > 0:
                    # Sum is too big, decrease the right side
                    right -= 1
                 elif total_sum < 0:
                    # Sum is too small, increase the left side
                    left += 1
                 else: # total_sum == 0
                    gist.append([i, neet[left], neet[right]])
                    
                    # Move BOTH pointers to find the next valid pair for this 'i'
                    left += 1
                    right -= 1
                    
                    # Skip duplicates for the 'left' pointer
                    while left < right and neet[left] == neet[left - 1]:
                        left += 1
                        
        return gist