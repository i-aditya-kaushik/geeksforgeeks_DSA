int floor(Node* root, int input) 
{ 
	if(root==NULL) return INT_MAX;

    if(root->data==input)
    return root->data;
    
    if(root->data > input)
    return floor(root->left, input);
    
    int flr = floor(root->right, input);
    return(flr<=input && flr!=-1) ? flr:root->data; 
}
