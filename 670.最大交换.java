/*
 * @lc app=leetcode.cn id=670 lang=java
 *
 * [670] 最大交换
 */

// @lc code=start
class Solution {
    public int maximumSwap(int num) {
        char[] chars1 = String.valueOf(num).toCharArray();//方便获取数字长度
        int length = chars1.length;

        int[] numArr = new int[length];
        int[] lastLoc = new int[10];
        Arrays.fill(lastLoc,-1);
        boolean flag = true;

        for(int i=length-1; i>=0; i--)
        {
            numArr[i] = chars1[i]-'0';
            if(lastLoc[numArr[i]] == -1)
                lastLoc[numArr[i]] = i;
        }

        for(int i=0; i<length; i++)
        {
            int thisNum = numArr[i];
            for(int k=9; k>thisNum; k--)
            {
                if(lastLoc[k] != -1 && lastLoc[k]>i)
                {
                    flag = false;
                    int temp = numArr[i];
                    numArr[i] = k;
                    numArr[lastLoc[k]] = temp;
                }
                if(!flag)
                    break;
            }
            if(!flag)
                    break;
        }
        return transfer(numArr);

    }

    //int数组转int
    public int transfer(int[] arr){
        String str = "";
        for(int i=0; i<arr.length; i++){
            String s = new String();
            int z = arr[i];
            s = Integer.toString(z);
            str = str.concat(s);
        }
        int num = Integer.parseInt(str);
        return num;
    }
}
// @lc code=end



