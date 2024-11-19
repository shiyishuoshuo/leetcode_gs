class Solution {
    public int largestRectangleArea(int[] heights) {
        int n = heights.length, max = 0;

        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i <= n; i++){
            while (!stack.isEmpty() && (i ==n || heights[i] < heights[stack.peek()])){
                int height = heights[stack.pop()];
                int width = stack.isEmpty() ? i : i - 1 - stack.peek();
                max = Math.max(max, width * height);
            }
            stack.push(i);
        }

        return max;
    }
}