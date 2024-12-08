class Solution55 {
    public static boolean canJump(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0 && i != nums.length - 1) {
                int j = 0;
                boolean flag = false;
                while (i - j >= 0) {
                    if (nums[i - j] > j) {
                        flag = true;
                        break;
                    }
                    j++;
                }
                if (!flag) {
                    return false;
                }
            }
        }
        return true;
    }

}