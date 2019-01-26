// 栈对象
var Stack = function() {
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
}(
// 清除
function clear() {
    this.top = 0;
}

/********************************** 以下是 Stack 类的测试使用 ***************************/

var s = new Stack();
s.push("David");
s.push("Raymond");
s.push("Bryan");
console.log("length: " + s.length());
console.log(s.peek());

var popped = s.pop();
console.log("The popped element is: " + popped);
console.log(s.peek());
s.push("Cynthia");
console.log(s.peek());
s.clear();
console.log("length: " + s.length());
console.log(s.peek());
s.push("Clayton");
console.log(s.peek());