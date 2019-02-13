/*************** Deque 类的实现 *************/
function Deque() {
    this.dataStore = [];
    this.enqueue = enqueue;
    this.dequeue = dequeue;
    this.unshift = unshift;
    this.pop = pop;
    this.front = front;
    this.back = back;
    this.toString = toString;
    this.empty = empty;
}

// 向队尾添加一个元素
function enqueue(element) {
    this.dataStore.push(element);
}

// 从队尾删除一个元素
function pop() {
    return this.dataStore.pop();
}

// 增加元素到队首
function unshift(element) {
    this.dataStore.unshift(element);
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


/******************** 用 Deque 类判断一个给定单词是否为回文*****************/
function isHuiWen(str) {
    var d = new Deque();
    for (let i = 0; i < str.length; ++i) {
        d.enqueue(str[i]);
    }

    var front = '', end = '';
    // 如果单词长度是奇数，则中间那个不需要判断
    while (!d.empty() && d.dataStore.length != 1) {
        front = d.dequeue();
        end = d.pop();
        if (front != end) {
            return false;
        }
    }
    return true;
}

var testStr = "levvel";
console.log(isHuiWen(testStr));