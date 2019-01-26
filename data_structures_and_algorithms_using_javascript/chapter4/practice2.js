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

/********************************** 用栈将中缀表达式转换为后缀表达式，并求值 ***************************/

// 思路
// 使用两个栈，一个用来存储操作数，另一个用来存储操作符
// 变为后缀表达式：
// 求值：
// 参考 —— https://www.cnblogs.com/hapjin/p/5374268.html

function suffixExpression() {
    var str = 'a+b*c+(d*e+f)*g';
    var stack = new Stack();
    var outStack = new Array();

    for (let i = 0; i < str.length; ++i) {
        if (')' == str[i]) {
            while (true) {
                var top = stack.peek();
                stack.pop();
                if ('(' != top) {
                    outStack[outStack.length] = top;
                } else {
                    break;
                }
            }
        } else if (['-', '+'].indexOf(str[i]) > -1) {
            if (['*', '/'].indexOf(stack.peek()) > -1) {
                while (['*', '/'].indexOf(stack.peek()) > -1) {
                    outStack[outStack.length] = stack.peek();
                    stack.pop();
                }
                outStack[outStack.length] = str[i];
            } else {
                stack.push(str[i]);
            }
        } else if (['(', '*', '/'].indexOf(str[i]) > -1) {
            stack.push(str[i]);
        } else {
            outStack[outStack.length] = str[i];
        }
    }

    for (let i = 0; i < outStack.length; i++) {
        console.log(outStack[i]);
    }
}

suffixExpression();

/*************** 求值 **************************/
function countSuffixExpression() {
    var str = '6523+8*+3+*';
    var stack = new Stack();

    for (let i = 0; i < str.length; i++) {
        if (isNaN(str[i])) {
            stack.push(eval(stack.pop() + str[i] + stack.pop()));
        } else {
            stack.push(str[i]);
        }
    }

    console.log(stack.pop());
}
countSuffixExpression();