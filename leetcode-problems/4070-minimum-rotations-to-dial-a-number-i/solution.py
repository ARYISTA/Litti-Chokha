class Solution:
    def minRotations(self, s: str) -> int:
        total_rotations = 0
        current_digit = 0  
        
        for char in s:
            target_digit = int(char)
            
            
            diff = abs(target_digit - current_digit)
            rotations = min(diff, 10 - diff)
            
            total_rotations += rotations
            current_digit = target_digit  
            
        return total_rotations