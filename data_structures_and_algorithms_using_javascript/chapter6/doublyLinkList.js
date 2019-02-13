/***** 双向链表 *****/
function Node(element) {
    this.element = element;
    this.next = null;
    // 增加一个 previous 属性
    this.previous = null;
}

function LList() {
    this.head = new Node("head");
    this.find = find;
    this.insert = insert;
    this.remove = remove;
    this.findPrevious = findPrevious;
    this.findLast = findLast;
    this.display = display;
    this.dispReverse = dispReverse;
}


// 查找方法
function find(item) {
    var currNode = this.head;
    while (currNode.element != item) {
        currNode = currNode.next;
    }
    return currNode;
}

// 插入新节点
function insert(newElement, item) {
    var newNode = new Node(newElement);
    var current = this.find(item);
    newNode.next = current.next;
    newNode.previous = current;
    current.next = newNode;
}

// 显示链表中的元素
function display() {
    var currNode = this.head;
    while (!(currNode.next == null)) {
        console.log(currNode.next.element);
        currNode = currNode.next;
    }
}

// 查找前一个元素的方法
function findPrevious(item) {
    var currNode = this.head;
    while(!(currNode.next == null) && (currNode.next.element != item)) {
        currNode = currNode.next;
    }
    return currNode;
}

// 删除元素
function remove(item) {
    var currNode = this.find(item);
    if (!(currNode.next == null)) {
        currNode.previous.next = currNode.next;
        currNode.next.previous = currNode.previous;
        currNode.next = null;
        currNode.previous = null;
    }
}

// 查找最后的节点
function findLast() {
    var currNode = this.head;
    while (!(currNode.next == null)) {
        currNode = currNode.next;
    }
    return currNode;
}

// 反向显示双向链表中的元素
function dispReverse() {
    var currNode = this.head;
    currNode = this.findLast();
    while (!(currNode.previous == null)) {
        console.log(currNode.element);
        currNode = currNode.previous;
    }
}
/********************* LList 类测试程序 ************************/
var cities = new LList();
cities.insert("Conway", "head");
cities.insert("Russellville", "Conway");
cities.insert("Carlisle", "Russellville");
cities.insert("Alma", "Carlisle");
cities.display();
console.log();
/******************** 测试 remove 方法 *************************/
cities.remove("Carlisle");
cities.display();
console.log();
cities.dispReverse();