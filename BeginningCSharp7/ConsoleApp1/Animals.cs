using System.Collections;
using System.Collections.Generic;
using System.Text;

namespace ConsoleApp1
{
    public class Animals : CollectionBase
    {
        public void Add(Animal newAnimal) => List.Add(newAnimal);

        public void Remove(Animal newAnimal) => List.Remove(newAnimal);

        public Animal this[int animalIndex]
        {
            get { return (Animal)List[animalIndex]; }
            set { List[animalIndex] = value; }
        }
    }
}