/*
 * @lc app=leetcode.cn id=23 lang=java
 *
 * [23] 合并K个排序链表
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
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists == null || lists.length == 0) return null;
        int left = 0; int right = lists.length - 1;
        while(right > 0) {
            while(left < right) {
                lists[left] = merge(lists[left], lists[right]);
                left++;
                right--;
            }
            left = 0;
        }
        return lists[0];
    }
    
    private ListNode merge(ListNode node1, ListNode node2) {
        ListNode head = new ListNode(0);
        ListNode pre = head;
        while(node1 != null && node2 != null) {
            if(node1.val < node2.val){
                pre.next = node1;
                node1 = node1.next;
                pre = pre.next;
            } else {
                pre.next = node2;
                node2 = node2.next;
                pre = pre.next;
            }
        }
        pre.next = node1 == null ? node2 : node1;
        return head.next;
    }
}

// @lc code=end

