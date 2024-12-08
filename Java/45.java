class Soultion45 {
    public static int jump(int[] nums) {
        if (nums.length == 1){
            return 0;
        }
        int result = 0;
        int i = 0;
        while (i < nums.length) {
            int next = 1;
            int maximum = 0;
            if (nums[i] + i >= nums.length - 1){
                return ++result;
            }
            for (int j = 1; j <= nums[i]; j++){
                if (i + j < nums.length){
                    if (nums[i + j] + j > maximum){
                        maximum = nums[i + j] + j;
                        next = j;
                    }
                }
            }
            result++;
            System.out.println(nums[i] + " " + i + " " + next + " " + result + " " );
            i += next;
        }


        return result;
    }

    public static void main(String[] args) {
        int[] x = {1, 2, 1, 1, 1};
        System.out.println(jump(x));
    }
}