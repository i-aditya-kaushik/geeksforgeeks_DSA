void bottomView(Node *root)
{
  map<int,int>mp;
  queue<pair<Node*,int>>q;
  int hd=0;
  q.push(make_pair(root,hd));
  
  while(!q.empty()){
      pair<Node*,int>temp=q.front();
      q.pop();
      hd=temp.second;
      mp[hd]=temp.first->data;
      
      
      if(temp.first->left){
          q.push(make_pair(temp.first->left,hd-1));
      }
      if(temp.first->right){
          q.push(make_pair(temp.first->right,hd+1));
      }
  }
   map<int,int>:: iterator it;
      for(it=mp.begin();it!=mp.end();it++){
          cout<<it->second<<" ";
  }
}