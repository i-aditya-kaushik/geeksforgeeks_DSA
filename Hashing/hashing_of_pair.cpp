int sumExists(int arr[], int sizeOfArray, int sum)
{
   unordered_set<int> s;
   for(int i=0;i<sizeOfArray;i++){
       if(s.find(sum-arr[i])!=s.end()){
           return(1);
       }
       s.insert(arr[i]);
   }
   return(0);
}