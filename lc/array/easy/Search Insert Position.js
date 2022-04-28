// https://leetcode.com/problems/search-insert-position/
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */

//ဒီ Approach က Bruteforce လုပ်ထားတာပါ အကယ်လို့ပိုပြီး မြန်ချင်ရင် binarySearch ကို သုံးပြီးလဲရှာလို့ရပါတယ် မေးခွန်းမှာ Sorted Array လို့ပြောထားတဲ့ အတွက်ပါ။

var searchInsert = function(nums, target) {

 function Comparator(arr,target,accum){
     if (arr[accum] < target ){
         return Comparator(arr,target,accum+1)
     }else{
        return accum
     }
     
 }

    
 if(nums.length === 0){
     return 0
 }else{
     return Comparator(nums,target,0)
 }   
    
};
