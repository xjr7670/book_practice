object PrintReverse extends App {
    if (args.length == 0) {
        println("You haven't enter any letter")
    } else if (args.length == 1) {
        println(args(0))
    } else {
        println(args.reverse.mkString(" "))
    }
}