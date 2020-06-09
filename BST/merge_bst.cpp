void func(Node *root1, map<int,int> &s)
{
   if(!root1) return;
   s[root1->data]++;
   if(root1->left) func(root1->left,s);
   if(root1->right) func(root1->right,s);
}

// Return a integer of integers having all the nodes in both the BSTs in a sorted order.
vector<int> merge(Node *root1, Node *root2)
{
   map<int,int> s;
   vector<int> v;
   func(root1,s);
   func(root2,s);
   for(auto it=s.begin(); it!=s.end(); it++){
       for(int i=0;i<it->second;i++) v.push_back(it->first);
   }
   return(v);
}