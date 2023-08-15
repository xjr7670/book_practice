using static System.Console;

namespace ConsoleApp1
{
    public class Chicken : Animal
    {
        public override void MakeANoise()
        {
            WriteLine($"{name} says 'cluck!';");
        }
        public void LayEgg() => WriteLine($"{name} has laid an egg.");
        public Chicken(string newName) : base(newName) {}
    }
}