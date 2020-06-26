#include<bits/stdc++.h>

using namespace std;

void dfs(int s, vector < int > adj[], bool vis[]) {
    vis[s] = true;
    for (int x: adj[s])
        if (vis[x] == false)
            dfs(x, adj, vis);

}

void fillorder(int s1, vector < int > adj[], bool vis[], stack < int > & s) {
    vis[s1] = true;
    for (int x: adj[s1]) {
        if (vis[x] == false)
            fillorder(x, adj, vis, s);
    }
    s.push(s1);
}

int kosaraju(int V, vector < int > adj[]) {
    stack < int > s;
    bool vis[V];
    memset(vis, false, sizeof(vis));
    for (int i = 0; i < V; i++)
        if (vis[i] == false)
            fillorder(i, adj, vis, s);
    memset(vis, false, sizeof(vis));
    vector < int > adj1[V];
    for (int i = 0; i < V; i++) {
        for (int x: adj[i])
            adj1[x].push_back(i);
    }

    int c = 0;
    while (!s.empty()) {
        int u = s.top();
        s.pop();

        if (vis[u] == false) {
            dfs(u, adj1, vis);
            c++;
        }

    }
    return c;

}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int a, b;
        cin >> a >> b;
        int m, n;
        vector<int> adj[a];
        for (int i = 0; i < b; i++) {
            cin >> m >> n;
            adj[m].push_back(n);
        }
        cout << kosaraju(a, adj) << endl;
    }
    return 0;
}