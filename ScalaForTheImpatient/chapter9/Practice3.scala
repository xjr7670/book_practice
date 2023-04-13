import scala.io.Source

object Practice3 {
  def main(args: Array[String]) {
    val fname = "longlineword.txt"
    val lineArr = Source.fromFile(fname, "UTF-8").getLines.toArray
    for (item <- lineArr) {
      if (item.length > 8) {
        println(item)
      }
    }
    // 一行搞掂
    // for (item <- Source.fromFile("longlineword.txt", "UTF-8").getLines.toArray if item.length > 8) println(item)
  }
}
