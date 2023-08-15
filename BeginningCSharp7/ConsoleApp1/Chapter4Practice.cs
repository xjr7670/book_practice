using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using static System.Console;
using static System.Convert;

namespace ConsoleApp1
{
    class Chapter4Practice
    {
        public static void Practice4_2()
        {
            double var1, var2;

            while (true)
            {
                WriteLine("Please enter number one: ");
                var1 = ToDouble(ReadLine());
                WriteLine("Please enter number two: ");
                var2 = ToDouble(ReadLine());
                if (var1 > 10 && var2 > 10) 
                {
                    WriteLine("Please make sure both two numbers are less than 10.");
                    continue;
                }
                else
                {
                    break;
                }
            }
            WriteLine($"var1 + var2 = {var1 + var2}");
        }
        
    }
}
