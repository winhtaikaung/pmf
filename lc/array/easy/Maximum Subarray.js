// https://leetcode.com/problems/maximum-subarray

// Ref about Kadane's Algorithm https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d

var max = (a)=>(b)=> (a<b)?b:a 
 

/**
 * This is using recursive approach of Kadane's Algorithm without Tail Call Optimization 
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {

    var sum = nums[0] 
    var maxSum = sum
    function sumMaxContiguous(arr){

        if (arr.length === 0){

            return maxSum
        }else{
            sum = max(sum+arr[0])(arr[0])
            maxSum=max(maxSum)(sum)
            return sumMaxContiguous(arr.slice(1))
        }

    }
    

    if(nums.length === 0){
        return 0
    }else if (nums.length ===1){
        return nums[0]
    }else{
        
        return sumMaxContiguous(nums.slice(1))
    }
};



/**
 * This is using imperative approach of Kadane's Algorithm to solve the problem
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray2 = function(nums) {

    let sum = nums[0] 
    let maxSum = sum
    
    for(var i=1;i<nums.length;i++){
        sum = max(sum+nums[i])(nums[i])
        maxSum=max(maxSum)(sum)
    }

    return maxSum;
}
