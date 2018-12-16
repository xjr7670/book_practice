const readline = require('readline');

function a() {
    const r1 = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    var ans = '222';
    r1.question("你认为怎么样、", (answer) => {
        console.log("thank you: ", answer);
        ans = answer;
        console.log("ans is: ", ans);
        r1.close();
    })
    return ans;
}

var n2=a();
console.log("n2 is: ", n2);