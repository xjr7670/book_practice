// 计数
function Node(data, left, right) {
    this.data = data;
    this.left = left;
    this.right = right;
    this.show = show;
    this.count = 1;
}

function show() {
    return this.data;
}

// 二叉查找树
function BST() {
    this.root = null;
    this.insert = insert;
    this.inOrder = inOrder;
    this.getMin = getMin;
    this.getMax = getMax;
    this.find = find;
    this.remove = remove;
    this.removeNode = removeNode;
    this.update = update;
}

function insert(data) {
    var n = new Node(data, null, null);
    if (this.root == null) {
        this.root = n;
    } else {
        var current = this.root;
        var parent;
        while (true) {
            parent = current;
            if (data < current.data) {
                current = current.left;
                if (current == null) {
                    parent.left = n;
                    break;
                }
            } else {
                current = current.right;
                if (current == null) {
                    parent.right = n;
                    break;
                }
            }
        }    
    }
}

// 更新 BST
function update(data) {
    var grade = this.find(data);
    grade.count++;
    return grade;
}

/************** 历遍树 ********************************/
// 中序遍历
function inOrder(node) {
    if (!(node == null)) {
        inOrder(node.left);
        console.log(node.show() + " ");
        inOrder(node.right);
    }
}

// 先序遍历
function preOrder(node) {
    if (!(node == null)) {
        console.log(node.show() + " ");
        preOrder(node.left);
        preOrder(node.right);
    }
}

// 后序遍历
function postOrder(node) {
    if (!(node == null)) {
        postOrder(node.left);
        postOrder(node.right);
        console.log(node.show() + " ");
    }
}

/************** 查找最小值和最大值 ********************/
function getMin() {
    var current = this.root;
    while (!(current.left == null)) {
        current = current.left;
    }
    return current.data;
}

function getMax() {
    var current = this.root;
    while (!(current.right == null)) {
        current = current.right;
    }
    return current.data;
}

/************* 查找给定值 ***********************/
function find(data) {
    var current = this.root;
    while (current != null) {
        if (current.data == data) {
            return current;
        } else if (data < current.data) {
            current = current.left;
        } else {
            current = current.right;
        }
    }
    return null;
}

/**************** 删除节点 ************************/
// 删除数据
function remove(data) {
    root = removeNode(this.root, data);
}
// 删除节点
function removeNode(node, data) {
    if (node == null) {
        return null;
    }
    if (data == node.data) {
        // 没有子节点的节点
        if (node.left == null && node.right == null) {
            return null;
        }
        // 没有左子节点的节点
        if (node.left == null) {
            return node.right;
        }
        // 没有右子节点的节点
        if (node.right == null) {
            return node.left;
        }
        // 有两个子节点的节点
        var tempNode = getSmallest(node.right);
        node.data = tempNode.data;
        node.right = removeNode(node.right, tempNode.data);
        return node;
    } else if (data < node.data) {
        node.left = removeNode(node.left, data);
        return node;
    } else {
        node.right = removeNode(node.right, data);
        return node;
    }
}


// 随机生成成绩和显示它们
function prArray(arr) {
    console.log(arr[0].toString() + ' ');
    for (let i = 1; i < arr.length; ++i) {
        console.log(arr[i].toString() + ' ');
        if (i % 10 == 0) {
            console.log("\n");
        }
    }
}

function genArray(length) {
    var arr = [];
    for (let i = 0; i < length; ++i) {
        arr[i] = Math.floor(Math.random() * 101);
    }
    return arr;
}

//////////////////// 测试
var grades = genArray(100);
prArray(grades);
var gradedistro = new BST();
for (let i = 0; i < grades.length; ++i) {
    var g = grades[i];
    var grade = gradedistro.find(g);
    if (grade == null) {
        gradedistro.insert(g);
    } else {
        gradedistro.update(g);
    }
}

var cont = "y";
while (cont == "y") {
    console.log("\n\nEnter a grade: ");
    var g = 78;
    var aGrade = gradedistro.find(g);
    if (aGrade == null) {
        console.log("No occurrences of " + g);
    } else {
        console.log("Occurrences of " + g + ": " + aGrade.count);
    }
    console.log("Look at another grade (y/n)? ");
    cont = "n";
}