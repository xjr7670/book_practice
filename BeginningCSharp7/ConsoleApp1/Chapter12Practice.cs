using System;
using System.Collections;
using System.Collections.Generic;
using static System.Console;


namespace ConsoleApp1
{
    public class ShortList<T> : IList<T>
    {
        protected IList<T> innerCollection;
        protected int maxSize = 10;
        public ShortList() : this(10) {}
        public ShortList(int size)
        {
            maxSize = size;
            innerCollection = new List<T>();
        }
        public ShortList(IEnumerable<T> list) : this(10, list) {}
        public ShortList(int size, IEnumerable<T> list)
        {
            maxSize = size;
            innerCollection = new List<T>(list);
            if (Count > maxSize)
            {
                ThrowTooManyItemsException();
            }
        }
        protected void ThrowTooManyItemsException()
        {
            throw new IndexOutOfRangeException(
                "Unable to add any more items; maximum size is " + maxSize.ToString() + " items.");
        }
        #region IList<T> Members
        public int IndexOf(T item) => innerCollection.IndexOf(item);
        public void Insert(int index, T item)
        {
            if (Count < maxSize)
            {
                innerCollection.Insert(index, item);
            }
            else
            {
                ThrowTooManyItemsException();
            }
        }
        public void RemoveAt(int index)
        {
            innerCollection.RemoveAt(index);
        }
        public T this[int index]
        {
            get
            {
                return innerCollection[index];
            }
            set
            {
                innerCollection[index] = value;
            }
        }
        #endregion
        #region Icollection<T> Members
        public void Add(T item)
        {
            if (Count < maxSize)
            {
                innerCollection.Add(item);
            }
            else
            {
                ThrowTooManyItemsException();
            }
        }
        public void Clear()
        {
            innerCollection.Clear();
        }
        public bool Contains(T item) => innerCollection.Contains(item);
        public void CopyTo(T[] array, int arrayIndex)
        {
            innerCollection.CopyTo(array, arrayIndex);
        }
        public int Count
        {
            get
            {
                return innerCollection.Count;
            }
        }
        public bool IsReadOnly
        {
            get
            {
                return innerCollection.IsReadOnly;
            }
        }
        public bool Remove(T item) => innerCollection.Remove(item);
        #endregion
        #region IEnumerable<T> Members
        public IEnumerator<T> GetEnumerator() => innerCollection.GetEnumerator();
        #endregion
        #region IEnumerable Members
        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
        #endregion
    }
}