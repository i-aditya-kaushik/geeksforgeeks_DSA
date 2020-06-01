int ct=0;
unordered_set<int> kdl(Node * node,int i,int k)
{
    unordered_set <int> l;
    unordered_set <int> r;
    if (node==NULL) return l;
    l=kdl(node->left,i+1,k);
    r=kdl(node->right,i+1,k);
    l.insert(r.begin(),r.end());
    if (l.empty()) l.insert(i-k);
    if (l.find(i)!=l.end()) ct++;
    return l;
}
int printKDistantfromLeaf(Node* node, int k)
{
	ct=0;
	if (!node) return 0;
	kdl(node,1,k);
	return ct;
}