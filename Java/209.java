

class Soultion209 {
    public static int minSubArrayLen(int target, int[] nums) {
        int back_pointer = 0;
        int sum = 0;
        int result = nums.length;
        boolean flag = false;
        for (int front_pointer = 0; front_pointer < nums.length; front_pointer++) {
            sum += nums[front_pointer];
            if (sum >= target) {
                flag = true;
                result = Math.min(result, front_pointer - back_pointer);
                sum -= nums[back_pointer++];
            }
        }
        if (flag) {
            return result;
        }
        return 0;
    }
}