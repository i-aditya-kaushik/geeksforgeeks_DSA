void levelOrder(Node* node)
{
    if (node == NULL) return;  
    queue<Node *> q;  
    q.push(node);  
  
    while (q.empty() == false)  
    {  
        int nodeCount = q.size();  
        while (nodeCount > 0) 
        {  
            Node *n = q.front();  
            cout << n->data << " ";  
            q.pop();  
            if (n->left != NULL)  
                q.push(n->left);  
            if (n->right != NULL)  
                q.push(n->right);  
            nodeCount--;  
        }  
        cout << "$ ";  
    }  
}