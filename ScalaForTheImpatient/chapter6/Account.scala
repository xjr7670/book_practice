class Account private (val id: Int, initialBalance: Double) {
    val id = Account.newUniqueNumber()
    private var balance = initialBalance
    def deposit(amount: Double) {
        balance += amount
    }
}

object Account {
    private var lastNumber = 0
    private def newUniqueNumber() = {
        lastNumber += 1;
        lastNumber
    }

    def apply(initialBalance: Double) = {
        new Account(newUniqueNumber(), initialBalance)
    }
}