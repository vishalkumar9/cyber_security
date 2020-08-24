#include<bits/stdc++.h>
using namespace std;
int main(){
    string s;
    cout<<"enter a sring\n";
    cin>>s;
    int i=0,j=s.length()-1;
    int f=0;
     while(i<j){
         if(s[i]==s[j])i++,j--;
         else {
             f=1;
             break;
         }
     }
   if(f==1)cout<<"STRING IS NOT PALINDROME";
   else cout<<"STRING IS PALINDROME";
    return 0;
}

