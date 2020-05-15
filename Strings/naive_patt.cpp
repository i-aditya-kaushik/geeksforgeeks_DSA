bool search(string pat, string txt) 
{ 
	
	int n = txt.length();
	int m = pat.length();
	int j=0;
	for(int i=0;i<n;i++){
	    if(txt[i]==pat[j]){
	        j++;
	    }
	    else{
	        j=0;
	    }
	    if(j==m){
	        return(1);
	    }
	}
	return(0);
	
}