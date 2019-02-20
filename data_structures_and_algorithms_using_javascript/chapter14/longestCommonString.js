// 寻找最长公共子串

function lcs(word1, word2) {
    var max = 0;
    var index = 0;
    var lcsarr = new Array(word1.length + 1);
    for (let i = 0; i <= word1.length + 1; ++i) {
        lcsarr[i] = new Array(word2.length + 1);
        for (let j = 0; j <= word2.length + 1; ++j) {
            lcsarr[i][j] = 0;
        }
    }

    for (let i = 0; i <= word1.length; ++i) {
        for (let j = 0; j <= word2.length; ++j) {
            if (i == 0 || j == 0) {
                lcsarr[i][j] == 0;
            } else {
                if (word1[i - 1] == word2[j - 1]) {
                    lcsarr[i][j] = lcsarr[i - 1][j - 1] + 1;
                } else {
                    lcsarr[i][j] = 0;
                }
            }
            if (max < lcsarr[i][j]) {
                max = lcsarr[i][j];
                index = i;
            }
        }
    }
    var str = "";
    if (max == 0) {
        return "";
    } else {
        for (let i = index - max; i <= max; ++i) {
            str += word2[i];
        }
        return str;
    }
}

var w1 = "abbcc";
var w2 = "dbbcc";
console.log(lcs(w1, w2));