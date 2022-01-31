public class Graph {

}

class DFS {

    List<Integer>[] graph = new ArrayList[];
    int n = 10; // no of nodes   

    void main() {

        boolean[] visited = new boolean[n];
        dfs(visited, 0);
    }

    void dfs(boolean[] visited, int node) {
        if (visited[node]) {
            return;
        }
        visited[node] = true;
        System.out.println(node);

        for (Integer child : graph.get(node)) {
            dfs(boolean[] visited, child);
        }
    }

}

class BFS {
    List<Integer>[] graph = new ArrayList[];
    int n = 10; // no of nodes   

    void main() {

    }

    void bfs(boolean[] visited) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(0);
        while (!queue.isEmpty()) {
            int node = queue.poll();
            visited[node] = true;
            for (int child : graph.get(node)) {
                if (!visited[child]) {
                    queue.add(child);
                }
            }
        }

    }

}


class CountNodeAtLevel {
    List<Integer>[] graph = new ArrayList[];
    int n = 10; // no of nodes   

    void main() {

    }

    void bfs(boolean[] visited) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(0);
        int level = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            System.out.println(level + " : " + size);

            for (int i=0; i<size; i++) {
                int node = queue.poll();
                System.out.println(node);
                visited[node] = true;
                for (int child : graph.get(node)) {
                    if (!visited[child]) {
                        queue.add(child);
                    }
                }
            }
            level++;
        }

    }
}


class ShortestPath {
    List<Integer>[] graph = new ArrayList[];
    int n = 10; // no of nodes   
    boolean[] visited = new boolean[n];

    Integer[] prev = new Integer[prev];

    void main(int start) {
        bfs(start);
        List<Integer> path = constructPath();
    }

    void bfs(int start) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        while (!queue.isEmpty()) {
            int node = queue.poll();
            for (int child : graph.get(node)) {
                if (!visited[child]) {
                    prev[child] = node;
                    queue.add(child);
                }
            }
        }

    }

    void constructPath(int start, int end) {
        List<Integer> path = new ArrayList<>();
        for (int node = end; node != null; node = prev[node]) {
            path.add(node);
        }
        Collections.reverse(path);
        if (path.get(0) == start) {
            return path;
        }
        return new ArrayList<Integer>();
    }
}



class TopologicalSort {
    List<Integer>[] graph = new ArrayList[];
    int n = 10; // no of nodes   
    boolean[] visited = new boolean[n];

    int orderIndex;

    void main() {
        int[] orderedNodes = new int[n];
        orderedNodes = orderedNodes.length-1;

        for (int node=0; node<n; i++) {
            if (!visited[node]) {
                orderedNodes = dfs(node, orderedNodes, orderIndex);
            }
        }
    }

    int dfs(int node, int[] orderedNodes, int orderIndex) {
        for (int child: graph.get(node)) {
            if (!visited[child]) {
                dfs(child, orderedNodes);
            }
        }
        orderedNodes[orderIndex] = node;
        return orderIndex - 1;
    }
}


// for longest path invert the weight 
// after calculation invert the distance array values
class SingleSourceShortestPath {  // O ( V * E )
    List<Edge> graph = new ArrayList<>();
    int n = 10; // no of nodes   
    boolean[] visited = new boolean[n];

    void main() {
        int[] orderedNode = topSort();
        Double[] distance = new Double[n];
        Arrays.fill(distance, Double.POSITIVE_INFINITY);
        distance[start] = 0;

        for (int nodeIndex : orderedNode) {
            for (Edge edge : graph.get(nodeIndex)) {
                Double newDistance = distance[nodeIndex] + edge.weight;
                distance[nodeIndex] = Math.min(distance[nodeIndex], newDistance);
            }
        }
    }
}


class Dijkshtra {  // O ( V * log(E) )
    List<Edge> graph = new ArrayList<>();
    int n = 10; // no of nodes   
    boolean[] visited = new boolean[n];

    void bfs(int start) {
        Double[] dist = new Double[n];
        Arrays.fill(dist, Double.POSITIVE_INFINITY);
        dist[start] = 0;

        Queue<Node> pq = new PriorityQueue<>((n1,n2) -> n1.weight-n2.weight);
        pq.add(new Pair(start, 0));

        while (!pq.isEmpty()) {
            Pair pair = pq.poll();
            visited[pair.node] = true;
            if (distance[pair.node]< pair.minDist) {
                continue;
            }
            for (Node child : graph[pair.node]) {
                if (visited[child.index]) {
                    continue;
                }
                Double newDistance = distance[pair.node] + child.weight;
                if (newDistance < distance[child.index]) {
                    distance[child.index] = newDistance;
                    pq.add(new Pair(child.index, newDistance));
                }
            }

        }
    }

    class Pair {
        int node;
        int minDist;
        Pair(int a, int b) {
            node = a;
            minDist = b;
        }
    }

    class Node {
        int index;
        int weight;
        Node(int i, int w) {
            index = i;
            weight = w;
        }
    }

}
