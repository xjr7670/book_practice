// 自组织方式优化查找

function swap(arr, index, index1) {
    var temp = arr[index];
    arr[index] = arr[index1];
    arr[index1] = temp;
}

function seqSearch(arr, data) {
    for (let i = 0; i < arr.length; ++i) {
        if (arr[i] == data) {
            if (i > 0) {
                swap(arr, i, i-1);
            }
            return true;
        }
    }
    return false;
}

// 改进版的
function advSeqSearch(arr, data) {
    for (let i = 0; i < arr.length; ++i) {
        if (arr[i] == data && i > (arr.length * 0.2)) {
            swap(arr, i, 0);
            return true;
        } else if (arr[i] == data) {
            return true;
        }
    }
    return false;
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

var numbers = [5, 1, 7, 4, 2, 10, 9, 3, 6, 8];
console.log(numbers);
for (let i = 1; i <= 3; i++) {
    seqSearch(numbers, 4);
    console.log(numbers);
}

// 测试改进版的查找
var nums = [];
for (let i = 0; i < 10; i++) {
    nums[i] = Math.floor(Math.random() * 11);
}
dispArr(nums);
console.log();
console.log("请输入一个要查找的值：");
var val = "3"
console.log(val);
if (advSeqSearch(nums, val)) {
    console.log("找到了元素: ");
    console.log();
    dispArr(nums);
} else {
    console.log(val + " 没有出现在这个数组中。")
}