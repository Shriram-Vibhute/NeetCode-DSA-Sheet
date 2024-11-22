class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int>mpp;
        for(int i = 0; i < nums1.size(); i++) {
            mpp[nums1[i]] = i;
        }
        vector<int>ans(nums1.size(), -1);

        stack<int>st; // For storing the elements from nums1
        for(int i = 0; i < nums2.size(); i++) {
            int curr = nums2[i];
            while(!st.empty() && curr > st.top()){
                int val = st.top();
                st.pop();
                int idx = mpp[val];
                ans[idx] = curr;
            }
            if(mpp.find(curr) != mpp.end()){
                st.push(curr);
            }
        }
        return ans;
    }
};
/*
Explanation of Monotonic Stack Pattern

The pattern you get from the Next Greater Element (Leetcode 496) problem is known as the Monotonic Stack Pattern. This pattern is useful in solving problems that involve finding relationships between elements in an array, especially when you're asked to find the "next" or "previous" element in a certain order.

Understanding the Monotonic Stack Pattern
In this problem, the task is to find for each element in an array, the next element that is greater than it. You use a stack to help efficiently track potential candidates for the "next greater element."

How it Works (Step by Step)
Monotonic Stack: A monotonic stack is a stack where the elements are ordered in a specific way. In this case, you maintain a decreasing stack (top of stack holds the largest value).
Processing each element: As you process each element, you compare it with the element at the top of the stack:
If the current element is greater than the element at the top of the stack, you've found the "next greater element" for the element at the top of the stack, so you pop it from the stack.
If the current element is smaller or equal to the stack's top, push it onto the stack because it might be the "next greater" element for future elements.
Efficiency: This ensures that each element is pushed and popped from the stack only once, leading to a time complexity of O(n).
Why Monotonic Stack Works Here:
You're processing the elements of the array in left-to-right order.
You use the stack to keep track of elements that haven't yet found their "next greater element."
When you find a larger element, it means that any smaller elements on the stack have now found their "next greater element."
Pattern to Recognize and Apply:
The Monotonic Stack pattern is helpful when you're dealing with problems where you need to:

Find the "next greater" or "previous greater" element for every element in an array.
Process elements in a way that requires comparison to the element that came before or after it (usually in a specific order).
Similar Types of Problems:
Here are some problem types where you can apply the Monotonic Stack pattern:

Next Greater Element (NGE) Problems:

Given an array, find the next greater element for each element.
Example: Leetcode 496 (Next Greater Element I), Leetcode 503 (Next Greater Element II).
Previous Greater Element:

Given an array, find the previous greater element for each element.
This is similar to NGE, but you look at the elements to the left instead of the right.
Stock Span Problem:

Given an array of stock prices, find for each day, how many consecutive days the price has been less than or equal to the current day's price.
Largest Rectangle in Histogram (Leetcode 84):

This is a classic problem where you need to find the largest rectangular area in a histogram, and you use a stack to maintain a monotonic decreasing sequence of bars.
Maximum Area of Rectangle in Binary Matrix (Leetcode 85):

This involves dynamic programming and monotonic stacks to solve.
Sliding Window Maximum (Leetcode 239):

Find the maximum value in a sliding window of size k for a given array.
When to Apply:
You should consider applying the Monotonic Stack pattern when:

You're looking to process elements in a sequence.
You need to maintain an order (either increasing or decreasing) in the stack as you process elements.
The problem requires efficiently finding the next or previous greater or smaller element.
Summary:
Pattern: Monotonic Stack (usually decreasing or increasing).
Typical Problems: Next Greater Element, Previous Greater Element, Stock Span, Largest Rectangle in Histogram, etc.
When to Use: When the problem involves finding relationships like the "next greater" element in a sequence, and you can process each element in one pass with the help of a stack.
Using a monotonic stack allows you to solve these problems in linear time (O(n)), making it much more efficient than a brute-force solution.
*/