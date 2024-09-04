#include <iostream>
#include <cmath>
#include <vector>
#include <string>
using namespace std;

// 소수인지 판별하는 함수
bool isPrime(int num) {
    // 1은 소수가 아님
    if (num <= 1) return false;

    // 2와 3은 소수임
    if (num == 2 || num == 3) return true;

    // 짝수는 소수가 아님
    if (num % 2 == 0) return false;

    // 소수 여부 판단을 위해 √num까지만 나눠서 확인
    for (int i = 3; i <= sqrt(num); i += 2) {
        if (num % i == 0) {
            return false;
        }
    }

    return true;
}

int main() {
    int num;
    cin >> num;

    // 메모이제이션을 위한 벡터 배열
    vector<vector<int>> memoObject(num + 1);

    // 1자리 수 소수 초기화
    memoObject[1] = {2, 3, 5, 7};

    // 2자리 수부터 num자리 수까지 소수를 구하는 로직
    for (int i = 2; i <= num; i++) {
        for (const int& beforeNum : memoObject[i - 1]) {
            for (int j = 0; j <= 9; j++) {
                int newNumber = stoi(to_string(beforeNum) + to_string(j));
                if (isPrime(newNumber)) {
                    memoObject[i].push_back(newNumber);
                }
            }
        }
    }

    // 결과 출력
    for (const int& printNumber : memoObject[num]) {
        cout << printNumber << endl;
    }

    return 0;
}
