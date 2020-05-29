bool check(struct Node * T, struct Node *S) 
{ 
    if (T == NULL && S == NULL) 
        return true; 
    if (T == NULL || S == NULL) 
        return false; 
    return (T->data == S->data  && check(T->left, S->left) && check(T->right, S->right) ); 
} 
  
  
bool isSubTree(Node *T, struct Node *S) 
{ 
    if (S == NULL) 
        return true; 
    if (T == NULL) 
        return false; 
    if (check(T, S)) 
        return true; 
    return isSubTree(T->left, S) || 
           isSubTree(T->right, S); 
} 