int findCeil(Node* root, int input) 
{ 
    if (root == NULL) 
        return -1; 
  
    if (root->data == input) 
        return root->data; 
  
    if (root->data < input) 
        return findCeil(root->right, input); 
  
    int ceil = findCeil(root->left, input); 
    return (ceil >= input) ? ceil : root->data; 

    
    
} 