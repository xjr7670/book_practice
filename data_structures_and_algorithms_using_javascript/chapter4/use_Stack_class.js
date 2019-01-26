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

/*******************************************************************************************************
                                            数制间的相互转换 
 *******************************************************************************************************/
/* 利用栈将一个数字从一种数制转换成另一种数制。假设想将数字 n 转换为以 b 为基数的数字，实现转换的算法如下：
 * 
 * (1) 最高位为 n % b，将此位压入栈
 * (2) 使用 n / b 代替 n。
 * (3) 重复步骤 1 和 2，直到 n 等于 0，且没有余数。
 * (4) 持续将栈内元素弹出，直到栈为空，依次将这些元素排列，就得到转换后数字的字符串形式。
 * 
 * 此算法只针对基数为 2 - 9 的情况。
*/

function mulBase(num, base) {
    var s = new Stack();
    do {
        s.push(num % base);
        num = Math.floor(num /= base);
    } while (num > 0);

    var converted = "";
    while (s.length() > 0) {
        converted += s.pop();
    }
    return converted;
}

/************************** 将数字转换为二进制和八进制 *************************/
var num = 32;
var base = 2;
var newNum = mulBase(num, base);
console.log(num + " converted to base " + base + " is " + newNum);
num = 125;
base = 8;
var newNum = mulBase(num, base);
console.log(num + " converted to base " + base + " is " + newNum);