string largestNumber(int n, int sum){
    string str="";
    if(n*9<sum){
        return "-1";
    }
    for(int i=0;i<n;i++){
        int dig = 9;
        while(dig>=0){
            if(sum-dig>=0){
                str+= to_string(dig);
                sum-= dig;
                break;
            }
            dig--;
        }
    }
    return str;
}