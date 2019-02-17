// 拓扑排序
// 查找最短路径

// 引入 process 模块，方便对输出进行控制
const process = require("process");

function Vertex(label) {
    this.label = label;
}

// 构建图
function Graph(v) {
    this.vertices = v;
    this.vertexList = [];
    this.edges = 0;
    this.edgeTo = [];
    this.adj = [];
    for (let i = 0; i < this.vertices; ++i) {
        this.adj[i] = [];
        this.adj[i].push("");
    }
    this.addEdge = addEdge;
    //this.toString = toString;
    this.showGraph = showGraph;
    this.dfs = dfs;
    this.bfs = bfs;
    // 用一个数组来存储已访问过的顶点
    this.marked = [];
    for (let i = 0; i < this.vertices; ++i) {
        this.marked[i] = false;
    }

    this.pathTo = pathTo;
    this.hasPathTo = hasPathTo;
    this.topSortHelper = topSortHelper;
    this.topSort = topSort;
}

function addEdge(v, w) {
    this.adj[v].push(w);
    this.adj[w].push(v);
    this.edges++;
}

// 显示符号名字而非数字的新函数
function showGraph() {
    var visited = [];
    for (let i = 0; i < this.vertices; ++i) {
        process.stdout.write(i + " -> ");
        visited.push(this.vertexList[i]);
        for (let j = 0; j < this.vertices; ++j) {
            if (this.adj[i][j] != undefined) {
                if (visited.indexOf(this.vertexList[j]) < 0) {
                    process.stdout.write(this.vertexList[j] + ' ');
                }
            }
        }
        console.log();
        visited.pop();
    }
}

// 深度优先算法
function dfs(v) {
    this.marked[v] = true;
    if (this.adj[v] != undefined) {
        console.log("Visited vertex: " + v);
    }
    for (let w in this.adj[v]) {
        if (!this.marked[this.adj[v][w]]) {
            this.dfs(this.adj[v][w]);
        }
    }
}

// 广度优先算法
function bfs(s) {
    var queue = [];
    this.marked[s] = true;
    queue.push(s);  // 添加到队尾
    while (queue.length > 0) {
        var v = queue.shift();  // 从队首移除
        if (v == undefined) {
            console.log("Visited vertex: " + v);
        }
        for (let i in this.adj[v]) {
            if (!this.marked[this.adj[v][i]]) {
                this.edgeTo[this.adj[v][i]] = v;
                this.marked[this.adj[v][i]] = true;
                queue.push(this.adj[v][i]);
            }
        }
    }
}

function hasPathTo(v) {
    return this.marked[v];
}

function pathTo(v) {
    var source = 0;
    if (!this.hasPathTo(v)) {
        return undefined;
    }
    var path = [];
    for (let i = v; i != source; i = this.edgeTo[i]) {
        path.push(i);
    }
    path.push(s);
    return path;
}



/****************** 拓扑排序算法 *****************************/
function topSort() {
    var stack = [];
    var visited = [];
    for (let i = 0; i < this.vertices; i++) {
        visited[i] = false;
    }
    for (let i = 0; i < this.vertices; i++) {
        if (visited[i] == false) {
            this.topSortHelper(i, visited, stack);
        }
    }
    for (let i = 0; i < stack.length; i++) {
        if (stack[i] != undefined && stack[i] != false) {
            console.log(this.vertexList[stack[i]]);
        }
    }
}

function topSortHelper(v, visited, stack) {
    visited[v] = true;
    for (let i in this.adj[v]) {
        if (!visited[this.adj[v][i]]) {
            this.topSortHelper(visited[v], visited, stack);
        }
    }
    stack.push(v);
}

// 查找一个顶点的最短路径
g = new Graph(6);
g.addEdge(1, 2);
g.addEdge(2, 5);
g.addEdge(1, 3);
g.addEdge(1, 4);
g.addEdge(0, 1);
g.vertexList = ["CS1", "CS2", "Data Structures", "Assembly Language", "Operating Systems", "Algorithms"];
g.showGraph();
g.topSort();