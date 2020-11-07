import java.util.concurrent.CountDownLatch;

/*
 * @lc app=leetcode.cn id=1114 lang=java
 *
 * [1114] 按序打印
 */

// @lc code=start
class Foo {
    private CountDownLatch c2Latch;
    private CountDownLatch c3Latch;
    public Foo() {
        c2Latch = new CountDownLatch(1);
        c3Latch = new CountDownLatch(1);
    }

    public void first(Runnable printFirst) throws InterruptedException {
        printFirst.run();
        c2Latch.countDown();
    }

    public void second(Runnable printSecond) throws InterruptedException {
        c2Latch.await();
        printSecond.run();
        c3Latch.countDown();
    }

    public void third(Runnable printThird) throws InterruptedException {
        c3Latch.await();       
        printThird.run();
    }
}
// @lc code=end

