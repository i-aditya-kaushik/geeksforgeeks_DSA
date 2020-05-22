class Geeks
{
    //Complete this function
    public Stack<Integer> deleteMid(Stack<Integer>s,int sizeOfStack,int current)
    {
        if (current == sizeOfStack){
            return s;
        }
       int x = s.peek(); 
       s.pop(); 
       deleteMid(s, sizeOfStack, current+1); 
       if (current != Math.floor(sizeOfStack/2.0)){s.push(x);}
       return s;
    } 
}