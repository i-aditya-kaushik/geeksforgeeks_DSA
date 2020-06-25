int minDistance(vector<int> dist, vector<bool> processed)
{
    int min = INT_MAX, min_index;
    
    for(int v = 0; v < dist.size(); v++)
    {
        if(!processed[v] && dist[v] <= min)
        {
            min = dist[v];
            min_index = v;
        }
    }
    
    return min_index;
}

vector <int>dijkstra(vector<vector<int>> graph, int src, int V)
{
    vector<int> dist(V);
    vector<bool> processed(V);
    
    fill(dist.begin(), dist.end(), INT_MAX);
    fill(processed.begin(), processed.end(), false);
    
    dist[src] = 0;
    
    for(int count = 0; count < V-1; count++)
    {
        int u = minDistance(dist, processed);
        
        processed[u] = true;
        
        for(int v = 0; v < V; v++)
        {
            if(!processed[v] && 
                graph[u][v] && 
                dist[u] != INT_MAX && 
                dist[u]+graph[u][v] < dist[v])
            {
                dist[v] = dist[u]+graph[u][v];
            }
        }
    }
    
    return dist;
}