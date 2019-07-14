/**
 * 练习题9.9 － 正 n 边形
 */

class RegularPolygen {
    private int n = 3;
    private double side = 1;
    private double x = 0;
    private double y = 0;

    public RegularPolygen(int n, double side, double x, double y) {
        this.n = n;
        this.side = side;
        this.x = x;
        this.y = y;
    }

    public RegularPolygen(int n, double side) {
        this(n, side, 0, 0);
    }

    public RegularPolygen() {
        this(3, 1, 0, 0);
    }

    public int getN() {
        return this.n;
    }

    public double getSide() {
        return this.side;
    }

    public double getX() {
        return this.x;
    }

    public double getY() {
        return this.y;
    }

    public void setN(int n) {
        this.n = n;
    }

    public void setSide(double side) {
        this.side = side;
    }

    public void setX(double x) {
        this.x = x;
    }

    public void setY(double y) {
        this.y = y;
    }

    // 返回周长
    public double getPerimeter() {
        return this.n * this.side;
    }

    // 返回面积
    public double getArea() {
        return (this.n * Math.pow(this.side, 2)) / (4 * Math.tan(Math.PI / this.n));
    }
}