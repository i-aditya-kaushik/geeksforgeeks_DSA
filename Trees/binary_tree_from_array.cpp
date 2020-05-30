Node *createTree(int parent[], int n)
{
    unordered_map<int,Node*> map;
    for(int i=0;i<n;i++)
    {
        Node* newnode = new Node(i);
        map[i] = newnode;
    }
    Node* root;
    for(int i=0;i<n;i++)
    {
        if(parent[i]==-1)
        {
            root = map[i];
            break;
        }
    }
    for(int i=0;i<n;i++)
    {
        if(parent[i]!=-1)
        {
            Node* temp = map[parent[i]];
            if(!temp->left)
            temp->left = map[i];
            else temp->right = map[i];
        }
    }
    return root;
}