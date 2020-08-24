/*
  Write a C/C++ program that takes n number of command line arguments and finds the least number.
In case of invalid entered value, prompt the user to enter another value.  
 */   
#include<iostream>
using namespace std;
int main(int argc,char** argv){
    cout<<"you have entered "<<argc<<" argumnets:"<<"\n";
    for(int i=0;i<argc;i++){
        cout<<argv[i]<<"\n";
    }
}
