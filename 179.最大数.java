import java.util.Comparator;

/*
 * @lc app=leetcode.cn id=179 lang=java
 *
 * [179] 最大数
 */

// @lc code=start
// class Solution {
    // private class NumberComparator implements Comparator<String>{
    //     @Override
    //     public int compare(String a, String b){
    //         return (b+a).compareTo(a+b);
    //     }
    // }

    // public String largestNumber(int[] nums) {
    //     String[] asStrs = new String[nums.length];
    //     for (int i = 0; i < nums.length; i++) {
    //         asStrs[i] = String.valueOf(nums[i]);
    //     }

    //     Arrays.sort(asStrs, new NumberComparator());

    //     if (asStrs[0].equals("0")) {
    //         return "0";
    //     }

    //     String largestNumberStr = new String();
    //     for (String numAsStr : asStrs) {
    //         largestNumberStr += numAsStr;
    //     }

    //     return largestNumberStr;
    // }
    
    
// }
class Solution {

    private StringBuilder res;

    public String largestNumber(int[] nums) {
        res = new StringBuilder();
        Arrays.stream(nums).boxed().map(x -> x.toString()).sorted((x, y) -> (y + x).compareTo(x + y)).forEach(x -> res.append(x));
        return res.charAt(0) == '0' ? "0" : res.toString();
    }
}
// @lc code=end

