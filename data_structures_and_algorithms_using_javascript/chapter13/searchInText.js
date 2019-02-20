// 查找文本数据

const fs = require("fs");


// 使用 seqSearch() 函数查找文本数据
function seqSearch(arr, data) {
    for (let i = 0; i < arr.length; ++i) {
        if (arr[i] == data) {
            return i;
        }
    }
    return -1;
}

// 使用 binSearch() 函数查找文本数据
function binSearch(arr, data) {
    var upperBound = arr.length - 1;
    var lowerBound = 0;
    while (lowerBound <= upperBound) {
        var mid = Math.floor((upperBound + lowerBound) / 2);
        if (arr[mid] < data) {
            lowerBound = mid + 1;
        } else if (arr[mid] > data) {
            upperBound = mid - 1;
        } else {
            return mid;
        }
    }
    return -1;
}

// 插入排序算法
function insertionSort(arr) {
    var temp, inner;
    for (let outer = 1; outer <= arr.length - 1; ++outer) {
        temp = arr[outer];
        inner = outer;
        while (inner > 0 && (arr[inner - 1] >= temp)) {
            arr[inner] = arr[inner - 1];
            --inner;
        }
        arr[inner] = temp;
    }
}

var words = fs.readFileSync("E:/temp/words.txt", "utf-8").split(" ");
var word = "rhetoric";
var start = new Date().getTime();
var position = seqSearch(words, word);
var stop = new Date().getTime();
var elapsed = stop - start;
if (position >= 0) {
    console.log("单词 " + word + " 被找的位置在：" + position + "。");
    console.log("顺序查找消耗了 " + elapsed + " 毫秒");
} else {
    console.log(word + " 这个单词没有出现在这个文件内容中。");
}

insertionSort(words);
start = new Date().getTime();
position = binSearch(words, word);
stop = new Date().getTime();
elapsed = stop - start;
if (position >= 0) {
    console.log("单词 " + word + " 被找的位置在：" + position + "。");
    console.log("二分查找消耗了 " + elapsed + " 毫秒");
} else {
    console.log(word + " 这个单词没有出现在这个文件内容中。");
}