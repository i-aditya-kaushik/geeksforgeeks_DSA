void connect(struct Node*p){
    if(p==NULL)
        return;
    queue<Node*>q;
    q.push(p);
    q.push(NULL);
    while(!q.empty())
    {
        Node* f=q.front();
        q.pop();
        if(f!=NULL)
        {
            f->nextRight=q.front();
            if(f->left)
                q.push(f->left);
            if(f->right)
                q.push(f->right);
        }
        else if(!q.empty())
        q.push(NULL);
    }
}