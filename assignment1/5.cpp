#include<bits/stdc++.h>
using namespace std;
int main(){
    string s;
    cin>>s;
    char ch;
     transform(s.begin(),s.end(),s.begin(),::toupper);
     for(int i=0;i<s.length();i++){
         int k=(s[i]-64);
         if((i+1)%2!=0)ch='#';
         else ch='$';
         for(int j=1;j<=k;j++){
            cout<<ch;
         }
     }