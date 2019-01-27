/*************** 队列的实现 *************/
function Queue() {
    this.dataStore = [];
    this.enqueue = enqueue;
    this.dequeue = dequeue;
    this.front = front;
    this.back = back;
    this.toString = toString;
    this.empty = empty;
    this.count = count
}

// 向队尾添加一个元素
function enqueue(element) {
    this.dataStore.push(element);
}

// 删除队首元素
function dequeue() {
    return this.dataStore.shift();
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
        retStr += this.dataStore[i] + "\n";
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

// 显示排除等候的跳舞的男性和女性的数量
function count() {
    return this.dataStore.length;
}

/********************************** 方块舞的舞伴分配问题 *************************************/

const fs = require("fs");

// 每个舞者都存储在一个 Dancer 对象中
function Dancer(name, sex) {
    this.name = name;
    this.sex = sex;
}

function getDancers(males, females) {
    var names = fs.readFileSync("dancers.txt").toString().split("\n");

    for (let i = 0; i < names.length; ++i) {
        names[i] = names[i].trim();
    }
    for (let i = 0; i < names.length; ++i) {
        var dancer = names[i].split(" ");
        var sex = dancer[0];
        var name = dancer[1];

        if (sex == "F") {
            females.enqueue(new Dancer(name, sex));
        } else {
            males.enqueue(new Dancer(name, sex));
        }
    }
}

// 将男性和女性组成舞伴，并宣布配对结果
function dance(males, females) {
    console.log("The dance partners are: \n");
    var person;
    while (!females.empty() && !males.empty()) {
        person = females.dequeue();
        console.log("Female dancer is: " + person.name);
        person = males.dequeue();
        console.log(" and the male dancer is: " + person.name);
    }
    console.log();
}


////////// 测试程序
var maleDancers = new Queue();
var femaleDancers = new Queue();

getDancers(maleDancers, femaleDancers);
dance(maleDancers, femaleDancers);
if (femaleDancers.count() > 0) {
    console.log("There are " + femaleDancers.count() + " female dancers waiting to dance.");
}

if (maleDancers.count() > 0) {
    console.log("There are " + maleDancers.count() + " female dancers waiting to dance.");
}