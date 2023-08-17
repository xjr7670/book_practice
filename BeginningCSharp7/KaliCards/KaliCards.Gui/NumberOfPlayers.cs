using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace KaliCards.Gui
{
    public class NumberOfPlayers : ObservableCollection<int>
    {
        public NumberOfPlayers() : base()
        {
            Add(2);
            Add(3);
            Add(4);
        }
    }
}
