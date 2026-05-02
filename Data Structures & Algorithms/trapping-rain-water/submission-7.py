class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        left = 0
        right = len(height) - 1
        
        # Track the maximum heights seen so far, not their indices
        max_left = height[left]
        max_right = height[right]
        
        total_water = 0
        
        while left < right:
            # We process the side with the smaller maximum boundary
            if max_left < max_right:
                left += 1
                # Update max_left if we find a taller bar
                max_left = max(max_left, height[left])
                # Add trapped water (if height[left] is the new max, this adds 0)
                total_water += max_left - height[left]
            else:
                right -= 1
                # Update max_right if we find a taller bar
                max_right = max(max_right, height[right])
                # Add trapped water
                total_water += max_right - height[right]
                
        return total_water