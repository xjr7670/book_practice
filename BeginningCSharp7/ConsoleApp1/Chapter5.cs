using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using static System.Console;
using static System.Convert;

namespace ConsoleApp1
{
    enum orientaiton : byte
    {
        north = 1,
        south = 2,
        east = 3,
        west = 4
    }
    class Chapter5
    {
        public static void Ch05Ex01()
        {
            short shortResult, shortVal = 4;
            int integerVal = 67;
            long longResult;
            float floatVal = 10.5F;
            double doubleResult, doubleVal = 99.999;
            string stringResult, stringVal = "17";
            bool boolVal = true;
            WriteLine("Variable Conversion Examples\n");
            doubleResult = floatVal * shortVal;
            WriteLine($"Implicit, -> double: {floatVal} * {shortVal} -> { doubleResult }");
            shortResult = (short)floatVal;
            WriteLine($"Explicit, -> short: {floatVal} -> {shortResult}");
            stringResult = Convert.ToString(boolVal) + Convert.ToString(doubleVal);
            WriteLine($"Explicit, -> string: \"{boolVal}\" + \"{doubleVal}\" -> " + $"{stringResult}");
            longResult = integerVal + ToInt64(stringVal);
            WriteLine($"Mixed, -> long: {integerVal} + {stringVal} -> {longResult}");
        }

        public static void Ch05Ex02()
        {
            byte directionByte;
            string directionString;
            orientaiton myDirection = orientaiton.north;
            WriteLine($"myDirection = {myDirection}");
            directionByte = (byte)myDirection;
            directionString = Convert.ToString(myDirection);
            WriteLine($"byte equivalent = {directionByte}");
            WriteLine($"string equivalent = {directionString}");        
        }

        public static void Ch05Ex03()
        {
            string[] friendNames = { "Todd Anthony", "Kevin Holton",
                                    "Shane Laigle"};
            WriteLine($"Here are {friendNames.Length} of my friends:");
            foreach(string name in friendNames)
            {
                WriteLine($"{name}");
            }
        }
    }
}
