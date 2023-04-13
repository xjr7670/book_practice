import scala.io.Source
import java.io.FileWriter

object Practice2 {
  def main(args: Array[String]) {
    val tabFile = "tabfile.txt"
    val src = Source.fromFile(tabFile, "UTF-8")
    val fileStr = src.mkString
    val void = "    "
    val pat = """\t""".r
    val newStr = pat.replaceAllIn(fileStr, void)
    src.close()

    val writer = new FileWriter(tabFile)
    writer.write(newStr)
    writer.close()
  }
}

      

