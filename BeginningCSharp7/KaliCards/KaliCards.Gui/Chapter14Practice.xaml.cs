using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;

namespace KaliCards.Gui
{
    /// <summary>
    /// Interaction logic for Chapter14Practice.xaml
    /// </summary>
    public partial class Chapter14Practice : Window
    {
        private PresistentSlider _sliderData = new PresistentSlider
        {
            MinValue = 1,
            MaxValue = 200,
            CurrentValue = 100
        };
        
        public Chapter14Practice()
        {
            DataContext = _sliderData;
            InitializeComponent();
        }
    }
}
