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
    for (let key in this.dataStore) {
        console.log(key + ' -> ' + this.dataStore[key]);
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

/***************** 使用 Dictionary 类 *****************/
var pbook = new Dictionary()
pbook.add("Mike", "123");
pbook.add("David", "345");
pbook.add("Cynthia", "456");
console.log("Number of entries: " + pbook.count());
console.log("David's extension: " + pbook.find("David"));
pbook.showAll();
pbook.remove("Mike");
pbook.clear();
console.log("Number of entries: " + pbook.count());