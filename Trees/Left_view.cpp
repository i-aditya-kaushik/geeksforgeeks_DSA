int leftmax = 0;
int max1 = 0;
// A wrapper over leftViewUtil()
void leftView(Node *root)
{
   if(!root){
       return;
   }
   if(leftmax<=max1){
    cout<<root->data<<" ";
    max1=leftmax;
   }
   if(root->left){leftView(root->left);leftmax+=1;}
   if(root->right){leftView(root->right);leftmax+=1;}
   leftmax= 0;
   max1=0;
}