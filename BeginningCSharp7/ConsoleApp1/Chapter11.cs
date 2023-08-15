using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;
using Ch11CardLib;

namespace ConsoleApp1
{
    public abstract class Animal
    {
        public abstract void MakeANoise();
        protected string name;
        public string Name
        {
            get { return name ;}
            set { name = value;}
        }
        public Animal() => name = "The animal with no name";

        public Animal(string newName) => name = newName;

        public void Feed() => WriteLine($"{name} has been fed.");
    }

    public class Primes
    {
        private long min;
        private long max;
        public Primes() : this(2, 100) {}
        public Primes(long minimum, long maximum)
        {
            if (minimum < 2)
            {
                min = 2;
            }
            else 
            {
                min = minimum;
            }
            max = maximum;
        }

        public IEnumerator GetEnumerator()
        {
            for (long possiblePrime = min; possiblePrime <= max; possiblePrime++)
            {
                bool isPrime = true;
                for (long possibleFactor = 2; possibleFactor <= (long)Math.Floor(Math.Sqrt(possiblePrime)); possibleFactor++)
                {
                    long remainderAfterDivision = possiblePrime % possibleFactor;
               
                    if (remainderAfterDivision == 0)
                    {
                        isPrime = false;
                        break;
                    }
                }
                if (isPrime)
                {
                    yield return possiblePrime;
                }
            }
            
        }
    }

    public class Chapter11
    {
        public static void Ch11Ex01()
        {
            WriteLine("Create an Array type collection of Animal objects ans use it:");
            Animal[] animalArray = new Animal[2];
            Cow myCow1 = new Cow("Lea");
            animalArray[0] = myCow1;
            animalArray[1] = new Chicken("Noa");
            foreach (Animal myAnimal in animalArray)
            {
                WriteLine($"New {myAnimal.ToString()} object added to Array collection, Name = {myAnimal.Name}");
            }
            WriteLine($"Array collection contains {animalArray.Length} objects");
            animalArray[0].Feed();
            ((Chicken) animalArray[1]).LayEgg();
            WriteLine();
            WriteLine("Create an ArrayList type collection of Animal objects and use it.");
            ArrayList animalArrayList = new ArrayList();
            Cow myCow2 = new Cow("Donna");
            animalArrayList.Add(myCow2);
            animalArrayList.Add(new Chicken("Andrea"));
            foreach (Animal myAnimal in animalArrayList)
            {
                WriteLine($"New {myAnimal.ToString()} object added to ArrayList collection, Name = {myAnimal.Name}");
            }
            WriteLine($"ArrayList collection contains {animalArrayList.Count} objects");
            ((Animal) animalArrayList[0]).Feed();
            ((Chicken) animalArrayList[1]).LayEgg();
            WriteLine();
            WriteLine("Additional manipulation of ArrayList:");
            animalArrayList.RemoveAt(0);
            ((Animal) animalArrayList[0]).Feed();
            animalArrayList.AddRange(animalArray);
            ((Chicken)animalArrayList[2]).LayEgg();
            WriteLine($"The animal called {myCow1.Name} is at index {animalArrayList.IndexOf(myCow1)}");
            myCow1.Name = "Mary";
            WriteLine($"The animal is now called {((Animal)animalArrayList[1]).Name}.");
        }

        public static void Ch11Ex02()
        {
            Animals animalCollection = new Animals();
            animalCollection.Add(new Cow("Donna"));
            animalCollection.Add(new Chicken("Mary"));
            foreach (Animal myAnimal in animalCollection)
            {
                myAnimal.Feed();
            }
        }

        public static void Ch11Ex03()
        {
            Primes primesFrom2To1000 = new Primes(2, 1000);
            foreach (long i in primesFrom2To1000)
            {
                Write($"{i} ");
                
            }
        }

        public static void Ch11CardClient()
        {
            Deck deck1 = new Deck();
            Deck deck2 = (Deck)deck1.Clone();
            WriteLine($"The first card in the original deck is: {deck1.GetCard(0)}");
            WriteLine($"The first card in the cloned deck is: {deck2.GetCard(0)}");
            deck1.Shuffle();
            WriteLine("Original deck shuffled.");
            WriteLine($"The first card in the original deck is: {deck1.GetCard(0)}");
            WriteLine($"The first card in the cloned deck is: {deck2.GetCard(0)}");
            
        }
    }
}
