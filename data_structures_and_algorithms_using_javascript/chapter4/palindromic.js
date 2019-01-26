// 栈对象
function Stack() {
    this.dataStore = [];
    this.top = 0;
    this.push = push;
    this.pop = pop;
    this.peek = peek;
    this.clear = clear;
    this.length = length;
}

// 压入方法
function push(element) {
    this.dataStore[this.top++] = element;
}

// 弹出方法
function pop() {
    // 这里 -- 操作符放在 this.top 前面
    // 是因为列表下标的最大值，是它的长度减1
    // 如果直接取 this.top，会发生下标溢出
    return this.dataStore[--this.top];
}

// 预览方法
function peek() {
    return this.dataStore[this.top-1];
}

// 求长度
function length() {
    return this.top;
}

// 清除
function clear() {
    this.top = 0;
}

/***************** 用栈判断是否为回文 ***********************/
function isPalindrome(word) {
    var s = new Stack();
    for (let i = 0; i < word.length; ++i) {
        s.push(word[i]);
    }
    var rword = "";
    while (s.length() > 0) {
        rword += s.pop();
    }
    if (word == rword) {
        return true;
    } else {
        return false;
    }
}

var word = "hello";
if (isPalindrome(word)) {
    console.log(word + " is a palindrome.");
} else {
    console.log(word + " is not a palindrome.");
}

word = "racecar";
if (isPalindrome(word)) {
    console.log(word + " is a palindrome.");
} else {
    console.log(word + " is not a palindrome.");
}