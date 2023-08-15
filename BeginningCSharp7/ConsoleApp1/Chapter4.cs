using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using static System.Console;
using static System.Convert;

namespace ConsoleApp1
{
    class Chapter4
    {
        public static void Ch04Ex01() 
        {
            WriteLine("Enter an integer: ");
            int myInt = ToInt32(ReadLine());
            bool isLessThan10 = myInt < 10;
            bool isBetween0And5 = (0 <= myInt) && (myInt <= 5);
            WriteLine($"Integer less than 10? {isLessThan10}");
            WriteLine($"Integer between 0 and 5? {isBetween0And5}");
            WriteLine($"Exactly one of the above is true? " +
                      $"{isLessThan10 ^ isBetween0And5}");
        }

        public static void Ch04Ex02() 
        {
            string comparison;
            WriteLine("Enter a number: ");
            double var1 = ToDouble(ReadLine());
            WriteLine("Enter another number: ");
            double var2 = ToDouble(ReadLine());

            if (var1 < var2) 
            {
                comparison = "less than";
            } 
            else 
            {
                if(var1 == var2)
                {
                    comparison = "equal to";
                }
                else
                {
                    comparison = "greater than";
                }
            }
            WriteLine($"The first number is {comparison} " +
                      $"the second number.");
        }

        public static void Ch04Ex04()
        {
            double balance, interestRate, targetBalance;
            WriteLine("What is your current balance?");
            balance = ToDouble(ReadLine());
            WriteLine("What is your current annual interest rate (in %)?");
            interestRate = 1 + ToDouble(ReadLine()) / 100.0;
            WriteLine("What balance would you like to have?");
            targetBalance = ToDouble(ReadLine());
            int totalYears = 0;
            while (balance < targetBalance)
            {
                balance *= interestRate;
                ++totalYears;
            }
            WriteLine($"In {totalYears} year{(totalYears == 1 ? "": "")} " +
                      $"you'll have a balance of {balance}.");
            if (totalYears == 0) {
                WriteLine("To be honest, you really don't need to use this calculator.");
            }
        }
    }
}
