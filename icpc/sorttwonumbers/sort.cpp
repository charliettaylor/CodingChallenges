#include <bits/stdc++.h>
using namespace std;

int main()
{
  int a, b;
  cin >> a >> b;
  vector<int> list = { a, b };

  sort(list.begin(), list.end());
  cout << list[0] << " " << list[1];
}
