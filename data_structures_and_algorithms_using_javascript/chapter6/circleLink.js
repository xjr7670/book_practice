/***** 循环链表 *****/
function Node(element) {
    this.element = element;
    this.next = null;
}

function LList() {
    this.head = new Node("head");
    this.head.next = this.head;
    this.find = find;
    this.insert = insert;
    this.remove = remove;
    this.findPrevious = findPrevious;
    this.display = display;
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
    current.next = newNode;
}

// 显示链表中的元素
function display() {
    var currNode = this.head;
    while (!(currNode.next == null) && !(currNode.next.element == "head")) {
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
    var prevNode = this.findPrevious(item);
    if (!(prevNode.next == null) && !(currNode.next.element == "head")) {
        prevNode.next = prevNode.next.next;
    }
}
/********************* LList 类测试程序 ************************/
var cities = new LList();
cities.insert("Conway", "head");
cities.insert("Russellville", "Conway");
cities.insert("Carlisle", "Russellville");
cities.insert("Alma", "Carlisle");
cities.display();

/******************** 测试 remove 方法 *************************/
cities.remove("Carlisle");
cities.display();