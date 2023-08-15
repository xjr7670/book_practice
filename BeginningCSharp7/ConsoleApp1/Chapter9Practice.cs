using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Vehicle;

namespace ConsoleApp1
{
    class Chapter9Practice
    {
        static void AddPassenger(IPassengerCarrier carrier)
        {
            System.Console.WriteLine($"{carrier.ToString()} add a passenger");
        }
        
        public static void Practice5()
        {
            Compact compact = new Compact();
            SUV suv = new SUV();
            PassengerTrain passengerTrain = new PassengerTrain();
            AddPassenger(compact);
            AddPassenger(suv);
            AddPassenger(passengerTrain);
        }
    }
}
