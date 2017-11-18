#include<stdlib.h>
#include<stdio.h>
#include<stdint.h>

typedef long double f128;

uint32_t r() {
	return 	((rand() & 0xff) <<  0) |
		((rand() & 0xff) <<  8) |
		((rand() & 0xff) << 16) |
		((rand() & 0xff) << 24);
};

uint64_t trial() {
	uint64_t i;
	uint32_t n = 0;
	for (i = 0; n != 0xffffffff; ++i) {
		n = n | r();
	}
	return i;
}

void naive() {
	uint64_t n;
	uint64_t i;
	uint64_t trials = 0;
	uint64_t ors = 0;
	double ratio = 0;
	for (i = 0; i < 10000000000; ++i) {
		n = trial();
		ors += n;
		trials += 1;
		ratio = (double) ors / trials;
		// printf("%llu, %llu, %llu, %f\n", n, ors, trials, ratio);
	}
	printf("%llu %llu\n", ors, trials);
}

f128 nck(uint32_t n, uint32_t k) {
	f128 ans = 1;
	uint32_t i;
	for (i = 1; i <= n; ++i) {
		ans *= i;
	}
	for (i = 1; i <= k; ++i) {
		ans /= i;
	}
	for (i = 1; i <= n - k; ++i) {
		ans /= i;
	}
	return ans;
}

f128 prob(uint32_t n, uint32_t k) {
	f128 ans = nck(n, k);
	ans /= 4294967296;
	return ans;
}

void square_matrix(f128 in[9][9]) {
	uint32_t r, c, i;
	f128 temp[9][9];
	for (r = 0; r < 9; ++r) {
		for (c = 0; c < 9; ++c) {
			temp[r][c] = 0;
			for (i = 0; i < 9; ++i) {
				temp[r][c] += in[r][i] * in[i][c];
			}
		}
	}
	for (r = 0; r < 9; ++r) {
		for (c = 0; c < 9; ++c) {
			in[r][c] = temp[r][c];
		}
	}
}

f128 matrix() {
	f128 m[9][9];
	uint32_t c, r, i;
	for (r = 0; r < 9; ++r) {
		for (c = 0; c < 9; ++c) {
			if (c < r) {
				m[r][c] = 0;
			}
			else {
				m[r][c] = prob(9 - r, c - r);
			}
		}
	}
	for (i = 0; i < 100; ++i) {
		square_matrix(m);
	}
	return 0;
}

int main() {
	printf("%d\n", sizeof(f64)*8);
	return 0;
}
