int fact(int n);

int fact(int n){
    int fact1=1;
    while(n!=1){
        fact1=fact1*n;
        n--;
    }
    return(fact1);
}

int findSmallerInRight(string str, int low, int high) 
{ 
    int counter = 0; 
    for (int i = low + 1; i <= high; ++i) 
        if (str[i] < str[low]) 
            ++counter; 
    return counter; 
} 

int findRank(string str) 
{
    int mul = fact(str.length()); 
    long long int rank = 1; 
    int countRight; 
    int i;
    map<int,int> s;
    for (i = 0; i < str.length(); ++i) { 
        s[str[i]]++;
        if(s[str[i]]>1){
            return(0);
        }
        mul /= str.length() - i; 
        countRight = findSmallerInRight(str, i, str.length() - 1); 
        rank += countRight * mul; 
    } 
    return rank%1000000007; 
}