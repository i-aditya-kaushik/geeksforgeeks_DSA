void convert(Node *head, TreeNode *&root) {
    if(head==NULL)
        return;
    queue<TreeNode*> q;
    root=new TreeNode(head->data);
    q.push(root);
    if(head->next)
    {
        head=head->next;
        while(head!=NULL)
        {
            TreeNode * temp=q.front();
            q.pop();
            temp->left=new TreeNode(head->data);
            q.push(temp->left);
            if(head->next)
                head=head->next;
            else
                break;
            temp->right=new TreeNode(head->data);
            q.push(temp->right);
            if(head->next)
                head=head->next;
            else
                break;
        }
    }
    else return;
}