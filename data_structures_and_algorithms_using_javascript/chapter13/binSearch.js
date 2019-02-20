// 二分查找算法


// 插入排序算法
function insertionSort(arr) {
    var temp, inner;
    for (let outer = 1; outer <= arr.length - 1; ++outer) {
        temp = arr[outer];
        inner = outer;
        while (inner > 0 && (arr[inner - 1] >= temp)) {
            arr[inner] = arr[inner - 1];
            --inner;
        }
        arr[inner] = temp;
    }
}

function binSearch(arr, data) {
    var upperBound = arr.length - 1;
    var lowerBound = 0;
    while (lowerBound <= upperBound) {
        var mid = Math.floor((upperBound + lowerBound) / 2);
        console.log("当前的中点：" + mid);
        if (arr[mid] < data) {
            lowerBound = mid + 1;
        } else if (arr[mid] > data) {
            upperBound = mid - 1;
        } else {
            return mid;
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


// 统计重复次数
function count(arr, data) {
    var count = 0;
    var position = binSearch(arr, data);
    if (position > -1) {
        ++count;
        for (let i = position - 1; i > 0; --i) {
            if (arr[i] == data) {
                ++count;
            } else {
                break;
            }
        }
        for (let i = position + 1; i < arr.length; ++i) {
            if (arr[i] == data) {
                ++count;
            } else {
                break;
            }
        }
    }
    return count;
}

var nums = [];
for (var i = 0; i < 100; ++i) {
    nums[i] = Math.floor(Math.random() * 101);
}

insertionSort(nums);
dispArr(nums);
console.log();
console.log("输入一个要查找的值： ");
var val = "37";
console.log(val);
var retVal = binSearch(nums, val);
if (retVal >= 0) {
    console.log("已找到 " + val + "，所在位置为：" + retVal);
} else {
    console.log(val + " 没有出现在这个数组中。");
}
console.log();

// 使用 count 函数
console.log("输入一个要计数的值： ");
val = "45";
console.log(val);
retVal = count(nums, val);
console.log("找到了 " + retVal + " 次重复出现的 " + val + "。");