#include <bits/stdc++.h>
#include <regex>
#include <fstream>
#define rep(i,a,b) for(int i=a;i<=b;i++)
#define ll long long
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    regex xm(R"(XM_.*?[\n;])");
    regex xp(R"(XP_.*?[\n;])");
    smatch resm, resp;
    cout<<"running"<<endl;
    freopen("input.txt", "r", stdin);//input filename
    freopen("output.txt", "w", stdout);//output filename
    string line;
    set < pair<string, string>> st;
    while (getline(cin, line))
    {
        //cout<<"running"<<endl;
        if (regex_search(line, resm, xm) && regex_search(line, resp, xp))
        {
            st.insert({ resm[0],resp[0] });
        }
    }
    for (auto x : st)
    {
        cout << x.first << "\t" << x.second << endl;
    }
    return 0;
}

