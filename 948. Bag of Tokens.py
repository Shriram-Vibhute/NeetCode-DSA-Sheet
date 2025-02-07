class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # Sorting
        tokens.sort()

        # Variables
        i, j = 0, len(tokens) - 1
        score = 0

        # Looping
        while i < j:
            if power >= tokens[i]:
                score += 1
                power -= tokens[i]
                i += 1
            elif score > 0:
                score -= 1
                power += tokens[j]
                j -= 1
            else:
                i += 1
        
        # Edge Case
        if i == j and power >= tokens[i]:
                score += 1
                i += 1
    
        return score