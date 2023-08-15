using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Timers;
using Ch11CardLib;
using Ch13CardClient;
using static System.Console;
using Microsoft.CSharp.RuntimeBinder;

namespace ConsoleApp1
{
    public class Chapter13
    {
        public static void Ch13Ex01()
        {
            Deck deck1 = new Deck();
            try 
            {
                Card myCard = deck1.GetCard(60);
            } 
            catch (CardOutOfRangeException e) 
            {
                WriteLine(e.Message);
                WriteLine(e.DeckContents[0]);
            } 
        }

        static int counter = 0;
        static string displayString = "This string will appear one letter at a time.";
        public static void Ch13Ex02()
        {
            Timer myTimer = new Timer(100);
            myTimer.Elapsed += new ElapsedEventHandler(WriteChar);
            myTimer.Start();
            System.Threading.Thread.Sleep(200);
        }
        static void WriteChar(object source, ElapsedEventArgs e)
        {
            Write(displayString[counter++ % displayString.Length]);
        }

        public static void Ch13Ex03()
        {
            Connection myConnection = new Connection();
            Display myDisplay = new Display();
           // myConnection.MessageArrived += new MessageHandler(myDisplay.DisplayMessage);
            myConnection.Connect();
        }

        public static void Ch13Ex04()
        {
            Connection myConnection1 = new Connection();
            myConnection1.Name = "First connection.";
            Connection myConnection2 = new Connection();
            myConnection2.Name = "Second connection.";
            Display myDisplay = new Display();
            myConnection1.MessageArrived += myDisplay.DisplayMessage;
            myConnection2.MessageArrived += myDisplay.DisplayMessage;
            myConnection1.Connect();
            myConnection2.Connect();
            System.Threading.Thread.Sleep(200);
        }

        public static void Ch13Ex05()
        {
            WriteLine("BejaminCards: a new and exciting card game.");
            WriteLine("To win you  must have 7 cards of the same suit in your hand.");
            WriteLine();
            // Prompt for number of players.
            bool inputOK = false;
            int choice = -1;
            do
            {
                WriteLine("How many players (2-7)?");
                string input = ReadLine();
                try
                {
                    /// Attempt to convert input into a valid number of players.
                    choice = Convert.ToInt32(input);
                    if ((choice >= 2) && (choice <= 7))
                    {
                        inputOK = true;
                    }
                }
                catch
                {
                    // Ignore failed conversions, just continue prompting.
                }
            } while (inputOK == false);
            // Initialize array of player objects.
            Player[] players = new Player[choice];
            // Get player names.
            for (int p = 0; p < players.Length; p++)
            {
                WriteLine($"Player {p+1}, enter your name:");
                string playerName = ReadLine();
                players[p] = new Player(playerName);
            }
            // Start game.
            Game newGame = new Game();
            newGame.SetPlayers(players);
            int whoWon = newGame.PlayGame();
            // Display winning players.
            WriteLine($"{players[whoWon].Name} has won the game!");
            
        }

        public static void Ch13Ex06()
        {
            Type classType = typeof(DecoratedClass);
            object[] customAttributes = classType.GetCustomAttributes(true);
            foreach (object customAttribute in customAttributes)
            {
                WriteLine($"Attribute of type {customAttribute} found.");
                DoesInterestingThingsAttrubute interestingAttribute = customAttribute as DoesInterestingThingsAttrubute;
                if (interestingAttribute != null)
                {
                    WriteLine($"This class does {interestingAttribute.WhatDoesItDo} x {interestingAttribute.HowManyTimes}!");
                }
            }
        }

        public static void Ch13Ex07()
        {
            Farm<Animal> farm = new Farm<Animal>
            {
                new Cow("Lea"),
                new Chicken("Noa"),
                new Chicken("chicken2"),
                new SuperCow("Andrea")
            };
            farm.MakeANoise();
            
        }

        public static void Ch13Ex08()
        {
            var animals = new[]
            {
                new { Name = "Benjamin", Age = 42, Weight = 185 },
                new { Name = "Benjamin", Age = 42, Weight = 185 },
                new { Name = "Andrea", Age = 46, Weight = 109 }
            };
            WriteLine(animals[0].ToString());
            WriteLine(animals[0].GetHashCode());
            WriteLine(animals[1].GetHashCode());
            WriteLine(animals[2].GetHashCode());
            WriteLine(animals[0].Equals(animals[1]));
            WriteLine(animals[0].Equals(animals[2]));
            WriteLine(animals[0] == animals[1]);
            WriteLine(animals[0] == animals[2]);
        }

        public static void Ch13Ex09()
        {
            Ch13Ex06Class.Ch13Ex06();
        }

        public static void Ch13Ex10()
        {
            string sentence = "his gaze against the sweeping bars has grown so weary";
            List<string> words;
            words = WordProcessor.GetWords(sentence);
            WriteLine("Original sentence: ");
            foreach (string word in words)
            {
                Write(word);
                Write(' ');
            }
            WriteLine('\n');
            
            words = WordProcessor.GetWords(
                sentence,
                reverseWords: true,
                capitalizeWords: true);
            WriteLine("Capitalized sentence with reversed words: ");
            foreach (string word in words)
            {
                Write(word);
                Write(' ');
            }
        }

        public static void Ch13Ex11()
        {
            WriteLine("f(a, b) = a + b: ");
            Ch13Ex08Class.PerformOperations((paramA, paramB) => paramA + paramB);
            WriteLine();
            WriteLine("f(a, b) = a * b: ");
            Ch13Ex08Class.PerformOperations((paramA, paramB) => paramA + paramB);
            WriteLine();
            WriteLine("f(a, b) = (a - b) % b: ");
            Ch13Ex08Class.PerformOperations((paramA, paramB) => (paramA - paramB) % paramB);
        }

