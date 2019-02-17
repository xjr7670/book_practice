const process = require("process");

// 顺序查找
function seqSearch(arr, data) {
    for (let i = 0; i < arr.length; ++i) {
        if (arr[i] == data) {
            return i;
        }
    }
    return -1;
}

// 显示数组
function dispArr(arr) {
    for (var i = 0; i < arr.length; ++i) {
        process.stdout.write(arr[i] + " ");
        if (i % 10 == 9) {
            process.stdout.write("\n");
        }
    }
    if (i % 10 != 0) {
        process.stdout.write("\n");
    }
}

var nums = [];
for (let i = 0; i < 100; ++i) {
    nums[i] = Math.floor(Math.random() * 101);
}
dispArr(nums);
console.log("输入一个要查找的数字：");
var num = 23;
console.log(num);
var position = seqSearch(nums, num);
if (position > -1) {
    console.log(num + " 出现在这个数组中，位置是：" + position);
} else {
    console.log(num + " 没有出现在这个数组中。");
}
console.log();
dispArr(nums);