
def findAns(n,k,arrA):
    

    arrA.sort()
    index = None
    for i in range(len(arrA)):
        if arrA[i] >= k:
            index = i
            break
    
    return days











# for _ in range(int(input())):
#     n,k = int(input())

#     arrA = list(map(int,input().split()))


#     print(findAns(n,k,arrA))

for _ in range(1):
    n,k = 1,1

    arrA = [10,10,10]


    print(findAns(n,k,arrA))

# using namespace std;
 
# int32_t main()
# {
#  nitro;
#  //freopen("input.txt","r",stdin);
#  //freopen("output.txt","w",stdout);
#  int t;
#  cin>>t;
#  while(t--)
#  {
#     int n,x;
#     cin>>n>>x;
#     vector<int> v(n);
#     for(int& i:v)
#     cin>>i;
#     sort(v.begin(),v.end());
#     vector<int>::iterator it = lower_bound(v.begin(), v.end(), x);
#     int lb = it - v.begin();
#     int d=0;
#     for(int i=lb;i<n;i++)
#     {
#     	if(x<v[i])
#     	{
#     		while(x<v[i])
#     		{
#     			x=2*x;
#     			d++;
#     		}
#     		d++;
#     	}
#     	else
#     	d++;
#     	x=2*v[i];
#     }
#     int tot=lb+d;
#     if(lb!=0)
#     {
#     	d=0;
#     	lb--;
#     	for(int i=lb;i<n;i++)
#     	{
#     		if(x<v[i])
#     		{
#     			while(x<v[i])
#     			{
#     				x=2*x;
#     				d++;
#     			}
#     			d++;
#     		}
#     		else
#     		d++;
#     		x=2*v[i];
#     	}
#     	int ans=min(d+lb,tot);
#     	cout<<ans<<endl;
#     }
#     else
#     cout<<tot<<endl;
#  }
#  return 0;
# }