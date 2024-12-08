import java.util.Arrays;

class Solution121 {
    public int maxProfit(int[] prices) {
        int max_profit = 0;
        int[] maxes  = new int[prices.length + 1];
        maxes[prices.length] = 0;
        for (int i = prices.length -1; i > 0; i--){
            maxes[i] = Math.max(prices[i], maxes[i + 1]);
        }
        for (int i = 0; i < prices.length; i++){
            if (maxes[i] - prices[i] > max_profit){
                max_profit = maxes[i] - prices[i];
            }
        }
        return max_profit;
    }
}