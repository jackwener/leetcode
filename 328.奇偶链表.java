/*
 * @lc app=leetcode.cn id=328 lang=java
 *
 * [328] 奇偶链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode oddEvenList(ListNode head) {
        if(head == null) return null;
        
        ListNode even_head = new ListNode(-1);
        ListNode even_cur = even_head;

        ListNode cur = head;

        while(cur.next != null && cur.next.next != null){
            even_cur.next = cur.next;
            cur.next = cur.next.next;
            even_cur.next.next = null;

            even_cur = even_cur.next;
            cur = cur.next;
        }

        if(cur.next != null){
            even_cur.next = cur.next;
            even_cur.next.next = null;
        }
        
        cur.next = even_head.next;

        return head;
    }
}
// @lc code=end

