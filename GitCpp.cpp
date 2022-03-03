#include <iostream>
using namespace std;

int main(){
    int n  = 11, i=0, sum = 0;
    loop:
    if(i==11) goto skip;
    sum = sum + i;
    i = i + 1;
    goto loop;
    skip:
    cout<<sum;
    
}