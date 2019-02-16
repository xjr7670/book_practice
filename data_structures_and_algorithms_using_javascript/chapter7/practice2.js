/******* Dictionary 类 ********/
function Dictionary() {
    this.dataStore = new Array();
    this.add = add;
    this.find = find;
    this.remove = remove;
    this.showAll = showAll;
    this.count = count;
    this.clear = clear;
}

function add(key, value) {
    this.dataStore[key] = value;
}

function find(key) {
    return this.dataStore[key];
}

function remove(key) {
    delete this.dataStore[key];
}

function showAll() {
    var sortedKey = Object.keys(this.dataStore).sort();
    for (let key in sortedKey) {
        console.log(sortedKey[key] + ' -> ' + this.dataStore[sortedKey[key]]);
    }
}

// 获取字典元素个数
function count() {
    var n = 0;
    for (let key in this.dataStore) {
        ++n;
    }
    return n;
}

// 清空字典
function clear() {

    for (let key in this.dataStore) {
        delete this.dataStore[key];
    }
}

/***************** 练习2，用字典统计一句话中各个单词的出现次数 *****************/
var sentence = "the brown fox jumped over the blue fox";
var wordCount = new Dictionary();
var sentArr = sentence.split(' ')

var w = '';
for (let i in sentArr) {
    w = sentArr[i];
    if (Object.keys(wordCount.dataStore).includes(w)) {
        wordCount.dataStore[w] += 1;
    } else {
        wordCount.add(w, 1)
    }
}

wordCount.showAll();