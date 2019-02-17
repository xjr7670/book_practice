// 希尔排序

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

    // 希尔排序
    this.gaps = [5, 3, 1];
    this.shellSort = shellSort;
    this.shellSort1 = shellSort1;
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

// 希尔排序
function shellSort() {
    for (let g = 0; g < this.gaps.length; ++g) {
        for (let i = this.gaps[g]; i < this.dataStore.length; ++i) {
            var temp = this.dataStore[i];
            for (var j = i; j >= this.gaps[g] && this.dataStore[j-this.gaps[g]] > temp; j -= this.gaps[g]) {
                this.dataStore[j] = this.dataStore[j-this.gaps[g]];
                
            }
            this.dataStore[j] = temp;
        }
       // console.log(this.dataStore.toString());
    }
}

// 动态计算间隔序列的希尔排序
function shellSort1() {
    var N = this.dataStore.length;
    var h = 1;
    while (h < N/3) {
        h = 3 * h + 1;
    }
    while (h >= 1) {
        for (let i = h; i < N; i++) {
            for (let j = i; j >= h && this.dataStore[j] < this.dataStore[j-h]; j -= h) {
                swap(this.dataStore, j, j-h);
            }
        }
        h = (h-1) / 3;
    }
}

function setGaps(arr) {
    this.gaps = arr;
}

// 测试希尔排序

// var nums = new CArray(100);
// nums.setData();
// console.log("\n希尔排序前：\n");
// console.log(nums.toString());
// console.log("\n希尔排序中：\n");
// nums.shellSort();
// console.log("\n希尔排序后：\n");
// console.log(nums.toString());

// var nums1 = new CArray(100);
// nums1.setData();
// console.log("\n希尔排序前1：\n");
// console.log(nums1.toString());
// nums1.shellSort1();
// console.log("\n希尔排序后1：\n");
// console.log(nums1.toString());

// 比较两种希尔排序算法
var nums = new CArray(100000);
nums.setData();
var start = new Date().getTime();
nums.shellSort();
var stop = new Date().getTime();
var elapsed = stop - start;
console.log("硬编码间隔序列的希尔排序耗时：" + elapsed + " 毫秒。");
nums.clear();
nums.setData();
start = new Date().getTime();
nums.shellSort1();
stop = new Date().getTime();
elapsed = stop - start;
console.log("动态间隔序列的希尔排序耗时：" + elapsed + " 毫秒。");
