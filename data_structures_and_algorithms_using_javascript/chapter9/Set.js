// 集合的构造函数
function Set() {
    this.dataStore = [];
    this.add = add;
    this.remove = remove;
//     this.size = size;
//     this.union = union;
//     this.interset = interset;
//     this.subset = subset;
//     this.difference = difference;
    this.show = show;
}

function add(data) {
    if (this.dataStore.indexOf(data) < 0) {
        this.dataStore.push(data);
        return true;
    } else {
        return false;
    }
}

function remove(data) {
    var pos = this.dataStore.indexOf(data);
    if (pos > -1) {
        this.dataStore.splice(pos, 1);
        return true;
    } else {
        return false;
    }
}

function show() {
    return this.dataStore;
}

// 测试 Set 类
var names = new Set();
names.add("David");
names.add("Jennifer");
names.add("Cynthia");
names.add("Mike");
names.add("Raymond");
if (names.add("Mike")) {
    console.log("Mike added");
} else {
    console.log("Can't add Mike, must already be in set.");
}
console.log(names.show());
var removed = "Mike";
if (names.remove(removed)) {
    console.log(removed + " removed");
} else {
    console.log(removed + " not removed");
}
names.add("Clayton");
console.log(names.show());
removed = "Alisa";
if (names.remove(removed)) {
    console.log(removed + " removed");
} else {
    console.log(removed + " not removed");
}