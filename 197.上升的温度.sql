--
-- @lc app=leetcode.cn id=197 lang=mysql
--
-- [197] 上升的温度
--

-- @lc code=start
# Write your MySQL query statement below
SELECT b.Id
FROM Weather as a,Weather as b
WHERE a.Temperature < b.Temperature and DATEDIFF(a.RecordDate,b.RecordDate) = -1;


-- @lc code=end

