/*
You are given a string (you need to take it input from user), the task is to encrypt this string
using # and $ symbols, alternatively. While encrypting the message the encrypted format must repeat
the symbol as many times as the letter position in alphabetical order (consider the string as case
insensitive).
*/
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
         return 0;
     }
