// https://open.kattis.com/problems/vote
#include <bits/stdc++.h>

using namespace std;

int main() {
  int t, n, v;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    cin >> n;
    bool noWinner = false;
    int max = 0, maxI = 0, cumSum = 0;
    for (int j = 0; j < n; ++j) {
      cin >> v;
      if (v > max) {
        max = v;
        noWinner = false;
        maxI = j + 1;
      }
      else if (v == max) noWinner = true;
      cumSum += v;
    }
    if (noWinner) {
      cout << "no winner" << endl;
    } else if (((double)max / cumSum) > 0.5) {
      cout << "majority winner " << maxI << endl;
    } else {
      cout << "minority winner " << maxI << endl;
    }
  }
}