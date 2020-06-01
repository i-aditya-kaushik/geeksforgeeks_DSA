vector <int> zigZagTraversal(Node* root)
{
	vector<int> a;
	stack<Node*> s1,s2;
	s1.push(root);
	while(!s1.empty() || !s2.empty()){
	    Node*temp;
	   if(!s1.empty()){
	       while(!s1.empty()){
	       temp=s1.top();
	       s1.pop();
	       a.push_back(temp->data);
	       if(temp->left)
	       s2.push(temp->left);
	       if(temp->right)
	       s2.push(temp->right);
	       }
	   }
	   else{
	       while(!s2.empty()){
	       temp=s2.top();
	       s2.pop();
	       a.push_back(temp->data);
	       if(temp->right)
	       s1.push(temp->right);
	       if(temp->left)
	       s1.push(temp->left);
	       }
	   }
	}
	return(a);
}