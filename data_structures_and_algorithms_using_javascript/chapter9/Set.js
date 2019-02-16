// 集合的构造函数
function Set() {
    this.dataStore = [];
    this.add = add;
    this.remove = remove;
    this.contains = contains;
    this.size = size;
    this.union = union;
    this.interset = interset;
    this.subset = subset;
    this.difference = difference;
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

// 检查一个成员是否属于该集合
function contains(data) {
    if (this.dataStore.indexOf(data) > -1) {
        return true;
    } else {
        return false;
    }
}

// 获取集合大小
function size() {
    return  this.dataStore.length;
}

// 并集
function union(set) {
    var tempSet = new Set();
    for (let i = 0; i < this.dataStore.length; ++i) {
        tempSet.add(this.dataStore[i]);
    }

    for (let i = 0; i < set.dataStore.length; ++i) {
        if (!tempSet.contains(set.dataStore[i])) {
            tempSet.dataStore.push(set.dataStore[i]);
        }
    }
    return tempSet;
}

function show() {
    return this.dataStore;
}

// 求交集
function interset(set) {
    var tempSet = new Set();
    for (let i = 0; i < this.dataStore.length; ++i) {
        if (set.contains(this.dataStore[i])) {
            tempSet.add(this.dataStore[i]);
        }
    }
    return tempSet;
}

// 判断是否为子集
function subset(set) {
    if (this.size() > set.size()) {
        return false;
    } else {
        for (let member of this.dataStore) {
            if (!set.contains(member)) {
                return false;
            }
        }
    }
    return true;
}

// 获取两个集合的补集
function difference(set) {
    var tempSet = new Set();
    for (let i = 0; i < this.dataStore.length; ++i) {
        if (!set.contains(this.dataStore[i])) {
            tempSet.add(this.dataStore[i]);
        }
    }
    return tempSet;
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

// 求两个集合的并集
var cis = new Set();
cis.add("Jennifer");
cis.add("Cynthia");
cis.add("Mike");
cis.add("Raymond");
var dmp = new Set();
dmp.add("Raymond");
dmp.add("Cynthia");
dmp.add("Jonathan");
var it = new Set();
it = cis.union(dmp);
console.log(it.show());

// 求两个集合的交集
var inter = cis.interset(dmp);
console.log(inter.show());

// 判断一个集合是否为另一个集合的子集
cis.add("Clayton");
cis.add("Denny");
cis.add("Jonathan");
cis.add("Terrill");
if (dmp.subset(cis)) {
    console.log("DMP is a subset of CIS.");
} else {
    console.log("DMP is not a subset of CIS.");
}
dmp.add("Shirley");
if (dmp.subset(cis)) {
    console.log("DMP is a subset of CIS.");
} else {
    console.log("DMP is not a subset of CIS.");
}

// 求两个集合的补集
var diff = new Set();
diff = cis.difference(dmp);
console.log("[" + cis.show() + "] difference [" + dmp.show() + "] -> [" + diff.show() + "]");