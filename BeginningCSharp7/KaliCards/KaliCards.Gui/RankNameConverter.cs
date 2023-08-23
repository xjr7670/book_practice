using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Data;


namespace KaliCards.Gui
{
 
    [ValueConversion(typeof(Ch13CardLib.Rank), typeof(string))]
    public class RankNameConverter : IValueConverter
    {
        public object Convert(object value, Type targetType, object parameter, System.Globalization.CultureInfo culture)
        {
            int source = (int)value;
            if (source == 1 || source > 10)
            {
                switch (source)
                {
                    case 1:
                        return "Ace";
                    case 11:
                        return "Jack";
                    case 13:
                        return "Queen";
                    default:
                        return DependencyProperty.UnsetValue;
                }
            }
            else
            {
                return source.ToString();
            }
        }
            
        public object ConvertBack(object value, Type targetType, object parameter, System.Globalization.CultureInfo culture)
        {
            return DependencyProperty.UnsetValue;
        }
    }

}
