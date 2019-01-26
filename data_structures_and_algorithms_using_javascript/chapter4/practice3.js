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

/********************************** 用栈解决佩兹糖国盒问题，移除黄色糖果，保持原来的顺序不变 ***************************/
var sweetBox = new Stack();
sweetBox.push('red');
sweetBox.push('yellow');
sweetBox.push('red');
sweetBox.push('yellow');
sweetBox.push('white');
sweetBox.push('yellow');
sweetBox.push('white');
sweetBox.push('yellow');
sweetBox.push('white');
sweetBox.push('red');

function getColor(element, stack) {

    console.log("Before: \n", stack.dataStore);

    var getColorStack = new Stack();    // 保存需要去掉的颜色的栈
    var setColorStack = new Stack();    // 保存原栈去掉特定的颜色之后的栈

    while (stack.length() > 0) {
        if (stack.peek() == element) {
            getColorStack.push(element);
            stack.pop();
        } else {
            setColorStack.push(stack.peek());
            stack.pop();
        }
    }
    
    var newStack = new Stack();
    while (setColorStack.length() > 0) {
        newStack.push(setColorStack.peek());
        setColorStack.pop();
    }
    console.log("After: \n", newStack.dataStore);
}
getColor('yellow', sweetBox);