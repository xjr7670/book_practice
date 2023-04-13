// 题 4

class Point (x: Int, y: Int) {
    private var x1 = x
    private var y1 = y

    override def toString(): String = {
        s"Point($x1, $y1)"
    }
}

object Point {
    def apply(x: Int, y: Int) = {
        new Point(x, y)
    }
}

object Test {
    def main(args: Array[String]): Unit = {
        val p = Point(3, 4)
        println(p)
    }
}