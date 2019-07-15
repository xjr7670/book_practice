public class Load {
    private double annualInterestRate;
    private int numberOfYears;
    private double loadAmount;
    private java.util.Date loadDate;

    /** Default construct */
    public Load() {
        this(2.5, 1, 1000);
    }

    /** Construct a load with specified annual interest rate,
     *  number of years, and load amount
     */
    public Load(double annualInterestRate, int numberOfYears, double loadAmount) {
        this.annualInterestRate = annualInterestRate;
        this.numberOfYears = numberOfYears;
        this.loadAmount = loadAmount;
        loadDate = new java.util.Date();
    }

    /** Return annualInterestRate */
    public double getAnnualInterestRate() {
        return annualInterestRate;
    }

    /** Set a new annualInterestRate */
    public void setAnnualInterestRate(double annualInterestRate) {
        this.annualInterestRate = annualInterestRate;
    }

    /** Return numberOfYears */
    public int getNumberOfYears() {
        return numberOfYears;
    }

    /** Set a new numberOfYears */
    public void setNumberOfYears(int numberOfYears) {
        this.numberOfYears = numberOfYears;
    }

    /** Return loadAmount */
    public double getLoadAmount() {
        return loadAmount;
    }

    /** Set a new loadAmount */
    public void setLoadAmount(double loadAmount) {
        this.loadAmount = loadAmount;
    }

    /** Find monthly payment */
    public double getMonthlyPayment() {
        double monthlyInterestRate = annualInterestRate / 1200;
        double monthlyPayment = loadAmount * monthlyInterestRate / (1 -
            (1 / Math.pow(1 + monthlyInterestRate, numberOfYears * 12)));
        
        return monthlyPayment;
    }

    /** Find total payment */
    public double getTotalPayment() {
        double totalPayment = getMonthlyPayment() * numberOfYears * 12;
        return totalPayment;
    }

    /** Return load date */
    public java.util.Date getLoadDate() {
        return loadDate;
    }
}