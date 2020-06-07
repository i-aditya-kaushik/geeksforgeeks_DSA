//APPROACH 1:

map<int,unordered_set<int>> myfunc(Node*root, map<int,unordered_set<int>>& m, int lev){
    m[lev].insert(root->data);
    if(root->left) myfunc(root->left,m,lev-1);
    if(root->right) myfunc(root->right,m,lev+1);
    return(m);
}

// root: root node of the tree
void verticalOrder(Node *root)
{
    map<int,unordered_set<int>> m;
    if(!root){
        return;
    }
    m = myfunc(root,m,0);
    for(auto it=m.begin();it!=m.end();it++){
        for(auto it2 = it->second.begin(); it2!=it->second.end();it2++){
            cout<<*it2<<" ";
        }
    }
} 


//APPROACH 2:

void myfunc(Node* root) 
{ 
    if (!root) 
        return; 
   
    map < int,vector<int> > m; 
    int hd = 0; 
 
    queue<pair<Node*, int> > que; 
    que.push(make_pair(root, hd)); 
  
     while (!que.empty()) 
     { 
        pair<Node *,int> temp = que.front(); 
        que.pop(); 
        hd = temp.second; 
        Node* node = temp.first; 
  
        m[hd].push_back(node->data); 
  
        if (node->left != NULL) 
            que.push(make_pair(node->left, hd-1)); 
        if (node->right != NULL) 
            que.push(make_pair(node->right, hd+1)); 
    } 

    map< int,vector<int> > :: iterator it; 
    for (it=m.begin(); it!=m.end(); it++) 
    { 
        for (int i=0; i<it->second.size(); ++i) 
            cout << it->second[i] << " "; 
    } 
} 