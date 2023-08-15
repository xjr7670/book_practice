using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;
using Ch09ClassLib;

namespace ConsoleApp1
{
    public abstract class MyBase {}
    internal class MyClass : MyBase 
    {
        public int val;
    }
    public interface IMyBaseInterface {}
    internal interface IMyBaseInterface2 {}
    internal interface IMyInterface : IMyBaseInterface, IMyBaseInterface2 {}
    internal sealed class MyComplexClass : MyClass, IMyInterface {}

    struct myStruct
    {
        public int val;
    }

    class Chapter9
    {
        public static void Ch09Ex01()
        {
            MyComplexClass myObj = new MyComplexClass();
            WriteLine(myObj.ToString());
        }

        public static void Ch09Ex02()
        {
            MyExternalClass myObj = new MyExternalClass();
            WriteLine(myObj.ToString());
        }

        public static void Ch09Ex03()
        {
            MyClass objectA = new MyClass();
            MyClass objectB = objectA;
            objectA.val = 10;
            objectB.val = 20;
            myStruct structA = new myStruct();
            myStruct structB = structA;
            structA.val = 30;
            structB.val = 40;
            WriteLine($"objectA.val = {objectA.val}");
            WriteLine($"objectB.val = {objectB.val}");
            WriteLine($"structA.val = {structA.val}");
            WriteLine($"structB.val = {structB.val}");
        }
    }
}
