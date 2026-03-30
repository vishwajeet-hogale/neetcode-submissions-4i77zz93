class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> s;
        vector<int> res;
        int idx = 0;
        for(auto x: nums){
            if (s.find(target - x) != s.end()){
                res.push_back(s[target - x]);
                res.push_back(idx);
                return res;
            }
            s[x] = idx;
            idx++;
        }
        return res;
    }
};
