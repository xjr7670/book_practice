class BankAccount(initialBalance: Double) {
  private var balance = initialBalance
  def currentBalance = balance
  def deposit(amount: Double) = { balance += amount; balance }
  def withdraw(amount: Double) = { balance -= amount; balance }
}

class CheckingAccount(initialBalance: Double) extends BankAccount(initialBalance: Double) {
  
  private var balance = initialBalance
  override def deposit(amount: Double) = {
    balance += amount - 1
    balance
  }

  def getBalance = balance

  override def withdraw(amount: Double) = {
    balance -= amount - 1
    balance
  }
}

object Test {
  def main(args: Array[String]) {
    val ca = new CheckingAccount(100)
    ca.deposit(4)
    println(ca.getBalance)
    ca.withdraw(5)
    println(ca.getBalance)
  }
}
