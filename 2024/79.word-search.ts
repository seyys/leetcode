/*
 * @lc app=leetcode id=79 lang=typescript
 *
 * [79] Word Search
 */

// @lc code=start
function exist(board: string[][], word: string): boolean {
  const letters: { [key in string]: number[][] } = {};
  const DIRECTIONS = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];

  for (let row = 0; row < board.length; row++) {
    for (let col = 0; col < board[0].length; col++) {
      if (board[row][col] in letters) {
        letters[board[row][col]].push([row, col]);
      } else {
        letters[board[row][col]] = [[row, col]];
      }
    }
  }

  function dfs(word: string, seen: number[][]) {
    if (word.length === 0) {
      return true;
    }
    const ch = word[0];

    const lastCoords = seen.at(-1);
    let potentialCoords: number[][] = [];
    if (lastCoords) {
      DIRECTIONS.forEach((dir) => {
        let [row, col] = lastCoords;
        row += dir[0];
        col += dir[1];
        if (
          row < 0 ||
          col < 0 ||
          row > board.length - 1 ||
          col > board[0].length - 1
        ) {
          return;
        }
        if (
          board[row][col] === ch &&
          !seen.some((coord) => coord[0] === row && coord[1] === col)
        ) {
          potentialCoords.push([row, col]);
        }
      });
    } else {
      potentialCoords = letters[ch] ?? [];
    }

    if (potentialCoords.length === 0) {
      return false;
    }

    return potentialCoords.some((coords) =>
      dfs(word.slice(1), [...seen, coords]),
    );
  }

  return dfs(word, []);
}
// @lc code=end
