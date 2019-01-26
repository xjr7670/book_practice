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
}

// 清除
function clear() {
    this.top = 0;
}

/********************************** 判断一个算术表达式中的括号是否匹配 ***************************/

// 思路
// 如果遇到左括号 ，则入栈，遇到右括号，则把栈顶的元素出栈
// 结束后判断栈的长度，如果不为 0，则缺少右括号；
// 如果在弹出元素时发现栈的长度已经是 0 了，则表示缺少左括号

function isMatch(arithmetic) {
    var arith = new Stack();
    var sLength = arithmetic.length;
    for (let i = 0; i < sLength; i++) {
        if (arithmetic[i] == '(') {
            arith.push(arithmetic[i]);
        } else if (arithmetic[i] == ')') {
            if (arith.length() > 0) {
                arith.pop();
            } else {
                return false;
            }
        }
    }
    return (arith.length() > 0 ? false : true);
}

var s1 = "2.3 + 23 / 12 + ((3.14159 x 0.24)))";
console.log(isMatch(s1));