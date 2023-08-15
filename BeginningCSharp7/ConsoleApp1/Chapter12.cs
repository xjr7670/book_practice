using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Math;
using static System.Console;

namespace ConsoleApp1
{
    public class Chapter12
    {
        public static void Ch12Ex01()
        {
            Vector v1 = GetVector("vector1");
            Vector v2 = GetVector("vector1");
            WriteLine($"{v1} + {v2} = {v1 + v2}");
            WriteLine($"{v1} - {v2} = {v1 - v2}");
        }

        public static void Ch12Ex02()
        {
            List<Animal> animalCollections = new List<Animal>();
            animalCollections.Add(new Cow("Rual"));
            animalCollections.Add(new Chicken("Donna"));
            foreach (Animal animal in animalCollections)
            {
                animal.Feed();
            }
        }


        public static void Ch12Ex03()
        {
            Vectors route = new Vectors();
            route.Add(new Vector(2.0, 90.0));
            route.Add(new Vector(1.0, 180.0));
            route.Add(new Vector(0.5, 45.0));
            route.Add(new Vector(2.5, 315.0));
            WriteLine(route.Sum());
            Comparison<Vector> sorter = new Comparison<Vector>(VectorDelegates.Compare);
            route.Sort(sorter);
            WriteLine(route.Sum());
            Predicate<Vector> searcher = new Predicate<Vector>(VectorDelegates.TopRightQuadrant);
            Vectors topRightQuadrantRout = new Vectors(route.FindAll(searcher));
            WriteLine(topRightQuadrantRout.Sum());
            
        }

        public static void Ch12Ex04()
        {
            Farm<Animal> farm = new Farm<Animal>();
            farm.Animals.Add(new Cow("Rual"));
            farm.Animals.Add(new Chicken("Donna"));
            farm.Animals.Add(new Chicken("Mary"));
            farm.Animals.Add(new SuperCow("Ben"));
            farm.MakeANoise();
            Farm<Cow> dairyFarm = farm.GetCows();
            dairyFarm.FeedTheAnimals();
            foreach (Cow cow in dairyFarm)
            {
                if (cow is SuperCow)
                {
                    (cow as SuperCow).Fly();
                }
            }
        }

        static Vector GetVector(string name)
        {
            WriteLine($"Input {name} magnitude: ");
            double? r = GetNullableDouble();
            WriteLine($"Input {name} angle (in degrees): ");
            double? theta = GetNullableDouble();
            return new Vector(r, theta);
        }

        static double? GetNullableDouble()
        {
            double? result;
            string userInput = ReadLine();
            try
            {
                result = double.Parse(userInput);
            }
            catch
            {
                result = null;
            }
            return result;
        }
    }

    public class SuperCow : Cow
    {
        public void Fly()
        {
            WriteLine($"{name} is flying.");
        }
        public SuperCow(string newName) : base(newName)
        {

        }
        public override void MakeANoise()
        {
            WriteLine($"{name} says 'here I come to save the day!'");
        }
    }

    public class Farm<T> : IEnumerable<T> where T : Animal
    {
        public void Add(T animal) => animals.Add(animal);
        private List<T> animals = new List<T>();
        public List<T> Animals
        {
            get { return animals; }
        }
        public IEnumerator<T> GetEnumerator() => animals.GetEnumerator();
        IEnumerator IEnumerable.GetEnumerator() => animals.GetEnumerator();

        public void MakeANoise()
        {
            foreach (T animal in animals)
            {
                animal.MakeANoise();
            }
        }
        public void FeedTheAnimals()
        {
            foreach (T animal in animals)
            {
                animal.Feed();
            }
        }
        public Farm<Cow> GetCows()
        {
            Farm<Cow> cowFarm = new Farm<Cow>();
            foreach (T animal in animals)
            {
                if (animal is Cow)
                {
                    cowFarm.Animals.Add(animal as Cow);
                }
            }
            return cowFarm;
        }
    }

    public class Vector
    {
        public double? R = null;
        public double? Theta = null;
        public double? ThetaRadians
        {
            // Convert degrees to radians
            get { return (Theta * Math.PI / 180.0); }
        }
        public Vector(double? r, double? theta)
        {
            // Normalize.
            if (r < 0)
            {
                r = -r;
                theta += 180;
            }
            theta = theta % 360;
            // Assign fields.
            R = r;
            Theta = theta;
        }
        public static Vector operator +(Vector op1, Vector op2)
        {
            try
            {
                // Get(x, y) coordinates for new vector.
                double newX = op1.R.Value * Sin(op1.ThetaRadians.Value)
                    + op2.R.Value * Sin(op2.ThetaRadians.Value);
                double newY = op1.R.Value * Cos(op1.ThetaRadians.Value)
                    + op2.R.Value * Cos(op2.ThetaRadians.Value);
                // Convert to (r, theta).
                double newR = Sqrt(newX * newX + newY * newY);
                double newTheta = Atan2(newX, newY) * 180.0 / PI;
                // Return result.
                return new Vector(newR, newTheta);
            }
            catch
            {
                // Return "null" vector.
                return new Vector(null, null);
            }
        }
        public static Vector operator -(Vector op1) => new Vector(-op1.R, op1.Theta);
        public static Vector operator -(Vector op1, Vector op2) => op1 + (-op2);

        public static double? operator *(Vector op1, Vector op2)
        {
            try
            {
                double angleDiff = (double)(op2.ThetaRadians.Value - op1.ThetaRadians.Value);
                return op1.R.Value * op2.R.Value * Math.Cos(angleDiff);
            }
            catch
            {
                return null;
            }
        }

        public override string ToString()
        {
            // Get string representation of coordinates.
            string rString = R.HasValue ? R.ToString(): "null";
            string thetaString = Theta.HasValue ? Theta.ToString(): "null";
            // Return (r, theta) string
            return string.Format($"({rString}, {thetaString})");
        }
    }

    public class Vectors : List<Vector>
    {
        public Vectors()
        {
        }
        public Vectors(IEnumerable<Vector> initialItems)
        {
            foreach (Vector vector in initialItems)
            {
                Add(vector);
            }
        }
        public string Sum()
        {
            StringBuilder sb = new StringBuilder();
            Vector currentPoint = new Vector(0.0, 0.0);
            sb.Append("origin");
            foreach (Vector vector in this)
            {
                sb.AppendFormat($" + {vector}");
                currentPoint += vector;
            }
            sb.AppendFormat($" = {currentPoint}");
            return sb.ToString();
        }
    }

    public static class VectorDelegates
    {
        public static int Compare(Vector x, Vector y)
        {
            if (x.R > y.R)
            {
                return 1;
            }
            else if (x.R < y.R)
            {
                return -1;
            }
            return 0;
        }
        public static bool TopRightQuadrant(Vector target)
        {
            if (target.Theta >= 0.0 && target.Theta <= 90.0)
            {
                return true;
            }
            else 
            {
                return false;
            }
        }
    }
}
