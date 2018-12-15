function words() {
    this.dataStore = [];
    this.add = add;
    this.join = join;
}

function add(temp) {
    this.dataStore.push(temp);
}

function join() {
    var joinWord = '';
    for (let i = 0; i < this.dataStore.length; ++i) {
        joinWord += this.dataStore[i];
    }
    return joinWord;
}

var w = new words();
w.add("h");
w.add("e");
w.add("l");
w.add("l");
w.add("o");
console.log(w.join());