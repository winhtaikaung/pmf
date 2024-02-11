// Problem: https://leetcode.com/problems/two-sum

const assert = require('assert');

// Solution function
function twoSum(nums, target) {
  // TODO: Implement solution
}

// Test cases
describe('Two Sum', () => {
  it('Test Case 1', () => {
    const nums = [2, 7, 11, 15];
    const target = 9;
    const expected = [0, 1];
    const result = twoSum(nums, target);
    assert.deepStrictEqual(result, expected);
  });

  it('Test Case 2', () => {
    const nums = [3, 2, 4];
    const target = 6;
    const expected = [1, 2];
    const result = twoSum(nums, target);
    assert.deepStrictEqual(result, expected);
  });

  it('Test Case 3', () => {
    const nums = [3, 3];
    const target = 6;
    const expected = [0, 1];
    const result = twoSum(nums, target);
    assert.deepStrictEqual(result, expected);
  });
});