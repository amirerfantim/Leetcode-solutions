
class Solution1 {
    public static int removeElement(int[] nums, int val) {
        int k = 0;

        for (int loop = 0; loop < nums.length; loop++){
            if (nums[loop] == val){
                k += 1;
            }
            if (nums[loop] != val){
                nums[loop - k] = nums[loop];
            }
        }
        return nums.length - k;
    }
}