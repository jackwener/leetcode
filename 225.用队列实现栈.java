import java.util.LinkedList;
import java.util.Queue;

/*
 * @lc app=leetcode.cn id=225 lang=java
 *
 * [225] 用队列实现栈
 */

// @lc code=start
//单队列实现
/*复杂度：入栈O(1)，pop和top为O(n) 或者 入栈O(n)，pop和top为O(1)
 *取决于头size个值放到尾部的代码段放在哪
 */
class MyStack {
    Queue<Integer> queue;

    public MyStack() {
        queue = new LinkedList<>();
    }

    public void push(int x) {
        queue.add(x);
    }

    public int pop() {
        return shift();
    }

    private int shift() {
        int size = queue.size();
        while (size-- > 1) {
            // 精髓：暂存大小,再将头size个值放到尾部
            queue.add(queue.poll());
        }
        return queue.poll();
    }

    public int top() {
        int peek = shift();
        // 放回队列
        queue.add(peek);
        return peek;
    }

    public boolean empty() {
        return queue.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */
// @lc code=end

