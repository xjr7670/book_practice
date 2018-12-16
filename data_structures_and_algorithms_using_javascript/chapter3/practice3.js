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
    this.showSameSex = showSameSex;
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

/*********************** 练习3. 创建 Person 类
增加一个方法显示列表中所有同性别的人 **********************************/

function Person(name, sex) {
    this.name = name;
    this.sex = sex;
}

function showSameSex(sex) {
    var sexArr = [];
    // for (this.front(); this.currPos() < this.length(); this.next()) {
    //     let currentPerson = this.getElement();
    //     if (currentPerson.sex === sex) {
    //         sexArr.push(currentPerson.name);
    //     }
    // }

    // 用 filter 实现
    sexArr = this.dataStore.filter((person) => {
        if (person.sex == sex) {
            return true;
        }
        return false;
    })
    return sexArr.map((obj) => {
        return obj.name;
    });
}

var p1 = new Person('Cavin', 'male');
var p2 = new Person('Jully', 'female');
var p3 = new Person('John', 'male');
var p4 = new Person('Alice', 'female');
var p5 = new Person('Tom', 'male');

var personList = new List();
personList.append(p1);
personList.append(p2);
personList.append(p3);
personList.append(p4);
personList.append(p5);
console.log(personList.showSameSex('female').toString());
    
