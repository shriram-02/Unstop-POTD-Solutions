#include <bits/stdc++.h>
using namespace std;
#define int long long
void find_shortest_distances(int n, int m, const std::vector<std::vector<int>>& connections) {
unordered_map<int,unordered_map<int,int>>mp;
for(auto it:connections){
    int a=it[0],b=it[1],c=it[2];
      if(mp[a].find(b)!=mp[a].end()){
      mp[a][b]=min(mp[a][b],c);
        }
          else{
          mp[a][b]=c;
            }
            }

            priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>>pq;
            pq.push({0,1});
            vector<int>dis(n+1,LLONG_MAX),vis(n+1,0);
            dis[1]=0;
            while(!pq.empty()){
                auto i=pq.top();
                    pq.pop();
                        int node=i.second;
                            int d=i.first;
                                if(d>dis[node])continue;
                                vis[node]=1;
                                    for(auto it:mp[node]){
                                            int adj=it.first,adjd=it.second;
                                                    if(!vis[adj] && dis[adj]>adjd+d){
                                                                dis[adj]=adjd+d;
                                                                            pq.push({adjd+d,adj});
                                                                                    }
                                                                                        }
                                                                                        }
                                                                                        for(int i=1;i<=n;i++){
                                                                                            cout<<dis[i]<<" ";
                                                                                            }
                                                                                            }

                                                                                            signed main() {
                                                                                                int n, m;
                                                                                                    std::cin >> n >> m;
                                                                                                        std::vector<std::vector<int>> connections(m, std::vector<int>(3));
                                                                                                            for (int i = 0; i < m; ++i) {
                                                                                                                    std::cin >> connections[i][0] >> connections[i][1] >> connections[i][2];
                                                                                                                        }
                                                                                                                            find_shortest_distances(n, m, connections);
                                                                                                                                return 0;
                                                                                                                                }