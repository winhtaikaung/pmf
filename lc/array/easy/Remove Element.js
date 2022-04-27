// https://leetcode.com/problems/remove-element/solution/



/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function (nums, val) {

    function remover(arr, accu) {
        if (accu > nums.length - 1) {
            return arr.length
        } else {
            if (arr[accu] === val && arr[accu + 1] === val) { // ဒီနေရာမှာ Pattern Matching Approach ကိုသုံးထားလိုက်တယ်  အကယ်လို arr က [2,2,2] နဲ့ val = 2 ဖြစ်ခဲ့ရင်
                arr.splice(accu, 2)
                return remover(arr, accu)
            }
            else if (arr[accu] === val) { // ဒါကတော့ arrရဲ့ index ကိုသုံးပြီး val ကို တိုက်စစ်လိုက်တယ် ညီ ရင်တခန်းပဲဖျက်တယ် 
                arr.splice(accu, 1)
                return remover(arr, accu)
            }
            remover(arr, accu + 1)
        }
    }

    if (nums.length === 0) {
        return 0
    } else {
        remover(nums, 0)
    }
};
