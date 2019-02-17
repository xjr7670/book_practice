// 图和图算法

const process = require("process");

function Vertex(label) {
    this.label = label;
}

// 构建图
function Graph(v) {
    this.vertices = v;
    this.edges = 0;
    this.adj = [];
    for (let i = 0; i < this.vertices; ++i) {
        this.adj[i] = [];
        this.adj[i].push("");
    }
    this.addEdge = addEdge;
    //this.toString = toString;
    this.showGraph = showGraph;
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

// 测试
g = new Graph(5);
g.addEdge(0, 1);
g.addEdge(0, 2);
g.addEdge(1, 3);
g.addEdge(2, 4);
g.showGraph();