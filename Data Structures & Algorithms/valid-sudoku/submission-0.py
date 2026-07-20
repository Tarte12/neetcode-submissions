class Solution:

  def isValidSudoku(self, board: List[List[str]]) -> bool:

    # 1. 행(Row) 검사
    for i in range(9):
      row = [x for x in board[i] if x != '.']
      if len(row) != len(set(row)):
        return False

    # 2. 열(Column) 검사
    for j in range(9):
      col = [board[i][j] for i in range(9) if board[i][j] != '.']
      if len(col) != len(set(col)):
        return False

    # 3. 3x3 박스 검사
    for r in range(0, 9, 3):
      for c in range(0, 9, 3):
        box = []
        for dr in range(3):
          for dc in range(3):
            val = board[r + dr][c + dc]
            if val != '.':
              box.append(val)

        if len(box) != len(set(box)):
          return False

    return True