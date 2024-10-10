#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector<vector<int>> mergeIntervals(vector<vector<int>>& intervals) {
    vector<vector<int>> merged;
    if (intervals.empty()) {
        return merged;
    }
    // 按照区间的起点进行排序
    sort(intervals.begin(), intervals.end());
    // 将第一个区间加入结果集
    merged.push_back(intervals[0]);
    for (int i = 1; i < intervals.size(); i++) {
        // 如果当前区间的起点小于等于上一个合并区间的终点，说明有重叠，合并区间
        if (intervals[i][0] <= merged.back()[1]) {
            merged.back()[1] = max(merged.back()[1], intervals[i][1]);
        } else {
            // 如果没有重叠，则直接加入当前区间
            merged.push_back(intervals[i]);
        }
    }
    return merged;
}
int main() {
    vector<vector<int>> intervals = {{10, 30}, {20, 60}, {80, 100}, {150, 180}};
    vector<vector<int>> result = mergeIntervals(intervals);
    // 输出合并后的区间
    for (const auto& interval : result) {
        cout << "[" << interval[0] << ", " << interval[1] << "] ";
    }
    cout << endl;
    return 0;
}
