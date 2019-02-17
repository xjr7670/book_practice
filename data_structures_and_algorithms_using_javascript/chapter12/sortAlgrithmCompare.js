// 几种排序算法的比较

// 插入排序

// 插入排序
// 冒泡排序
// 数组测试平台
function CArray(numElements) {
    this.dataStore = [];
    this.pos = 0;
    this.numElements = numElements;
    this.insert = insert;
    this.toString = toString;
    this.clear = clear;
    this.setData = setData;
    this.swap = swap;
    for (let i = 0; i < numElements; ++i) {
        this.dataStore[i] = i;
    }
    this.bubbleSort = bubbleSort;
    this.selectionSort = selectionSort;
    this.insertionSort = insertionSort;
}

function setData() {
    for (let i = 0; i < this.numElements; ++i) {
        this.dataStore[i] = Math.floor(Math.random() * (this.numElements + 1));
    }
}

function clear() {
    for (let i = 0; i < this.dataStore.length; ++i) {
        this.dataStore[i] = 0;
    }
}

function insert(element) {
    this.dataStore[this.pos++] = element;
}

function toString() {
    var retstr = "";
    for (let i = 0; i < this.dataStore.length; ++i) {
        retstr += this.dataStore[i] + " ";
        if (i > 0 && i % 10 == 0) {
            retstr += "\n";
        }
    }
    return retstr;
}

function swap(arr, index1, index2) {
    var temp = arr[index1];
    arr[index1] = arr[index2];
    arr[index2] = temp;
}


// 冒泡排序算法
function bubbleSort() {
    var numElements = this.dataStore.length;
    var temp;
    for (let outer = numElements; outer >= 2; --outer) {
        for (var inner = 0; inner <= outer - 1; ++inner) {
            if (this.dataStore[inner] > this.dataStore[inner + 1]) {
                swap(this.dataStore, inner, inner + 1);
            }
        }
        // console.log(this.toString());
    }
}

// 选择排序算法
function selectionSort() {
    var min, temp;
    for (let outer = 0; outer <= this.dataStore.length - 2; ++outer) {
        min = outer;
        for (let inner = outer + 1; inner <= this.dataStore.length - 1; ++inner) {
            if (this.dataStore[inner] < this.dataStore[min]) {
                min = inner;
            }
            swap(this.dataStore, outer, min);
        }
        // console.log(this.dataStore.toString());
    }
}

// 插入排序算法
function insertionSort() {
    var temp, inner;
    for (let outer = 1; outer <= this.dataStore.length - 1; ++outer) {
        temp = this.dataStore[outer];
        inner = outer;
        while (inner > 0 && (this.dataStore[inner - 1] >= temp)) {
            this.dataStore[inner] = this.dataStore[inner - 1];
            --inner;
        }
        this.dataStore[inner] = temp;
    }
}

// 为排序函数计时

var numElements = 10000;
var mynums = new CArray(numElements);
mynums.setData();
var start = new Date().getTime();
mynums.bubbleSort();
var stop = new Date().getTime();
var elapsed = stop - start;
console.log("对 " + numElements + " 个元素执行冒泡排序耗时：" + elapsed + " 毫秒。");
start = new Date().getTime();
mynums.selectionSort();
stop = new Date().getTime();
elapsed = stop - start;
console.log("对 " + numElements + " 个元素执行选择排序耗时：" + elapsed + " 毫秒。");
start = new Date().getTime();
mynums.insertionSort();
stop = new Date().getTime();
elapsed = stop - start;
console.log("对 " + numElements + " 个元素执行插入排序耗时：" + elapsed + " 毫秒。");
