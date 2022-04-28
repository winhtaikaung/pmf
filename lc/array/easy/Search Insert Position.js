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

// ဒီ Approach ကတော့ Binaray Search နဲ့ လုပ်ထားတာပါ အပေါ်က ထက် ၂၀ms ပိုမြန်ပါတယ်။ သူကတော့ အလယ်ကဖြတ်ဖြတ်ပြီး ရှိတဲ့ အပိုင်း ကို ရှာသွားတာမို့လို့ ပိုမြန်ပါတယ်
var searchInsertBinarySearchApproach = function(nums, target) {

 function Comparator(arr,left,right,target){
   
   const mid = Math.round((left+right)/2)

     if (arr[mid] === target){
         return mid
     }

     if (left>right){ // ဒီနေရာကတော့ ကိုယ့် target က Array ထဲမှာ ရှာမတွေ့ရင် Left Index ကိုပြန်ပေးမှာပါ
         return left
     }else if(arr[mid]>target){ // ဒီနေရာကတော့ ကိုဘ်ရှာချင်တဲ့ Target ဘယ်ဖက်မှာရှိတယ်ဆိုဘယ်ကိုတောက်လျောက် RecursiveCallပြီး ရှာမှာဖြစ်ပါတယ်
         return Comparator(arr,left,mid-1,target) 
     }

     return Comparator(arr,mid+1,right,target)// ဒီနေရာကတော့ ကိုဘ်ရှာချင်တဲ့ Target ညာဖက်မှာရှိတယ်ဆိုဘယ်ကိုတောက်လျောက်RecursiveCallပြီး ရှာမှာဖြစ်ပါတယ်
    
     
 }

    
 if(nums.length === 0){
     return 0
 }else{

     return Comparator(nums,0,nums.length-1,target)
 }   
    
};
