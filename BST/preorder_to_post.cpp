#include<bits/stdc++.h>
using namespace std;

struct node
{
    int data;
    struct node *left;
    struct node *right;
};

struct node *root=NULL;

void inorder(struct node *root)
{
    if(root==NULL) return;

    else{
        inorder(root->left);
        cout<<root->data<<" ";
        inorder(root->right);
    }
}

void postorder(struct node *root)
{
    if(root==NULL){
        return;
    }

    else{
        postorder(root->left);
        postorder(root->right);
        cout<<root->data<<" ";
    }
}

void add(int ele)
{
    struct node *newnode;
    newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = ele;
    newnode->left = NULL;
    newnode->right = NULL;
    if(root == NULL){
        root = newnode;
    }

    else{
        struct node *temp = root;
        while(1){
            if(temp->data > ele){
                if(temp->left!=NULL){
                    temp = temp->left;
                }

                else{
                    temp->left = newnode;
                    break;
                }
            }

            else{
                if(temp->right != NULL){
                    temp = temp->right;
                }
                else{
                    temp->right = newnode;
                    break;
                }
            }
        }
    }
}

int main()
{
    int nooftestcases;
    cin>>nooftestcases;

    while(nooftestcases--){
        int n;
        cin>>n;

        int a[n];
        for(int i=0;i<n;i++) cin>>a[i];

        for(int i=0;i<n;i++){
            add(a[i]);
        }
        postorder(root);
        cout<<endl;
        root=NULL;
    }
}