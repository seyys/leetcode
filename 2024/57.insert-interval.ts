/*
 * @lc app=leetcode id=57 lang=typescript
 *
 * [57] Insert Interval
 */

// @lc code=start
function insert(intervals: number[][], newInterval: number[]): number[][] {
  let isInserted = false;
  for (let i = 0; i < intervals.length; i++) {
    if (intervals[i][0] > newInterval[0]) {
      intervals = [
        ...intervals.slice(0, i),
        newInterval,
        ...intervals.slice(i),
      ];
      isInserted = true;
      break;
    }
  }
  
  if (!isInserted) {
    intervals.push(newInterval);
  }

  const result: number[][] = [intervals[0]];

  for (let i = 1; i < intervals.length; i++) {
    if (result[result.length - 1][1] >= intervals[i][0]) {
      result[result.length - 1][1] = Math.max(
        result[result.length - 1][1],
        intervals[i][1],
      );
    } else {
      result.push(intervals[i]);
    }
  }

  return result;
}
// @lc code=end
