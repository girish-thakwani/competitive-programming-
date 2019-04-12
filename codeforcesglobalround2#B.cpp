#include<iostream>
#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll sum(ll arr[],ll n){
        ll a[n];
        for(int i=0;i<n;i++)a[i]=arr[i];
        sort(a,a+n,greater<int>());
        ll s=0;
        for(int i=0;i<n;i+=2){s+=a[i];}
return s;
}
int main(){
        ll n,h,r,l;cin>>n>>h;r=h;l=h;
        ll arr[n];
        for(ll i=0;i<n;i++){
                cin>>arr[i];
        }
        ll i=n;
        while(sum(arr,i)>h){
                --i;
        }
        cout<<i;

return 0;}
