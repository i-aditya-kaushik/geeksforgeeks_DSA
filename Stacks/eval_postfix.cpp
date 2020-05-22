int scanNum(char ch) {
   int value;
   value = ch;
   return int(value-'0');   
}

int isOperator(char ch) {
   if(ch == '+'|| ch == '-'|| ch == '*'|| ch == '/' || ch == '^')
      return 1;    
   return -1;   
}

int isOperand(char ch) {
   if(ch >= '0' && ch <= '9')
      return 1;    
   return -1;   
}

float operation(int a, int b, char op) {
   if(op == '+')
      return b+a;
   else if(op == '-')
      return b-a;
   else if(op == '*')
      return b*a;
   else if(op == '/')
      return b/a;
   else if(op == '^')
      return pow(b,a);    
   else
      return INT_MIN;   
}

// The main function that returns value of a given postfix expression
int evaluatePostfix(string &str)
{
   int a, b;
   stack<int> stk;

   for(auto it=str.begin(); it!=str.end(); it++) {
      if(isOperator(*it) != -1) {
         a = stk.top();
         stk.pop();
         b = stk.top();
         stk.pop();
         stk.push(operation(a, b, *it));
      }else if(isOperand(*it) > 0) {
         stk.push(scanNum(*it));
      }
   }
   return stk.top();
}