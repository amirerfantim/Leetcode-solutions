import java.util.Arrays;

class Solution169 {
    public static int majorityElement(int[] nums) {
        Arrays.sort(nums);
        return nums[(int) (nums.length / 2)];
    }

}