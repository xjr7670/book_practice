// 散列表
function HashTable() {
    this.table = new Array(137);
    this.simpleHash = simpleHash;
    this.betterHash = betterHash;
    this.showDistro = showDistro;
    this.put = put;
    // this.get = get;
}

// 散列函数
function simpleHash(data) {
    var total = 0;
    for (let i = 0; i < data.length; ++i) {
        total += data.charCodeAt(i);   
    }
    return total % this.table.length;
}

// 更好的散列函数
function betterHash(string) {
    const H = 37;
    var total = 0;
    for (let i = 0; i < string.length; ++i) {
        total += H * total + string.charCodeAt(i);
    }
    total = total % this.table.length;
    if (total < 0) {
        total += this.table.length - 1;
    }
    return parseInt(total);
}

function put(key, data) {
    var pos = this.betterHash(key);
    this.table[pos] = data;
}

function showDistro() {
    var n = 0;
    for (let i = 0; i < this.table.length; ++i) {
        if (this.table[i] != undefined) {
            console.log(i + ": " + this.table[i]);
        }
    }
}

/******************* 散列化整型键 *************************/
function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function genStuData(arr) {
    for (let i = 0; i < arr.length; ++i) {
        var num = "";
        for (let j = 1; j <= 9; ++j) {
            num += Math.floor(Math.random() * 10);
        }
        num += getRandomInt(50, 100);
        arr[i] = num;
    }
}

var numStudents = 10;
var arrSize = 97;
var idLen = 9;
var students = new Array(numStudents);
genStuData(students);
console.log("Student data: \n");
for (let i = 0; i < students.length; ++i) {
    console.log(students[i].substring(0, 8) + " " + students[i].substring(9));
}
console.log("\n\nData distribution: \n");
var hTable = new HashTable();
for (let i = 0; i < students.length; ++i) {
    hTable.put(students[i]);
}
hTable.showDistro();

