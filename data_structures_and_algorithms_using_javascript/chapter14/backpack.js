// 背包问题：如何使装进背包的物品价值最大化

const process = require("process");

function max(a, b) {
    return (a > b) ? a: b;
}

function knapsack(capacity, size, value, n) {
    if (n == 0 || capacity == 0) {
        return 0;
    }
    if (size[n - 1] > capacity) {
        return knapsack(capacity, size, value, n - 1);
    } else {
        return max(value[n - 1] + 
                   knapsack(capacity - size[n - 1], size, value, n - 1),
                   knapsack(capacity, size, value, n - 1));
    }
}


// 动态规划法解决背包问题
function dKnapsack(capacity, size, value, n) {
    var K = [];
    for (let i = 0; i <= capacity + 1; i++) {
        K[i] = [];
    }
    for (let i = 0; i <= n; i++) {
        for (let w = 0; w <= capacity; w++) {
            if (i == 0 || w == 0) {
                K[i][w] = 0;
            } else if (size[i - 1] <= w) {
                K[i][w] = max(value[i - 1] + K[i - 1][w - size[i - 1]], K[i - 1][w]);
            } else {
                K[i][w] = K[i - 1][w];
            }
            process.stdout.write(K[i][w] + " ");
        }
        console.log();
    }
    return K[n][capacity];
}

var value = [4, 5, 10, 11, 13];
var size = [3, 4, 7, 8, 9];
var capacity = 16;
var n = 5;
console.log("递归解决背包问题：")
console.log(knapsack(capacity, size, value, n));
console.log();
console.log("动态规划解决背包问题：")
console.log(dKnapsack(capacity, size, value, n));