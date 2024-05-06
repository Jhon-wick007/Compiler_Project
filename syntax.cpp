#include <bits/stdc++.h>

using namespace std;
 
// Tree Structure

typedef struct node 
{
    char data;
    int val;
    string info;
    struct node *left, *right;
} * nptr;
 string x="";
// Function to create new node

nptr newNode(char c)
{

    nptr n = new node;
    if(isalnum(c)){
         n->val=int(c)-48;
         }
    n->data = c;
    n->info=c;
    n->left = n->right = nullptr;

    return n;
}
 
// Function to build Expression Tree
nptr build(string& s)
{
 

    // Stack to hold nodes

    stack<nptr> stN;
 

    // Stack to hold chars

    stack<char> stC;

    nptr t, t1, t2;
 

    // Prioritising the operators

    int p[123] = { 0 };

    p['+'] = p['-'] = 1, p['/'] = p['*'] = 2, p['^'] = 3,

    p[')'] = 0;
 

    for (int i = 0; i < s.length(); i++) 

    {

        if (s[i] == '(') {
 

            // Push '(' in char stack

            stC.push(s[i]);

        }
 

        // Push the operands in node stack

        else if (isalnum(s[i])) 

        {

            t = newNode(s[i]);

            stN.push(t);

        }

        else if (p[s[i]] > 0) 

        {

            // If an operator with lower or

            // same associativity appears

            while (

                !stC.empty() && stC.top() != '('

                && ((s[i] != '^' && p[stC.top()] >= p[s[i]])

                    || (s[i] == '^'

                        && p[stC.top()] > p[s[i]]))) 

            {
 

                // Get and remove the top element

                // from the character stack

                t = newNode(stC.top());

                stC.pop();
 

                // Get and remove the top element

                // from the node stack

                t1 = stN.top();

                stN.pop();
 

                // Get and remove the currently top

                // element from the node stack

                t2 = stN.top();

                stN.pop();
 

                // Update the tree

                t->left = t2;

                t->right = t1;
 

                // Push the node to the node stack

                stN.push(t);

            }
 

            // Push s[i] to char stack

            stC.push(s[i]);

        }

        else if (s[i] == ')') {

            while (!stC.empty() && stC.top() != '(') 

            {

                t = newNode(stC.top());

                stC.pop();

                t1 = stN.top();

                stN.pop();

                t2 = stN.top();

                stN.pop();

                t->left = t2;

                t->right = t1;

                stN.push(t);

            }

            stC.pop();

        }

    }

    t = stN.top();

    return t;
}
 
// Function to print the post order
// traversal of the tree

void postorder(nptr root)
{

    if (root) 

    {

        postorder(root->left);

        postorder(root->right);

        cout << root->data<<".val="<<root->val<<endl;
        
        x+=root->data;

    }
}

int toInt(string s) 
{ 

    int num = 0; 

         

    // Check if the integral value is 

    // negative or not 

    // If it is not negative, generate the number 

    // normally 

    if(s[0]!='-') 

        for (int i=0; i<s.length(); i++) 

            num = num*10 + (int(s[i])-48); 

    // If it is negative, calculate the +ve number 

    // first ignoring the sign and invert the 

    // sign at the end 

    else

    { 

      for (int i=1; i<s.length(); i++) 

        num = num*10 + (int(s[i])-48); 

      num = num*-1; 

    } 

     

    return num; 
} 
 
// This function receives a node of the syntax tree 
// and recursively evaluates it 

int eval(node* root) 
{ 

    // empty tree 

    if (!root) 

        return 0; 
 

    // leaf node i.e, an integer 

    if (!root->left && !root->right) 

        return toInt(root->info); 
 

    // Evaluate left subtree 

    int l_val = eval(root->left); 

    // Evaluate right subtree 

    int r_val = eval(root->right); 
 

    // Check which operator to apply 

    if (root->info=="+") 

        return root->val= l_val+r_val; 
 

    if (root->info=="-") 

        return root->val=l_val-r_val; 
 

    if (root->info=="*") 

        return root->val=l_val*r_val; 
 

    return root->val=l_val/r_val; 
}
 
// Driver code

int main()
{

    string s ;
    cin>>s;

    s = "(" + s;

    s += ")";

    nptr root = build(s);
 cout<<eval(root)<<endl;
   

    // Function call

    postorder(root);
 cout<<x<<endl;

    return 0;
}
