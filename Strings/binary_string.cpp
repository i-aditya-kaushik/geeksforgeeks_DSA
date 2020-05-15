long binarySubstring(int n, string a){
    long c=0;
    for(int i=0;i<n;i++){
        if(a[i]=='1'){
            c+=1;
        }
    }
    return((c*(c-1))/2);
}