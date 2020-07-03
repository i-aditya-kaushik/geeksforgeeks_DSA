string decodeHuffmanData(struct MinHeapNode* root, string s)
{
    MinHeapNode * t = root;
    string ans;
    for(int i = 0;i < s.length();i++)
    {
        if(s[i] == '0')
            t = t -> left;
        else
            t = t -> right;
        if(t -> data != '$')
        {
            string sp(1,t-> data);
            ans += sp;
            t = root;
        }
    }
    return ans;
}