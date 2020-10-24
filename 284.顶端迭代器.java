/*
 * @lc app=leetcode.cn id=284 lang=java
 *
 * [284] 顶端迭代器
 */

// @lc code=start
// Java Iterator interface reference:
// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html

// Java Iterator interface reference:
// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html

class PeekingIterator implements Iterator<Integer> {
    private Iterator<Integer> iterator;
    private Integer curr;
    
	public PeekingIterator(Iterator<Integer> iterator) {
        this.iterator = iterator;
	    curr = iterator.hasNext() ? iterator.next(): null;
	}
	
    // Returns the next element in the iteration without advancing the iterator.
	public Integer peek() {
        return curr;
	}
	
	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	@Override
	public Integer next() {
	    int res = curr;
        curr = iterator.hasNext() ? iterator.next(): null;
        return res;
	}
	
	@Override
	public boolean hasNext() {
	    return curr != null;
	}
}

// @lc code=end

