using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace KaliCards.Gui
{
    [Serializable]
    public class GameOptions
    {
        private ObservableCollection<string> playerNames = new ObservableCollection<string>();
        public List<string> SelectedPlayers { get; set; } = new List<string>();
        public bool playAgainstComputer = true;
        public int numberOfPlayers = 2;
        public ComputerSkillLevel computerSkill = ComputerSkillLevel.Dumb;

        public ObservableCollection<string> PlayerNames
        {
            get
            {
                return playerNames;
            }
            set
            {
                playerNames = value;
                OnPropertyChanged("PlayerNames");
            }
        }

        public void AddPlayers(string playerName)
        {
            if (playerNames.Contains(playerName))
            {
                return;
            }
            playerNames.Add(playerName);
            OnPropertyChanged("PlayerNames");
        }

        public int NumberOfPlayers
        {
            get { return numberOfPlayers; }
            set
            {
                numberOfPlayers = value;
                OnPropertyChanged(nameof(NumberOfPlayers));
            }
        }

        public bool PlayAgainstComputer
        {
            get { return playAgainstComputer; }
            set
            {
                playAgainstComputer = value;
                OnPropertyChanged(nameof(PlayAgainstComputer));
            }
        }

        public ComputerSkillLevel ComputerSkill
        {
            get { return computerSkill; }
            set
            {
                computerSkill = value;
                OnPropertyChanged(nameof(ComputerSkill));
            }
        }

        public event PropertyChangedEventHandler PropertyChanged;
        private void OnPropertyChanged(string propertyName)
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
        }
    }

    [Serializable]
    public enum ComputerSkillLevel
    {
        Dumb,
        Good,
        Cheats
    }
}
