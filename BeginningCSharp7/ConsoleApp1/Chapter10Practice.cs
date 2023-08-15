using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Chapter10MyClass
    {
        protected string myString;
        public string ContainedString
        {
            set { myString = value; }
        }
        public virtual string GetString()
        {
            return myString;
        }
    }

    class MyDerivedClass : Chapter10MyClass
    {
        public override string GetString()
        {
            return base.GetString() + "(output from derived class)";
        }
    }

    class MyCopyableClass
    {
        public int count = 40;
        public MyCopyableClass GetCopy()
        {
            return (MyCopyableClass) MemberwiseClone();
        }
    }

    public class Practice10Client
    {
        public static void Practice4()
        {
            MyCopyableClass copyableClass1 = new MyCopyableClass();
            
            MyCopyableClass copyableClass2 = copyableClass1.GetCopy();


            System.Console.WriteLine($"copyableClass1.count = {copyableClass1.count}");
            System.Console.WriteLine($"copyableClass2.count = {copyableClass2.count}");

            copyableClass1.count = 48;

            System.Console.WriteLine("after...\n");

            System.Console.WriteLine($"copyableClass1.count = {copyableClass1.count}");
            System.Console.WriteLine($"copyableClass2.count = {copyableClass2.count}");
        }
    }
}
