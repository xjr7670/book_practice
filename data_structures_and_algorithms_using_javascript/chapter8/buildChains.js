// ********** 碰撞冲突解决 － 开链法
// 散列表
function HashTable() {
    this.table = new Array(137);
    this.simpleHash = simpleHash;
    this.betterHash = betterHash;
    this.showDistro = showDistro;
    this.buildChains = buildChains;
    this.put = put;
    this.get = get;
}

// 散列函数
function simpleHash(data) {
    var total = 0;
    for (let i = 0; i < data.length; ++i) {
        total += data.charCodeAt(i);   
    }
    return total % this.table.length;
}

// 更好的散列函数
function betterHash(string) {
    const H = 37;
    var total = 0;
    for (let i = 0; i < string.length; ++i) {
        total += H * total + string.charCodeAt(i);
    }
    total = total % this.table.length;
    if (total < 0) {
        total += this.table.length - 1;
    }
    return parseInt(total);
}

function put(key, data) {
    var pos = this.betterHash(key);
    var index = 0;
    if (this.table[pos][index] == undefined) {
        this.table[pos][index+1] = data;
        ++index;
    } else {
        while (this.table[pos][index] != undefined) {
            ++index;
        }
        this.table[pos][index+1] = data;
    }    
}

function get(key) {
    var index = 0;
    var hash = this.betterHash(key);
    if (this.table[pos][index] == key) {
        return this.table[pos][index+1];
        index += 2
    } else {
        while (this.table[pos][index] != key) {
            index += 2;
        }
        return this.table[pos][index+1];
    }
    return undefined;
}

function showDistro() {
    var n = 0;
    for (let i = 0; i < this.table.length; ++i) {
        if (this.table[i][0] != undefined) {
            console.log(i + ": " + this.table[i]);
        }
    }
}

// 开链法
function buildChains() {
    for (let i = 0; i < this.table.length; ++i) {
        this.table[i] = new Array();
    }
}

/******************* 使用开链法避免碰撞 *************************/
var hTable = new HashTable();
hTable.buildChains();
var someNames = ["David", "Jennifer", "Donnie", "Raymond", "Cynthia", "Mike", "Clayton", "Danny", "Jonathan"];
for (let i = 0; i < someNames.length; ++i) {
    hTable.put(someNames[i]);
}
hTable.showDistro();
