/*
 * @lc app=leetcode.cn id=1189 lang=golang
 *
 * [1189] “气球” 的最大数量
 */

// @lc code=start
func maxNumberOfBalloons(text string) int {
	dict := make(map[string]int)
	dict["b"] = 0
	dict["a"] = 0
	dict["l"] = 0
	dict["o"] = 0
	dict["n"] = 0
    for i:=0; i < len(text); i++{
        _ , ok := dict[text[i:i+1]]
		if(ok) {
			dict[text[i:i+1]] ++
		} 
    }
	dict["l"] /= 2
	dict["o"] /= 2
	return max(dict["b"],max(dict["a"],max(dict["l"],max(dict["o"],dict["n"]))))
}
func max(x, y int) int {
    if x < y {
        return x
    }
    return y
}
// @lc code=end

