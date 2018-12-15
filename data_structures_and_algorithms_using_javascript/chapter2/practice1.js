function grade() {
    this.grades = [];
    this.add = add;
    this.average = average;
}

function add(n) {
    this.grades.push(n);
}

function average() {
    var total = 0.0;
    for (let i = 0; i < this.grades.length; ++i) {
        total += this.grades[i];
    }
    return total / this.grades.length;
}

var stuGrade = new grade();
stuGrade.add(50);
stuGrade.add(80);
stuGrade.add(75);
console.log(stuGrade.average().toFixed(3));