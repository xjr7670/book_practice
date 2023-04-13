package com.horstmann.impatient

package object people {
  val defaultName = "John Q. Public"
}

package people {
  class Person {
    var name = defaultName
  }
}
