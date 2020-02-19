import java.util.LinkedList;

/*
 * @lc app=leetcode.cn id=707 lang=java
 *
 * [707] 设计链表
 *
 * https://leetcode-cn.com/problems/design-linked-list/description/
 *
 * algorithms
 * Medium (23.42%)
 * Likes:    113
 * Dislikes: 0
 * Total Accepted:    14.1K
 * Total Submissions: 59K
 * Testcase Example:  '["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]\r\n[[],[1],[3],[1,2],[1],[1],[1]]\r'
 *
 * 设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next
 * 是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。
 * 
 * 在链表类中实现这些功能：
 * 
 * 
 * get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
 * addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
 * addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
 * addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index
 * 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
 * deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
 * 
 * 
 * 
 * 
 * 示例：
 * 
 * MyLinkedList linkedList = new MyLinkedList();
 * linkedList.addAtHead(1);
 * linkedList.addAtTail(3);
 * linkedList.addAtIndex(1,2);   //链表变为1-> 2-> 3
 * linkedList.get(1);            //返回2
 * linkedList.deleteAtIndex(1);  //现在链表是1-> 3
 * linkedList.get(1);            //返回3
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 所有val值都在 [1, 1000] 之内。
 * 操作次数将在  [1, 1000] 之内。
 * 请不要使用内置的 LinkedList 库。
 * 
 * 
 */

// @lc code=start
public class ListNode {
    int val;
    ListNode next;
    ListNode prev;
    ListNode(int val) { this.val = val; }
  }
  
class MyLinkedList {
int size;
// sentinel nodes as pseudo-head and pseudo-tail
ListNode head, tail;
public MyLinkedList() {
    size = 0;
    head = new ListNode(0);
    tail = new ListNode(0);
    head.next = tail;
    tail.prev = head;
}

public int get(int index) {
    if (index < 0 || index >= size) return -1;

    ListNode curr;
    if (index + 1 < size - index){
      curr = head;
      for(int i = 0; i < index + 1; ++i) curr = curr.next;
    } else {
      curr = tail;
      for(int i = 0; i < size - index; ++i) curr = curr.prev;
    }
    return curr.val;
}

public void addAtHead(int val) {
    ListNode pred = head, succ = head.next;

    ++size;
    ListNode toAdd = new ListNode(val);
    toAdd.prev = pred;
    toAdd.next = succ;
    pred.next = toAdd;
    succ.prev = toAdd;
}

public void addAtTail(int val) {
    ListNode succ = tail, pred = tail.prev;

    ++size;
    ListNode toAdd = new ListNode(val);
    toAdd.prev = pred;
    toAdd.next = succ;
    pred.next = toAdd;
    succ.prev = toAdd;
}

public void addAtIndex(int index, int val) {
    if (index > size) return;

    if (index < 0) index = 0;

    ListNode pred, succ;
    if (index < size - index) {
    pred = head;
    for(int i = 0; i < index; ++i) pred = pred.next;
    succ = pred.next;
    }
    else {
    succ = tail;
    for (int i = 0; i < size - index; ++i) succ = succ.prev;
    pred = succ.prev;
    }

    ++size;
    ListNode toAdd = new ListNode(val);
    toAdd.prev = pred;
    toAdd.next = succ;
    pred.next = toAdd;
    succ.prev = toAdd;
}

public void deleteAtIndex(int index) {
    if (index < 0 || index >= size) return;

    ListNode pred, succ;
    if (index < size - index) {
    pred = head;
    for(int i = 0; i < index; ++i) pred = pred.next;
    succ = pred.next.next;
    }
    else {
    succ = tail;
    for (int i = 0; i < size - index - 1; ++i) succ = succ.prev;
    pred = succ.prev.prev;
    }

    --size;
    pred.next = succ;
    succ.prev = pred;
}
}
  


// @lc code=end

