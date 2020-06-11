void FindMedian::insertHeap(int &x)
{
	if(max.empty()==true || x <= max.top())
        max.push(x);
    else
        min.push(x);
    balanceHeaps();
}

// Function to balance heaps
void FindMedian::balanceHeaps()
{
	if(max.size()>min.size()+1)
    {
        min.push(max.top());
        max.pop();
    }
    else if(min.size()>max.size())
    {
        max.push(min.top());
        min.pop();
    }
}

// Function to return getMedian
double FindMedian::getMedian()
{
	if(min.size()==max.size()){
	   // cout<<min.top()<<" "<<max.top()<<endl;
        return (min.top()+max.top())/2;
	}
// 	cout<<max.top()<<endl;
    return max.top();
}
