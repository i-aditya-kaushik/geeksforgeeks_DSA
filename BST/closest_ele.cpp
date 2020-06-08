int minDiff(Node *root, int k)
{
    queue<Node*>q;  vector<int>v;
    if(!root)  {return 0;}   
    q.push(root);
    while(!q.empty())
    {
    Node*temp=q.front(); q.pop();  v.push_back(temp->data);
    
    if(temp->left) q.push(temp->left);
    if(temp->right) q.push(temp->right);
    }
    int min=abs(k-v[0]);
    for(int i=0;i<v.size();i++)
    {
    int s=abs(k-v[i]); if(s<min){min=s;}
    }
     return min;
}