class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for column in range(9):
                value = board[row][column]
                if value == '.':
                    continue
                elif value in rows[row] or value in columns[column] or value in boxes[(row//3, column//3)]:
                    return False

                rows[row].add(value)
                columns[column].add(value)
                boxes[(row//3, column//3)].add(value)

        return True