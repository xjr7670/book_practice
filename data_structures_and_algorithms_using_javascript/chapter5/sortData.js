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


/********************************** 使用队列对数据进行排序 *************************************/
function distribute(nums, queues, n, digit) { // 参数 digit 表示个位或十位上的值
    for (let i = 0; i < n; ++i) {
        if (digit == 1) {
            queues[nums[i] % 10].enqueue(nums[i]);
        } else {
            queues[Math.floor(nums[i] / 10)].enqueue(nums[i]);
        }
    }
}

function collect(queues, nums) {
    var i = 0;
    for (let digit = 0; digit < 10; ++digit) {
        while (!queues[digit].empty()) {
            nums[i++] = queues[digit].dequeue();
        }
    }
}

function dispArray(arr) {
    var str = "";
    for (let i = 0; i < arr.length; i++) {
        str += arr[i] + " ";
    }
    console.log(str);
}

// 主程序
var queues = [];
for (let i = 0; i < 10; i++) {
    queues[i] = new Queue();
}

var nums = [];
for (let i = 0; i < 10; i++) {
    nums[i] = Math.floor(Math.floor(Math.random() * 101));
}

console.log("Before radix sort: ");
dispArray(nums);
distribute(nums, queues, 10, 1);
collect(queues, nums);
distribute(nums, queues, 10, 10);
collect(queues, nums);
console.log("\n\nAfter radix sort: ");
dispArray(nums);