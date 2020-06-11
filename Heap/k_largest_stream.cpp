void kthLargest(int arr[], int n, int k)
{
    int i=0;
    priority_queue <int , vector<int> , greater<int>> pq;
    while(i<n)
    {
      if(pq.size()<k)
      { 
          pq.push(arr[i]);
          if(pq.size()==k)
          cout<<pq.top()<<" ";
          else
              cout<<"-1 ";
      }
      else if(pq.size()==k && arr[i]>pq.top()){   
        pq.pop();
        pq.push(arr[i]);
        cout<<pq.top()<<" ";
      }
     else if(pq.size()==k && arr[i]<=pq.top())
     {
         cout<<pq.top()<<" ";
     }
       
       i++;
    }
}