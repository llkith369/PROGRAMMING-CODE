#include<iostream>
using namespace std;


int main()
{
    int a,b,c;
    cin>>a>>b>>c;

    if (a>b)
    {
        if (a>c)
        {
            cout<<"a is highest number"<<a<<endl;
        }
        else
        {
            cout<<"the a is greater than b not c"<<c<<endl;
        }
        
        
    }
    else if (b>a)
    {
        if (b>c)
        {
            cout<<"the b is highest number"<<b<<endl;
        }
        else
        {
            cout<<"the c is greater "<<c<<endl;
        }
        
    }
    
    return 0;
}
