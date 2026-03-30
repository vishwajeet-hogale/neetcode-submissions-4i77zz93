class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // 1) count frequencies
        unordered_map<int,int> freq;
        for (int x : nums) {
            freq[x]++;
        }

        // 2) min-heap (size k) of (frequency, value)
        //    keep the top-k most frequent items
        priority_queue<
            pair<int,int>,
            vector<pair<int,int>>,
            greater<pair<int,int>>
        > pq;

        for (auto &p : freq) {
            int val = p.first;
            int f   = p.second;
            pq.push({f, val});
            if (pq.size() > k) {
                pq.pop();
            }
        }

        // 3) extract results
        vector<int> res;
        // res.reserve(k);
        while (!pq.empty()) {
            res.push_back(pq.top().second);
            pq.pop();
        }
        return res;
    }
};