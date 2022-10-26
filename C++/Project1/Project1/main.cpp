#include <iostream>

using namespace std;
/*
int main() {
	
	long long int x = 100;      // 8 bytes
	unsigned long int y = 1000; // 4 bytes
	bool b = true;			    // 1 bytes
	char c = '0';			    // 1 bytes
	float f = 30.5;				//4 byt
	double d = 50.0;			//8 byt

	d = 15.0;

	cout << "hello" << " blabal";

	if (x == y) {
		cout << "True";
	}
	else {
		cout << "False";
	}

	for (int i = 0; i < 5; i++) {
		cout << "wow" << i;
	}
	return 0;
}*/
int main() {
	for (int i = 1; i < 100; i++)
		if (i % 15 == 0) {
			cout << "FizzBuzz\n";
		}
		else if (i % 3 == 0) {
			cout << "Fizz\n";
		}
		else if (i % 5 == 0) {
			cout << "Buzz\n";
		}

		else {
			cout << i <<"\n";
		}
}