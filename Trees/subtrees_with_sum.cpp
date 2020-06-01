int res = 0;

int childSum(Node *root, int x)
{
    if(root == NULL)
    {
        return 0;
    }
    
    int lh = 0;
    if(root->left)
    {
        lh = childSum(root->left, x);
    }
    
    int rh = 0;
    if(root->right)
    {
        rh = childSum(root->right, x);
    }
    
    int sum = root->data + lh + rh;
    
    if(sum == x)
    {
        res++;
    }
    
    return sum;
}
int countSubtreesWithSumX(Node* root, int x)
{
    res = 0;
    childSum(root, x);
	return res;
}