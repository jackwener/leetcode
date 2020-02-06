--
-- @lc app=leetcode.cn id=183 lang=mysql
--
-- [183] 从不订购的客户
--

-- @lc code=start
# Write your MySQL query statement below
select a.Name as Customers
from Customers as a
left join Orders as b
on a.Id=b.CustomerId
where b.CustomerId is null;

-- @lc code=end

