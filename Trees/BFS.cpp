void levelOrder(Node* node)
{
    if(node==NULL){
      return;
    }
    queue<Node*> s,n;
    s.push(node);
    while(s.size()!=0){
      cout<<s.front()->data<<" ";
      if((s.front())->left !=NULL){
          s.push(s.front()->left);
      }
      if((s.front())->right !=NULL){
          s.push(s.front()->right);
      }
      s.pop();
    }
}