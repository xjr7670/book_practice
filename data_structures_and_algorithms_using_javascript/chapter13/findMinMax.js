// 13.1.1 查找最小值和最大值

// 查找最小值
function findMin(arr) {
    var min = arr[0];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] < min) {
            min = arr[i];
        }
    }
    return min;
}

// 查找最大值
function findMax(arr) {
    var max = arr[0];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
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


// 测试
var nums = [];
for (let i = 0; i < 100; ++i) {
    nums[i] = Math.floor(Math.random() * 101);
}

var minValue = findMin(nums);
dispArr(nums);
console.log();
console.log("最值值是：" + minValue);
var maxValue = findMax(nums);
console.log();
console.log("最大值是：" + maxValue);