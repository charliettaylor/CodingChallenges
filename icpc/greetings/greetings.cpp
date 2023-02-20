#include <bits/stdc++.h>
using namespace std;

int main()
{
  string hey;
  cin >> hey;
  int count = (hey.length() - 2) * 2;
  hey = "h";
  for (int i = 0; i < count; i++)
  {
    hey += "e";
  }
  hey += "y";
  cout << hey;
}