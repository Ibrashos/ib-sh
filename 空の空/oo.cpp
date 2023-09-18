#include <iostream>
#include <vector>

using namespace std;
vector<int> nums = { 3,2,3 };
int target;
vector<int> twoSum(vector<int>& nums, int target);


int main() {
	target = 6;
	twoSum(nums, target);
}

vector<int> twoSum(vector<int>& nums, int target) {
	int j = nums.size();
	vector<int> res;
	vector<int> non = {};
	for (int n = 0; n < j; n++) {
		for (int k = n+1; k < j; k++) {
			res.push_back(n);
			res.push_back(k);
			return nums[n] + nums[k] == target ? res : non;
		}
	}
	return {};
}
