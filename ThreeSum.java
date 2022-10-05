package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

// https://leetcode.com/problems/3sum/solutions/
public class ThreeSum {
    public static void main(String[] args) {
        int[] nums = { 0,0,0,0};
        System.out.println(threeSum(nums).size());

    }

    public static List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 2; i++) {
            // Check to see if current i is the same as previous, if so duplicate triple,
            // continue
            if (i > 0) {
                if (nums[i] == nums[i - 1]) {
                    continue;
                }
            }
            int low = i + 1;
            int high = nums.length - 1;
            int lasthigh = Integer.MAX_VALUE;
            int lastlow = Integer.MIN_VALUE;
            while (low < high) {
                if (nums[i] + nums[low] + nums[high] == 0) {
                    if ((i != low) && (i != high) && (low != high)) {
                        List triple = new ArrayList<Integer>();
                        triple.add(nums[i]);
                        triple.add(nums[low]);
                        triple.add(nums[high]);
                        if ((nums[low] != lastlow) && (nums[high] != lasthigh)) {
                            result.add(triple);
                            lastlow = nums[low];
                            lasthigh = nums[high];
                        }
                        high--;
                    }
                } else if (nums[i] + nums[low] + nums[high] < 0) {
                    low++;
                } else if (nums[i] + nums[low] + nums[high] > 0) {
                    high--;
                }
            }
        }
        return result;
    }
}
