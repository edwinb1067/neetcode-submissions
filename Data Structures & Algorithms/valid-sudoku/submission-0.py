class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # We use a dictionary where the key is the index (0-8) 
        # and the value is a set of numbers seen in that row/col/box
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set) # Key will be (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val == ".":
                    continue
                
                # Check if value already exists in current row, column, or 3x3 box
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in boxes[(r // 3, c // 3)]):
                    return False
                
                # Add the value to the respective sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r // 3, c // 3)].add(val)
                
        return True