/*************** 队列的实现 *************/
function Queue() {
    this.dataStore = [];
    this.enqueue = enqueue;
    this.dequeue = dequeue;
    this.front = front;
    this.back = back;
    this.toString = toString;
    this.empty = empty;
}

// 向队尾添加一个元素
function enqueue(element) {
    this.dataStore.push(element);
}

// 删除队首元素
function dequeue() {
    var priority = this.dataStore[0].code;
    var largeIx = 0;
    for (let i = 0; i < this.dataStore.length; ++i) {
        if (this.dataStore[i].code > priority) {
            priority = this.dataStore[i].code;
            largeIx = i;
        }
    }
    return this.dataStore.splice(largeIx, 1);
}

// 读队首和队尾的元素
function front() {
    return this.dataStore[0];
}

function back() {
    return this.dataStore[this.dataStore.length-1];
}

// 显示队列内所有元素
function toString() {
    var retStr = "";
    for (let i = 0; i < this.dataStore.length; ++i) {
        retStr += this.dataStore[i].name + " code: " + this.dataStore[i].code + "\n";
    }
    return retStr;
}

// 判断队列是否为空
function empty() {
    if (this.dataStore.length == 0) {
        return true;
    } else {
        return false;
    }
}


/********************************** 优先队列 *************************************/
function Patient(name, code) {
    this.name = name;
    this.code = code;
}

var p = new Patient("Smith", 5);
var ed = new Queue();
ed.enqueue(p);
p = new Patient("Jones", 4);
ed.enqueue(p);
p = new Patient("Fehrenbach", 6);
ed.enqueue(p);
p = new Patient("Brown", 1);
ed.enqueue(p);
p = new Patient("Ingram", 7);
ed.enqueue(p);
console.log(ed.toString());

var seen = ed.dequeue();
console.log("Patient being treated: " + seen[0].name);
console.log("Patient waiting to be seen: ");
console.log(ed.toString());
// 下一轮
var seen = ed.dequeue();
console.log("Patient being treated: " + seen[0].name);
console.log("Patients waiting to be seen: ");
console.log(ed.toString());
var seen = ed.dequeue();
console.log("Patient being treated: " + seen[0].name);
console.log("Patients waiting to be seen: ");
console.log(ed.toString());


function mySort() {
    var numList = [1, 3, 5, 2, 5, 9, 9, 7];
    var large = numList[0];
    var largeIx = 0;
    for (let i = 0; i < numList.length; ++i) {
        if (numList[i] > large) {
            large = numList[i];
            largeIx = i;
        }
    }
    console.log(largeIx);
    console.log(numList.splice(largeIx, 1));
}

mySort();