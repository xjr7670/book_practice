package com.smart.basic;

public abstract class TransactionSynchronizationManager {
    // 1 用于保存每个事务线程对应的 Connection 或 Session 等类型的资源
    private static final ThreadLocal resources = new ThreadLocal();

    // 2 用于保存每个事务线程对应事务的名称
    private static final ThreadLocal currentTransactionName = new ThreadLocal();

    // 3 用于保存每个事务线程对应事务的 read-only 状态
    private static final ThreadLocal currentTransactionReadOnly = new ThreadLocal();

    // 4 用于保存每个事务线程对应事务的隔离级别
    private static final ThreadLocal currentTransactionIsolationLevel = new ThreadLocal();

    // 5 用于保存每个事务线程对应事务的激活态
    private static final ThreadLocal actualTransactionActive = new ThreadLocal();
}
