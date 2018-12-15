// 7.1
// function fractorial(num) {
//     if (num <= 1) {
//         return 1;
//     } else {
//         return num * arguments.callee(num-1);
//     }
// }

// 7.2.1
// function createFunctions() {
//     var result = new Array();

//     for (var i = 0; i < 10; i++) {
//         result[i] = function() {
//             return i;
//         };
//     }

//     return result;
// }

// function createFunctions() {
//     var result = new Array();

//     for (var i = 0; i < 10; i++) {
//         result[i] = function(num) {
//             return function() {
//                 return num;
//             };
//         }(i);
//     }

//     return result;
// }

// 7.4
// function MyObject() {
//     var privateVariable = 10;

//     function privateFunction() {
//         return false;
//     }

//     this.publicMethod = function() {
//         privateVariable++;
//         return privateFunction();
//     };
// }

// function Person(name) {
//     this.getName = function() {
//         return name;
//     };

//     this.setName = function(value) {
//         name = value;
//     };
// }

// var person = new Person("Nicholas");
// alert(person.getName());
// person.setName("Greg");
// alert(person.getName());
