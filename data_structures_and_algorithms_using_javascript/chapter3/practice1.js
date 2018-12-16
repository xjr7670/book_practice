function List() {
    this.listSize = 0;
    this.pos = 0;
    this.dataStore = [];    // 初始化一个空数组来保存列表元素
    this.clear = clear;
    this.find = find;
    this.toString = toString;
    this.insert = insert;
    this.append = append;
    this.remove = remove;
    this.front = front;
    this.end = end;
    this.prev = prev;
    this.next = next;
    this.length = length;
    this.currPos = currPos;
    this.moveTo = moveTo;
    this.getElement = getElement;
    this.contains = contains;
    this.smartInsert = insertLargeThan;
}

function append(element) {
    this.dataStore[this.listSize++] = element;
}

function find(element) {
    for (let i = 0; i < this.dataStore.length; ++i) {
        if (this.dataStore[i] == element) {
            return i;
        }
    }
    return -1;
}

function remove(element) {
    var foundAt = this.find(element);
    if (foundAt > -1) {
        this.dataStore.splice(foundAt, 1);
        --this.listSize;
        return true;
    }
    return false;
}

function length() {
    return this.listSize;
}

function toString() {
    return this.dataStore;
}

function insert(element, after) {
    var insertPos = this.find(after);
    if (insertPos > -1) {
        this.dataStore.splice(insertPos+1, 0, element);
        ++this.dataStore;
        return true;
    }
    return false;
}

function clear() {
    delete this.dataStore;
    this.dataStore = [];
    this.listSize = this.pos = 0;
}

function contains(element) {
    for (let i = 0; i < this.dataStore.length; ++i) {
        if (this.dataStore[i] == element) {
            return true;
        }
    }
    return false;
}

function front() {
    this.pos = 0;
}

function end() {
    this.pos = this.listSize - 1;
}

function prev() {
    if (this.pos > 0) {
        --this.pos;
    }
}

function next() {
    // if (this.pos < this.listSize - 1) {
    //     ++this.pos;
    // }

    // 在本章中，列表应该是可以无限next下去的，否则后面的for循环会进入死循环
    ++this.pos;
}

function currPos() {
    return this.pos;
}

function moveTo(position) {
    this.pos = position;
}

function getElement() {
    return this.dataStore[this.pos];
}

/*********************** 练习1. 增加一个向列表插入元素的方法，
只在该元素大于列表中的所有元素时才插入 **********************************/

function insertLargeThan(element, after) {
    var largeThanAll = this.dataStore.every((a) => {
        if (element > a) {
            return true;
        }
        return false;
    });
    if (largeThanAll) {
        this.insert(element, after);
    }
}

var numList = new List();
numList.append(1);
numList.append(3);
numList.append(4);
numList.append(8);
console.log(numList.dataStore.toString());
numList.smartInsert(10, 4);
console.log(numList.dataStore.toString());
    
