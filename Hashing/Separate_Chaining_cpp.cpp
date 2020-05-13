#include<bits/stdc++.h>

using namespace std;

void separateChaining(vector<vector<int>> &hashTable,int hashSize,int arr[],int sizeOfArray);

int main() {
	int t;
	cin>>t;
	while(t--)
	{
	    int hashSize;
	    cin>>hashSize;
	    vector<vector<int>> hashTable(hashSize);
	    
	    
	    int sizeOfArray;
	    cin>>sizeOfArray;
	    int arr[sizeOfArray];
	    
	    for(int i=0;i<sizeOfArray;i++)
	    cin>>arr[i];
	    
	    
	    
	    separateChaining( hashTable, hashSize, arr, sizeOfArray);
	    
	    for(int i=0;i<hashTable.size();i++)
	    {
	        if(hashTable[i].size()>0)
	        {
	            cout<<i<<"->";
	            for(int j=0;j<hashTable[i].size()-1;j++)
	            {
	                cout<<hashTable[i][j]<<"->";
	            }
	            cout<<hashTable[i][hashTable[i].size()-1];
	            cout<<endl;
	        }
	    }
	    
	    
	    
	}
	return 0;
}

void separateChaining(vector<vector<int>> &hashTable,int hashSize,int arr[],int sizeOfArray)
{
    // cout<<hashSize<<" "<<sizeOfArray<<endl;
  for(int i=0;i<sizeOfArray;i++){
      int a = arr[i]%hashSize;
      hashTable[a].push_back(arr[i]);
  }
}