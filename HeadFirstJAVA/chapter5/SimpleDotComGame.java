import java.util.concurrent.ThreadLocalRandom;

public class SimpleDotComGame {
    public static void main(String[] args) {
        int numOfGuesses = 0;
        GameHelper helper = new GameHelper();
        SimpleDotCom dot = new SimpleDotCom();
        int randomNum = ThreadLocalRandom.current().nextInt(0, 5);
        int[] locations = {randomNum, randomNum+1, randomNum+2};
        dot.setLocationCells(locations);
        boolean isAlive = true;

        while (isAlive == true) {
            String userGuess = helper.getUserInput("enter a number");
            String result = dot.checkYourself(userGuess);
            numOfGuesses++;

            if (result.equals("kill")) {
                isAlive = false;
                System.out.println("You took " + numOfGuesses + " guesses.");
            }
        }
    }
}