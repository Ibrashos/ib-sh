#include <iostream>
#include <vector>

using namespace std;
vector<int> nums = { 3,3,3,3,3 };
int target;
vector<int> twoSum(vector<int>& nums, int target);


int main() {
	target = 1;
	for (int num : twoSum(nums, target)) {
		cout << num;
	}


}

vector<int> twoSum(vector<int>& nums, int target) {
	vector<int> res = {5,6,6};
	int n = 0;
	nums.resize(nums.size() + 1);
	while(n!=nums.size()) {
		if (nums[n] == NULL) break;
		if (nums[n] + nums[n + 1] == target) {
			return res;
		}
		n++;
	}


}

