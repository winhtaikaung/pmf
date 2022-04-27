// https://leetcode.com/problems/remove-duplicates-from-sorted-array/

// Wrong Implementation that cause stack overflow  -> 
// The result is correct however it cannot handle large inputs and using extra space to keep track of items 

/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    var bucket = []
    var lastLocation = 0
    function remover(arr){
        if(arr.length !== 0){
          if (arr[0]!== undefined && !bucket.includes(arr[0])){
             bucket.push(arr[0])
             nums[lastLocation] = arr[0]
             lastLocation=lastLocation+1
          }

           return remover(arr.slice(1)) 
        }else{
         return bucket
        } 
        
    }
    
    if (nums.length === 0 ){
        return []
    }else{
       
       return remover(nums).length
        
    }
};

// Correct Approach inplace modification of nums array with O(1) complexity 
// Complexity O(1)
/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    
    
    function remover(arr,index){
        if(index === arr.length-1){
          return arr.length
        }{
          if (arr[index]!== arr[index+1]){
             remover(arr,index+1)
          }else{
            arr.splice(index+1,1)
            remover(arr,index)
          }
        }
           
        
        
    }
    
    if (nums.length === 0 ){
        return 0
    }
       
    remover(nums,0)
        
    
};


