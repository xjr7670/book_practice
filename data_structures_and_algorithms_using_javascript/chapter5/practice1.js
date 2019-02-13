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
    this.dataStore.pop();
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


/********************************** 队列的测试 *************************************/
var q = new Deque();
q.enqueue("Meredith");
q.enqueue("Cynthia");
q.enqueue("Jennifer");
console.log(q.toString());
q.pop();
console.log(q.toString());
console.log("Front of queue: " + q.front());
console.log("Back of queue: " + q.back());
q.unshift('Cavin');
console.log(q.toString());
