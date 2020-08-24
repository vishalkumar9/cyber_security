#include<bits/stdc++.h>
using namespace std;
int main(){
    int a,b;
 cout<<"enter the range a and b in which u have to find prime numbers\n";
 cin>>a>>b;
  int prime[b+1]={0};
  prime[0]=1;
   for(int i=2;i<=b;i++){
       if(prime[i]==0){
           for(int j=i*i;j<=b;j+=i){
               prime[j]=1;
           }
       }
   }
   cout<<"prime number in the range is display below\n";
   for(int i=a;i<=b;i++){
       if(prime[i]==0)
       cout<<i<<" ";
   }
  return 0;
}
