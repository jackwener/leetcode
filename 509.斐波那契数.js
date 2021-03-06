/*
 * @lc app=leetcode.cn id=509 lang=javascript
 *
 * [509] 斐波那契数
 */

// @lc code=start
/**
 * @param {number} N
 * @return {number}
 */

// let fib = n => n <= 0 ? 0 : n == 1 ? 1 : fib(n - 2) + fib(n - 1)

let fib = n => {
    if (n == 0) return 0;
    let a1 = 0;
    a2 = 1;
    for (let i = 1; i < n; i++) {
        [a1, a2] = [a2, a1 + a2];
    }
    return a2;
}



// let fib = n => Math.round(
//     (Math.pow((1 + Math.sqrt(5)) / 2, n) -
//       Math.pow((1 - Math.sqrt(5)) / 2, n)) /
//      Math.sqrt(5)
//   );
// @lc code=end

