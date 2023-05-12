import scala.io.Source


object Practice1 {
  def main(args: Array[String]): Unit = {
    val filename = "./myfile.txt"
    val source = Source.fromFile(filename, "UTF-8")
    val lineArr = source.getLines.toArray
    val newLines = lineArr.reverse
    source.close()

    val out = new java.io.PrintWriter(filename)
    for (i <- 0 until newLines.length-1) {
      out.println(newLines(i))
    }
    out.close()
  }
}

