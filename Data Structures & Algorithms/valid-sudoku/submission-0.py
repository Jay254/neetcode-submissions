class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create sets to track seen numbers in rows, columns, and sub-boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue  # Skip empty cells
                
                # Calculate the box index
                box_index = (r // 3) * 3 + (c // 3)
                
                # Check if the number is already in the row, column, or box
                if num in rows[r] or num in cols[c] or num in boxes[box_index]:
                    return False
                
                # Add the number to the sets for the row, column, and box
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)
        
        return True  # No duplicates found, the board is valid