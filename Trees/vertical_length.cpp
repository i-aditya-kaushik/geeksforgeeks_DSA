void getlength(Node* root,int &max, int &min,int curr){
    if(root==NULL){
        return;
    }
    getlength(root->left,max,min,curr-1);
    if(curr<min){
        min = curr;
    }
    if(curr>max){
        max=curr;
    }
    getlength(root->right,max,min,curr+1);
}
// your task is to complete this functionh
// function should return the width of the tree
int verticalWidth(Node* root)
{
    int maximum = 0; int minimum = 0;
    if(root==NULL){
        return(0);
    }
    getlength(root,maximum, minimum,0);
    return(abs(minimum)+maximum+1);
}