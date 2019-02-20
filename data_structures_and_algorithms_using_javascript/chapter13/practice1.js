// 顺序查找，返回匹配到的最后一个元素


function seqSearch(arr, data) {
    for (let i = arr.length; i >= 0; --i) {
        if (arr[i] == data) {
            return i;
        }
    }
    return -1;
}