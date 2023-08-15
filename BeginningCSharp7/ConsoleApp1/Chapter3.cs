using System;

namespace ConsoleApp1
{
    class Chapter3
    {
        public static void Practice5()
        {
            int a, b, c, d;
            Console.WriteLine("Please enter number1: ");
            a = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Please enter number2: ");
            b = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Please enter number3: ");
            c = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Please enter number4: ");
            d = Convert.ToInt32(Console.ReadLine());

            int times = a * b * c * d;
            Console.Write($"Times of these 4 numbers is: {times}");

        }
    }
}
