using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;
using Ch10CardLib;

namespace Ch10CardClient
{
    class Program
    {
        static void Main(string[] args)
        {
            Ch10Practice5();
           // ReadKey();
        }

        static void Ch10Practice5()
        {
            Deck myDeck = new Deck();
            myDeck.Shuffle();
            Card[] cards = new Card[5];
            cards[0] = myDeck.GetCard(0);
            Suit suit = cards[0].suit;
            bool theSame = true;

            for(int i = 1; i < 52; i++)
            {
                WriteLine(myDeck.GetCard(i).ToString());


                if (i % 5 == 0) // current round ended
                {
                    WriteLine();
                    if (theSame)
                    {
                        foreach (Card card in cards)
                        {
                            WriteLine(card.ToString());
                        }
                        WriteLine("Flush!");
                        break;
                    }
                    theSame = true;
                    
                    suit = myDeck.GetCard(i).suit;
                }

                cards[i % 5] = myDeck.GetCard(i);
                if (!suit.Equals(myDeck.GetCard(i).suit))
                {
                    theSame = false;
                }

                if (i == 50)
                {
                    WriteLine("No Flush!");
                    break;
                }        
            } 
        }
    }
}
