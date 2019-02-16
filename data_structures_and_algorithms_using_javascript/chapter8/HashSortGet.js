// 8.4.2 节 —— 对散列表排序、从散列表中取值（没有实现）
// 散列表
function HashTable() {
    this.table = new Array(137);
    this.simpleHash = simpleHash;
    this.betterHash = betterHash;
    this.showDistro = showDistro;
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
    this.table[pos] = data;
}

function get(key) {
    return this.table[this.betterHash(key)];
}

function showDistro() {
    var n = 0;
    for (let i = 0; i < this.table.length; ++i) {
        if (this.table[i] != undefined) {
            console.log(i + ": " + this.table[i]);
        }
    }
}

/******************* 散列化整型键 *************************/
