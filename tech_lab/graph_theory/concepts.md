[//]: # (本文的概念定义源自于我本人对于Combinatorics and Graph Theory一书里概念的再理解，可能有谬误，欢迎指正，联系电邮: zengjuchen@gmail.com)

**V**:  vertex(plural vertices)

**E**:  edges, unordered pairs of vertices

**directed graph/digraph**:  A graph whose edges have direction. [Picture of digraph.](./pictures/digraph.png)

**multigraph**:  A graph whose set E allow repeated elements, technically we do that by replacing E with a mulitiset. [Definition of multiset](https://en.wikipedia.org/wiki/Multiset) || [Picture of multigraph.](./pictures/multigraph.png)

**pseudograph**:  A graph whose edge can connect a vertice to itself(This connection is called a loop). [Picture of pseudograph.](./pictures/pseudograph.png)

**hypergraph**:  A graph whose edge can include arbitary vertices(from 1 to inf.). [Picture of hypergraph.](./pictures/hypergraph.png)

**infinitegraph**:  A graph whose E and V is infinite set.

**loop**:  A edge that connect a vertice to itself.

**order**:  The total vertice number of a graph.

**size**:  The total edge number of a graph.

**neighborhood/open neighborhood**:  All the vertices who has a edge connected to the specified vertice.  
Denoted as `N(v) = {x ∈ V | vx ∈ E}`, v can be a single vertice or a set of vertices.

**closed neighborhood**:  A vertice's open neighborhood plus itself.  
Denoted as `N[v] = {v} ∪ N(v)`, v can be a single vertice or a set of vertices.

**degree**:  The number of edges incident(have relationship) with a vertice, denoted as `deg(v)`.  
The maximum degree of a graph G is `Δ(G) = max{deg(v) | v ∈ V(G)}`  
The minimum degree of a graph G is `δ(G) = min(deg(v) | v ∈ V(G)}`  

**degree sequence**:  An n-item sequence lists the degrees of all vertices in graph, often with descending order.

**walk**:  A sequence of vertices(not necessarily distinct) in which each adjacent vertices has an edge from the previous vertice to next vertice.  
Has a edege between two vertices is not a sufficient condition here, because we need to consider edges with directions.

**path**:  A walk with distinct vertices.

**trail**:  A walk with distinct edges.  
Every path is a trail, but not every trail is a path. Considering oriented edges case such as: `a -> b -> a`

**cycle/closed path**:  A path `v1, ..., vk(k >= 3)` plus the edge `vk-v1`.  
In another word, a cycle is a path with an extra edge which connects path's end vertice with the path's start vertice.  

**circuit/closed trail**:  A trail that starts and ends at the same vertice.

**length of walk/path/trail/cycle/circuit**  The edge numbers of that walk, counting repeatitions.

**vertex deletion**:  `G - v` denotes a new graph by removing vertice v and all edges incidents with v from G.  
If S is a set of vertices, `G - S` denotes the new graph by removing each vertex of `S` from `G` and all releated edges.

**edge deletion**:  `G - e` denotes a new graph by removing edge `e`(keep the vertice) from G.

**connected graph**:  Every vertice of the graph can be joined by a path.

**connected component/component**:  A maximal connected piece in a graph, a graph could have 1 or more `connected component`.

**cut vertex**:  If the deletion of a vertex causes the number of component of graph to increase, we call this vertex a `cut vertex`

**cut set**:  For a vertices set `S`, if `G - S` is disconnected, we call this set `S` a cut set.

**bridge**:  If the deletion of an edge causes graph components number increased, we call this edge a bridge.

**complete graph**:  Every vertex is adjacent to every other vertex in the graph.  
Complete graph does not have any cut sets, because you can make it disconnected by remove vertices.  
Every non-complete graph has at least 1 cut set.

**connectivity**:  For non-complete graph `G`, the minimum size of its cut set is called its connectivity, denoted as `k(G)`.  
For a complete graph, its `k(G)` is `n - 1`, where n is its order.  
If G is disconnected, its connectivity is 0, since `G - {}` is disconnected.  
If G is connected, `1 <= k(G) <= n-2`.  
For a positive interger X, if `k(G) >= X`, we say graph `G` is `X-connected`, which reflects a graph's connection strength.  
`1-connecetd` simply means a graph is connected.

**empty graph**:  A graph with no edges.

**complements**:  Give a graph G, its complement is a graph with same vertices, but whose edges are all the edges that G doesn't have.

**regular graph**:  A graph whose all vertices have the same degree. G is said to be regular of degree r if all([deg(v) == r for v in G])
