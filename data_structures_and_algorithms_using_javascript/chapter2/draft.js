// var nums = [1, 2, 3, 7, 10, 8, 9];
// function square(num) {
//     console.log(num, num * num);
// }
// nums.forEach(square);

// var names = ["David", "Mike", "Cynthia", "Clayton", "Bryan", "Raymond"];
// names.sort();
// console.log(names);

// function isEven(num) {
//     return num % 2 == 0;
// }

// var nums = [2, 4, 6, 8, 10];
// var even = nums.every(isEven);
// var someEven = nums.some(isEven);
// if (someEven) {
//     console.log("some numbers are even");
// } else {
//     console.log("no numbers are even");
// }
// nums = [1, 3, 5, 7, 9];
// someEven = nums.some(isEven);
// if (someEven) {
//     console.log("some numbers are even");
// } else {
//     console.log("no numbers are even");
// }

// function add(runningTotal, currentValue) {
//     return runningTotal + currentValue;
// }
// nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
// var sum = nums.reduce(add);
// console.log(sum);

// var words = ["the ", "quick ", "brown ", "fox "];
// var sentence = words.reduce(add);
// console.log(sentence);
// sentence = words.reduceRight(add);
// console.log(sentence);

// function curve(grade) {
//     return grade += 5;
// }

// var grades = [77, 65, 81, 92, 83];
// var newgrades = grades.map(curve);
// console.log(newgrades);

// function first(word) {
//     return word[0];
// }

// var words = ["for", "your", "information"];
// var acronym = words.map(first);
// console.log(acronym.toString());

// function isEven(num) {
//     return num % 2 == 0;
// }

// function isOdd(num) {
//     return num % 2 != 0;
// }

// var nums = [];
// for (var i = 0; i < 20; ++i) {
//     nums[i] = i + 1;
// }
// var evens = nums.filter(isEven);
// console.log("Even numbers: ");
// console.log(evens);

// var odds = nums.filter(isOdd);
// console.log("Odd numbers: ");
// console.log(odds);

// function passing(num) {
//     return num >= 60;
// }

// var grades = [];
// for (let i = 0; i < 20; ++i) {
//     grades[i] = Math.floor(Math.random() * 101);
// }
// var passGrades = grades.filter(passing);
// console.log("All grades: ");
// console.log(grades);
// console.log("Passing grades: ");
// console.log(passGrades);

// function afterc(str) {
//     if (str.indexOf("cie") > -1) {
//         return true;
//     }
//     return false;
// }

// var words = ["recieve", "deceive", "percieve", "deceit", "concieve"];
// var misspelled = words.filter(afterc);
// console.log(misspelled);

/*************************** 2.6 二维和多维数组 **************************/

/************ 2.6.1 创建二维数据 ***************/
// var twod = [];
// var rows = 5;
// for (let i = 0; i < rows;  ++i) {
//     twod[i] = [];
// }

// Array.matrix = function(numrows, numcols, initial) {
//     var arr = [];
//     for (let i = 0; i < numrows; ++i) {
//         let columns = [];
//         for (let j = 0; j < numcols; ++j) {
//             columns[j] = initial;
//         }
//     arr[i] = columns;
//     }
//     return arr;
// }

// var nums = Array.matrix(5, 5, "");
// console.table(nums);
// nums[1][2] = "Joe";
// console.table(nums);

/************ 2.6.2 处理二维数组的元素 ***************/

// var grades = [[89, 77], [76, 82, 81], [91, 94, 89, 99]];
// var total = 0;
// var average = 0.0;
// for (let row = 0; row < grades.length; ++row) {
//     for (let col = 0; col < grades[row].length; ++col) {
//         total += grades[row][col];
//     }
//     average = total / grades[row].length;
//     console.log("Student " + parseInt(row+1) + " average: " + average.toFixed(2));
//     total = 0;
//     average = 0.0;
// }
// for (let col = 0; col < grades.length; ++col) {
//     for (let row = 0; row < grades[col].length; ++row) {
//         total += grades[row][col];
//     }

//     average = total / grades[col].length;
//     console.log("Test " + parseInt(col+1) + " average: " + average.toFixed(2));
//     total = 0;
//     average = 0.0;    
// }

/************ 2.7 对象数组 ***************/

// function Point(x, y) {
//     this.x = x;
//     this.y = y;
// }

// function displayPts(arr) {
//     for (let i = 0; i < arr.length; ++i) {
//         console.log(arr[i].x + ", " + arr[i].y);
//     }
// }

// var p1 = new Point(1, 2);
// var p2 = new Point(3, 5);
// var p3 = new Point(2, 8);
// var p4 = new Point(4, 4);
// var points = [p1, p2, p3, p4];
// for (let i = 0; i < points.length; ++i) {
//     console.log("Point " + parseInt(i+1) + ": " + points[i].x + ", " + points[i].y);
// }
// var p5 = new Point(12, -3);
// points.push(p5);
// console.log("after push: ");
// displayPts(points);
// points.shift()
// console.log("After shift: ");
// displayPts(points);

/************ 2.8 对象中的数组 ***************/

function weekTemps() {
    this.dataStore = [];
    this.add = add;
    this.average = average;
}

function add(temp) {
    this.dataStore.push(temp);
}

function average() {
    var total = 0;
    for (let i = 0; i < this.dataStore.length; ++i) {
        total += this.dataStore[i];
    }
    return total / this.dataStore.length;
}

var thisWeek = new weekTemps();
thisWeek.add(52);
thisWeek.add(55);
thisWeek.add(61);
thisWeek.add(65);
thisWeek.add(55);
thisWeek.add(50);
thisWeek.add(52);
thisWeek.add(49);
console.log(thisWeek.average());