        public static void Ch13Ex12()
        {
            string[] people = { "Donna", "Mary", "Andrea" };
            WriteLine(people.Aggregate(
                (a, b) => a + " " + b));
            WriteLine(people.Aggregate<string, int>(
                0,
                (a, b) => a + b.Length));
            WriteLine(people.Aggregate<string, string, string>(
                "Some people: ",
                (a, b) => a + " " + b,
                a => a));
            WriteLine(people.Aggregate<string, string, int>(
                "Some people: ",
                (a, b) => a + " " + b,
                a => a.Length));
        }
    }

    // public delegate void MessageHandler(string messageText);
    public class Connection
    {
        /// public event MessageHandler MessageArrived;
        public event EventHandler<MessageArrivedEventArgs> MessageArrived;
        public string Name { get; set; }
        private Timer pollTimer;
        public Connection()
        {
            pollTimer = new Timer(100);
            pollTimer.Elapsed += new ElapsedEventHandler(CheckForMessage);
        }
        public void Connect() => pollTimer.Start();
        public void Disconnect() => pollTimer.Stop();
        private static Random random = new Random();
        private void CheckForMessage(object source, ElapsedEventArgs e)
        {
            WriteLine("Checking for new messages.");
            if ((random.Next(9) == 0) && (MessageArrived != null))
            {
                MessageArrived(this, new MessageArrivedEventArgs("Hello Mami!"));
            }
        }
    }

    public class Display
    {
        public void DisplayMessage(object source, MessageArrivedEventArgs e)
        {
            WriteLine($"Message arrived from: {((Connection)source).Name}");
            WriteLine($"Message Text: {e.Message}");
        }
    }

    public class MessageArrivedEventArgs : EventArgs
    {
        private string message;
        public string Message
        {
            get { return message; }
        }
        public MessageArrivedEventArgs() => message = "No message sent.";
        public MessageArrivedEventArgs(string newMessage) => message = newMessage;
    }

    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Method, AllowMultiple = false)]
    class DoesInterestingThingsAttrubute : Attribute
    {
        public DoesInterestingThingsAttrubute(int howManyTimes)
        {
            HowManyTimes = howManyTimes;
        }
        public string WhatDoesItDo { get; set; }
        public int HowManyTimes { get; set; }
        
    }

    [DoesInterestingThingsAttrubute(1000, WhatDoesItDo = "voodoo")]
    public class DecoratedClass {}

    class MyClass1
    {
        public int Add(int var1, int var2) => var1 + var2;
    }
    class MyClass2 {}

    class Ch13Ex06Class
    {
        static int callCount = 0;
        static dynamic GetValue()
        {
            if (callCount++ == 0)
            {
                return new MyClass1();
            }
            return new MyClass2();
        }

        public static void Ch13Ex06() {
            try
            {
                dynamic firstResult = GetValue();
                dynamic secondResult = GetValue();
                WriteLine($"firstResult is {firstResult.ToString()}");
                WriteLine($"secondResult is {secondResult.ToString()}");
                WriteLine($"firstResult call: {firstResult.Add(2, 3)}");
                WriteLine($"secondResult call: {secondResult.Add(2, 3)}");
            }
            catch (RuntimeBinderException ex)
            {
                WriteLine(ex.Message);
            }
        }
    }

    public static class WordProcessor
    {
        public static List<string> GetWords(
            string sentence,
            bool capitalizeWords = false,
            bool reverseOrder = false,
            bool reverseWords = false)
        {
            List<string> words = new List<string>(sentence.Split(' '));
            if (capitalizeWords) 
            {
                words = CapitalizeWords(words);
            }
            if (reverseOrder)
            {
                words = ReverseOrder(words);
            }
            if (reverseWords)
            {
                words = ReverseWords(words);
            }
            return words;
        }

        private static List<string> CapitalizeWords(List<string> words)
        {
            List<string> capitalizeWords = new List<string>();
            foreach (string word in words)
            {
                if (word.Length == 0)
                {
                    continue;
                }
                if (word.Length == 1)
                {
                    capitalizeWords.Add(word[0].ToString().ToUpper());
                }
                else
                {
                    capitalizeWords.Add(word[0].ToString().ToUpper() + word.Substring(1));
                }

            }
            return capitalizeWords;
        }

        private static List<string> ReverseOrder(List<string> words)
        {
            List<string> reversedWords = new List<string>();
            for (int wordIndex = words.Count - 1; wordIndex >= 0; wordIndex--)
            {
                reversedWords.Add(words[wordIndex]);
            }
            return reversedWords;
        }

        private static List<string> ReverseWords(List<string> words)
        {
            List<string> reversedWords = new List<string>();
            foreach (string word in words)
            {
                reversedWords.Add(ReverseWord(word));
            }
            return reversedWords;
        }

        private static string ReverseWord(string word)
        {
            StringBuilder sb = new StringBuilder();
            for (int characterIndex = word.Length - 1; characterIndex >= 0; characterIndex--)
            {
                sb.Append(word[characterIndex]);
            }
            return sb.ToString();
        }

    }

    delegate int TwoIntegerOperationDelegate(int paramA, int paramB);
    class Ch13Ex08Class
    {
        public static void PerformOperations(TwoIntegerOperationDelegate del)
        {
            for (int paramAVal = 1; paramAVal <= 5; paramAVal++)
            {
                for (int paramBVal = 1; paramBVal <= 5; paramBVal++)
                {
                    int delegateCallResult = del(paramAVal, paramBVal);
                    Write($"f({paramAVal}, {paramBVal})={delegateCallResult}");
                    if (paramBVal != 5)
                    {
                        Write(", ");
                    }
                }
                WriteLine();
            }
        }
    }
}
