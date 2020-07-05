bool comp(Job a, Job b) 
{ 
     return (a.profit > b.profit); 
} 

pair<int,int> JobScheduling(Job arr[], int n) 
{ 
    sort(arr, arr+n, comp); 
  
    int result[n]; 
    bool slot[n];   
    for (int i=0; i<n; i++) 
        slot[i] = false; 
    for (int i=0; i<n; i++) 
    { 
       for (int j=min(n, arr[i].dead)-1; j>=0; j--) 
       { 
          if (slot[j]==false) 
          { 
             result[j] = i;  
             slot[j] = true; 
             break; 
          } 
       } 
    } 
    int c=0;
    int ans = 0;
    for (int i=0; i<n; i++){
       if (slot[i]){
           c+=1;
           ans+=arr[result[i]].profit;
       }
    }
    return make_pair(c,ans);
} 