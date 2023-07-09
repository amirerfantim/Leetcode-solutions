import java.util.Arrays;

class Solution189J {
    public void rotate(int[] nums, int k) {
        int length = nums.length;
        int[] result = new int[length];
        for (int i = 0; i < length; i++){
            result[(i + k) % length] = nums[i];
        }
        System.out.println(Arrays.toString(result));
        System.arraycopy(result, 0, nums, 0, length);
    }
}