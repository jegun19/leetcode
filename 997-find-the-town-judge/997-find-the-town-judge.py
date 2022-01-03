class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        length = len(trust)
        if length == 1 and n == 1:
            return -1
        
        elif length == 0 and n == 1:
            return 1
        
        else:
            # Construct dictionary of votes
            vote_dict = {}
            for i in range(0, length):
                target = trust[i][1]
                if target not in vote_dict:
                    vote_dict[target] = 1
                else:
                    vote_dict[target] += 1
                
            # Check how many votes each person got
            for which in vote_dict:
                
                # Check if the person which got the most vote voted for someone else
                if vote_dict[which] == n - 1:
                    for k in range(0, length):
                        
                        # Return -1 if that person voted
                        if trust[k][0] == which:
                            return -1
                        
                    # Return that person if that person didn't vote for somebody else
                    return which
                
            return -1