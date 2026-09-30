#include<bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin>>n;
    vector<long long>a(n);
    for(int i=0;i<n;i++)cin>>a[i];
    long long m=-1,sum=0;
    for(int i=0;i<n;i++){
        if(a[i]>=m){
            sum+=a[i];
            m=a[i];
        }
    }
    cout<<sum;
    return 0;
}