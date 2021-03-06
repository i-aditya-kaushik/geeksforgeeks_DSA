void serialize(Node *root,vector<int> &arr)
{
    if(root == NULL)
    {
        arr.push_back(-1);
        return;
    }
    
    arr.push_back(root->data);
    
    serialize(root->left,  arr);
    serialize(root->right, arr);
}

int indexArr = 0;
Node * deSerializeC(vector<int> &arr)
{
    
    
    if(arr.size() == indexArr)
    {
        return NULL;
    }
    
    int val = arr[indexArr];
    indexArr++;
    
    if(val == -1)
    {
        return NULL;
    }
    
    Node *root = new Node(val);
    
    root->left  = deSerializeC(arr);
    root->right = deSerializeC(arr);
    
    return root;
}

/*this function deserializes
 the serialized vector A*/
Node * deSerialize(vector<int> &arr)
{
   indexArr = 0;
   return deSerializeC(arr);
}