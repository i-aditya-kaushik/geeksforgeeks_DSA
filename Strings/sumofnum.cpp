#include<vector>
#include<string>
int findSum(string str)
{
	
	vector<string> s;
	int answer=0;
	string ans="";
	for(int i=0;i<str.length();i++){
	    if(str[i]>='0' && str[i]<='9'){
	        ans+=str[i];
	    }
	    if(ans==""){
	        continue;
	    }
	    if(str[i]>='a'&&str[i]<='z'){
	        s.push_back(ans);
	        ans="";
	        continue;
	    }
	    if(i==str.length()-1){
	        s.push_back(ans);
	    }
	}
	for(string x:s){
	    answer+= stoi(x);
	}
	return(answer);
	
}