// 使用动态规划法求斐波那契数列

function dynFib(n) {
    var val = [];
    for (let i = 0; i <= n; ++i) {
        val[i] = 0;
    }
    if (n == 1 || n == 2) {
        return 1;
    } else {
        val[1] = 1;
        val[2] = 2;
        for (let i = 3; i <= n; ++i) {
            val[i] = val[i - 1] + val[i-2];
        }
        return val[n-1];
    }
}

// 使用递归实现求斐波那契数列
function recurFib(n) {
    if (n < 2) {
        return n;
    } else {
        return recurFib(n - 1) + recurFib(n - 2);
    }
}

// 迭代版的动态规划法
function iterFib(n) {
    var last = 1;
    var nextLast = 1;
    var result = 1;
    for (let i = 2; i < n; i++) {
        result = last + nextLast;
        nextLast = last;
        last = result;
    }
    return result;
}

var times = 40;
var start = new Date().getTime();
console.log(recurFib(times));
var stop = new Date().getTime();
console.log("递归计算耗时：" + (stop - start) + " 毫秒");
console.log()

start = new Date().getTime();
console.log(dynFib(times));
stop = new Date().getTime();
console.log("动态规划耗时：" + (stop - start) + " 毫秒。");

start = new Date().getTime();
console.log(iterFib(times));
stop = new Date().getTime();
console.log("迭代版的动态规划耗时：" + (stop - start) + " 毫秒。");