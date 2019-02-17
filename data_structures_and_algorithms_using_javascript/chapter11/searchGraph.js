// 搜索图

// 引入 process 模块，方便对输出进行控制
const process = require("process");

function Vertex(label) {
    this.label = label;
}

// 构建图
function Graph(v) {
    this.vertices = v;
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
}

function addEdge(v, w) {
    this.adj[v].push(w);
    this.adj[w].push(v);
    this.edges++;
}

// 显示图
function showGraph() {
    for (let i = 0; i < this.vertices; ++i) {
        process.stdout.write(i + " -> ");
        for (let j = 0; j < this.vertices; ++j) {
            if (this.adj[i][j] != undefined) {
                process.stdout.write(this.adj[i][j] + ' ');
            }
        }
        console.log();
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

// 测试 dfs
g = new Graph(5);
g.addEdge(0, 1);
g.addEdge(0, 2);
g.addEdge(1, 3);
g.addEdge(2, 4);
g.showGraph();
// g.dfs(0);
g.bfs(0);