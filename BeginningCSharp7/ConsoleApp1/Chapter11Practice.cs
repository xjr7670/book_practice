using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Chapter11Practice
    {
    }

    class People : DictionaryBase, ICloneable
    {
        public void Add(Person person)
        {
            Dictionary.Add(person.Name, person);
        }

        public void remove(string name)
        {
            Dictionary.Remove(name);
        }

        public Person this[string name]
        {
            get { return (Person)Dictionary[name]; }
            set { Dictionary[name] = value; }
        }

        public Person[] getOldest()
        {
            Person oldestPerson = null;
            People oldestPeople = new People();
            Person currentPerson;
            foreach (DictionaryEntry p in Dictionary) 
            {
                currentPerson = p.Value as Person;
                if (oldestPerson == null)
                {
                    oldestPerson = currentPerson;
                    oldestPeople.Add(oldestPerson);
                }
                else 
                {
                    if (currentPerson > oldestPerson)
                    {
                        oldestPeople.Clear();
                        oldestPeople.Add(currentPerson);
                        oldestPerson = currentPerson;
                    }
                    else 
                    {
                        if (currentPerson >= oldestPerson)
                        {
                            oldestPeople.Add(currentPerson);
                        }
                    }
                }
            }
            Person[] oldestPeopleArray = new Person[oldestPeople.Count];
            int copyIndex = 0;
            foreach (DictionaryEntry p in oldestPeople)
            {
                oldestPeopleArray[copyIndex] = p.Value as Person;
                copyIndex++;
            }
            return oldestPeopleArray;
        }

        public object Clone()
        {
            Person currentPerson, newPerson;
            People people = new People();
            foreach (DictionaryEntry p in Dictionary)
            {
                currentPerson = p.Value as Person;
                newPerson = new Person();
                newPerson.Age = currentPerson.Age;
                newPerson.Name = currentPerson.Name;
                people.Add(newPerson);
            }
            return people;
        }

        public IEnumerable Ages
        {
            get
            {
                foreach (object person in Dictionary.Values)
                {
                    yield return (person as Person).Age;
                }
            }
        }
    }

    public class Person
    {
        private string name;
        private int age;
        public string Name
        {
            get { return name; }
            set { name = value; }
        }
        public int Age
        {
            get { return age; }
            set { age = value; }
        }

        public static bool operator <(Person p1, Person p2) => p1.age < p2.age;
        public static bool operator >(Person p1, Person p2) => p1.age > p2.age;
        public static bool operator <=(Person p1, Person p2) => p1.age <= p2.age;
        public static bool operator >=(Person p1, Person p2) => p1.age >= p2.age;


    }
}
