public class Duck {
    private int size;
    public static void main(String[] args) {
        System.out.println("Size of duck is " + getSize());
    }

    public void setSize(int s) {
        size = s;
    }

    public int getSize() {
        return size;
    }
}