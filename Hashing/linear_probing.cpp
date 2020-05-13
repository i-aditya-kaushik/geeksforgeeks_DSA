#include <bits/stdc++.h>
using namespace std;


void linearProbing(int hash[],int hashSize,int arr[],int sizeOfArray);
int main() {
	int t;
	cin>>t;
	while(t--)
	{
	    int hashSize;
	    cin>>hashSize;
	    int hash[hashSize];
	    
	    
	    int  sizeOfArray;
	    cin>>sizeOfArray;
	    int arr[sizeOfArray];
	    
	    for(int i=0;i<sizeOfArray;i++)
	    cin>>arr[i];
	    
	    
	    
	    for(int i=0;i<hashSize;i++)
	    hash[i]=-1;
	    
	    linearProbing( hash, hashSize, arr, sizeOfArray);
	    
	    for(int i=0;i<hashSize;i++)
	    cout<<hash[i]<<" ";
	    
	    cout<<endl;
	    
	    
	}
	return 0;
}// } Driver Code Ends


//Complete this function
void linearProbing(int hash[],int hashSize,int arr[],int sizeOfArray)
{
    for(int i=0;i<sizeOfArray;i++){
        if(hash[arr[i]%hashSize]==-1){hash[arr[i]%hashSize] = arr[i];}
        else{
            int p = 1;
            Label:
                if(hash[(arr[i]+p)%hashSize]==-1){
                    hash[(arr[i]+p)%hashSize] = arr[i];
                    continue;
                }
                if(p==i){
                    break;
                }
                p++;
                goto Label;
        }
    }
}