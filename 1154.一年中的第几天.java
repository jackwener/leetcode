/*
 * @lc app=leetcode.cn id=1154 lang=java
 *
 * [1154] 一年中的第几天
 */

// @lc code=start
class Solution {
    public int dayOfYear(String date) {
          int[] arr = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        String[] split = date.split("-");
        
        int day = Integer.parseInt(split[2]);
        
        int month = Integer.parseInt(split[1]);
        
        if (isLeapYear(split[0]) && month > 2) {
            day += 1;
        }
        for (int i = 0; i < month - 1; i++) {
            day += arr[i];
        }
        return day;

    }
      private boolean isLeapYear(String stringYear) {
        int year = Integer.parseInt(stringYear);
        return (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0));
    }
}

// @lc code=end

