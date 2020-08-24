/*
Write a C/C++ program to encrypt and decrypt the string using Caesar Cypher Algorithm. While
encrypting the given string, 5 is added to the ASCII value of the characters. Similarly, for decrypting the
string, 5 is subtracted from the ASCII value of the characters to print an original string. Example - Input
String - hello, Encrypted String - mjqqt
*/
#include<bits/stdc++.h>
using namespace std;
int main(){
    string s;
    cin>>s;
    int choice;
    cout<<"do you want to encrypt or decrypt(enetr 1 or 2 respectively)\n";
    cin>>choice;
    if(choice==1){
        for(int i=0;i<s.length();i++){
               s[i]=s[i]+5;
        }
    }
    else{
        for(int i=0;i<s.length();i++){
           s[i]=s[i]-5;
        }
    }
     cout<<"successfully done\n";
    cout<<s;
   return 0;
}
