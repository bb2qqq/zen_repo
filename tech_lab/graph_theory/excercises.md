### Basics
1. if G is a graph of order n, what is the maximum number of edges in G?

    A:
    If G is infinite graph or multigraph, the answer is infinite.
    If G is normal graph, from the first vertice you can develop (n-1) new edges,  
    then develop (n-2) new edges from the second vertice, and get totally (n-1) + (n-2) + ... + 2 + 1 edges.  
    which is ((n-1)(n-1+1))/2 = (n-1)*n/2
    If G is digraph, we have double edge numbers than normal graph, which is n*(n-1).

<br/>

2. Prove that for any graph G with order equal or greater than 2, the degree sequence has at leasst one pair of repeated entries.

A:

<br/>

3. Consider the graph shown in [Picture](./pictures/base_ques3.png)
    (a) How many different paths have c as an end vertex?  
    (b) How many different paths avoid vertex c altogether?  
    (c) What is the maximum length of a circuit in this graph?  
        Give an example of such a circuit.  
    (d) What is the maximum length of a circuit that does not include vertex c?
        Give an example of such a circuit.

A:

<br/>

4. Is it ture that a finite graph having exactly two vertices of odd degree must contain a path from one to the other?  
   Give a proof or a counterexample.

<br/>

5. Let G be a graph where minimum degree δ(G) >= k.  
    (a) Prove that G has a path of length at least k.  
    (b) If k >= 2, prove that G has a cycle of length at least k + 1.


<br/>

6. Prove that every closed odd walk in a graph contains an odd cycle.

<br/>

7. Draw a connected graph having at most 10 vertices that has at least 1 cycle of each length from 5 through 9, but has no cycles of any other length.

<br/>

8. Let P1 and P2 be two paths of maximum length in a connected graph G.
Prove that P1 and P2 have a common vertex.

<br/>

9. Let G be a graph of order n that is not connected. What is the maximum size of G?  

A: An un-connected graph has at least 2 component, the minimum component is a single vertice. So to maximize the degree of the graph, the left another component shall be complete connected.  
With the answer of question 1. We know the maximum edge for a simple graph with order n is n(n-1)/2, so the edges of the left component is (n-1)(n-1 -1)/2 = (n-1)(n-2)/2.  
Since there is no edge between two components.  
The maximum size for an un-connected graph is (n-1)(n-2)/2

<br/>

10. Let G be a graph of order n and size strictly less than n - 1, Prove that G is not connected.

A: By definition a connected graph is a graph whose every vertice can be joined by a path.  
This path has n vertices, as a distinct vertice sequence, it requires at least n -1 edges to connect each vertices.  
With less than n - 1 edges(size <= n-1), some vertice will be disconnected with others.  
Which menas the graph is not connected.  

<br/>

11. Prove that an edge e is a bridge of G if and only if e lies on no cycle of G.

A: By remove a small piece of line from a cycle, you got a curve, which is still a single component.  
So by definition, a bridge can't be in any cycle.  
For a edge not in any cycle of a graph, we can conclude it was on some curve path in which by extend it as far as possible it can't cross itself.  
By remove a small piece of line from a curve without cross point. you got two components.  
Thus if an edge is not in any cycle of a graph, it is a bridge.

<br/>

12. Prove or disprove each of the following statements  
(a) If G has no bridges, then G has exactly one cycle.  
(b) If G has no cut vertices, then G has no bridges.  
(c) If G has no bridges, then G has no cut vertices.  

A:
(a) Disprove, G can be a graph with two component, each component is a cycle. Thus G got two cycles with no bridges.  
(b) Disaprove, for a 2-vertice-1-edge graph, it has no cut vertice, but has a bridge.  
(c) Disaprove, imagine a graph is composed by 2 cycles which shares a common joint vertex. This graph has no bridge, but obviously this joint vertice is a cut vertice

<br/>

13. Prove or disprove: If every vertex of a connected graph G lies on at least one cycle, then G is 2-connected.  

A: Disaprove, if a graph is composed by 2 cycles which shares a common joint vertex. It satisfied the conditions in the question, but it is 1-connecetd, because the minimum cut set is {single joint vertice}.

<br/>

14. Prove that every 2-connected graph contains at least one cycle.

A: By definition, a graph with connectivity 2 is a connected graph.  
Assume it doesn't have any cycle, then it is a curve which doesn't cross any point of itself.  
For such a curve, delete any vertice in the middle of it will increase its component number, thus its connectivity is 1.  
Which counter the fact that it is 2-connected.  
So a 2-connected graph must contains at least one cycle.

<br/>

15. Prove that for every graph G,  
    (a) k(G) <= δ(G)  
    (b) if δ(G) >= n - 2, then k(G) = δ(G)

A:
(a): In any graph, if we delete all vertices connected to the minimum degree vertice, we will cause the component number to increase. At this moment, we deleted δ(G) vertices, according to definition of connectivity, k(G) must be <= δ(G).  
(b): if δ(G) >= n - 2, let's delete arbitrary n - 3 vertices in the graph, and we got 3 vertices left.  
These three nodes each have at least 1 edge remains.  
δ(G) >= n-2 means they all connected to at least n - 2 different nodes. remove n - 3 nodes, they each at still have connection with at least another node.  
Which means these three nodes are still connected.  
So, we need to remove at least n - 2 vertices which connects to the vertice with degree n - 2, to got a component increasement.  
Which means, k(G) = n - 2. [If the cut set size is n - 1, a single vertice is left, the component number won't increase]

<br/>

16. Let G be a graph of order n.
    (a) if δ(G) >= (n-1)/2, then prove that G is connected.
    (a) if δ(G) >= (n-2)/2, then prove that G could be un-connected.
