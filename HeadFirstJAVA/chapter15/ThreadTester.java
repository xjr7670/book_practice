class ThreadTester {
    public static void main(String[] args) {
        Runnable threadJob = new MyRunnable();
        Thread myThread = new Thread(threadJob);

        myThread.start();
        try {
            myThread.sleep(2000);
        } catch (InterruptedException ex) {
            System.out.println("user interrupted!");
            ex.printStackTrace();
        }
        
        System.out.println("back in main");
    }
}