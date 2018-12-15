function weekTemps() {
    this.dataStore = (function() {
        var arr = [];
        for (let i = 0; i < 12; ++i) {
            arr.push([]);
        }
        return arr;
    })();
    this.add = add;
    this.average = average;
}


function add(month, temp) {
    this.dataStore[month-1].push(temp);
}

function average(month) {
    var total = 0;
    for (let i = 0; i < this.dataStore[month-1].length; ++i) {
        total += this.dataStore[month-1][i];
    }
    return total / this.dataStore[month-1].length;
}

var thisWeek = new weekTemps();
thisWeek.add(1, 59);
thisWeek.add(2, 30);
thisWeek.add(3, 40);
thisWeek.add(1, 21);
thisWeek.add(2, 44);
thisWeek.add(3, 48);
console.log(thisWeek.average(1));