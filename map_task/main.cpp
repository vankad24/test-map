#include <iostream>
#include <chrono>
#include <map>
#include <cmath>

using namespace std;

#define println(x) std::cout << x << std::endl;
#define print(x) std::cout << x << " ";

long long getMillis() {
	return std::chrono::duration_cast<std::chrono::milliseconds>(
			std::chrono::system_clock::now().time_since_epoch()).count();
}

int main() {
	int n;
	map<int,int> m;
	for (int i=0; i <= 7; i++){
        m.clear();
        n = std::ceil(std::pow(10, i));
		auto start = getMillis();
        for (int j=0; j < n; j++) {
            m[j]=24;
        }
		print(i);
		print(getMillis()-start);
    }
	return 0;
}
