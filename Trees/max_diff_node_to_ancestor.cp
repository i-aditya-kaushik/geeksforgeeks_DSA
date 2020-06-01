int maxDiffUtil(Node* t, int *res) 
{ 
    if (t == NULL) 
        return INT_MAX;
    if (t->left == NULL && t->right == NULL) 
        return t->data;
    int val = min(maxDiffUtil(t->left, res), 
                  maxDiffUtil(t->right, res)); 
    *res = max(*res, t->data - val);     
    return min(val, t->data); 
} 
  
int maxDiff(Node *root) 
{ 
    int res = INT_MIN; 
    maxDiffUtil(root, &res); 
    return res; 
} 