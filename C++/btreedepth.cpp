#include <iostream>
#include <stack>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    // Recursive DFS, can we do iterative?
    int maxDepth(TreeNode* root) {
        stack<TreeNode*> s;
        s.push(root);
        int depth = 1;
        int max = depth;
        TreeNode* curr;

        while(!s.empty()){
            curr = s.top();
            while(curr->left){
                s.push(curr->left);
                curr = curr->left;
                ++depth;
            }
            if(depth > max){
                max = depth;
            }
            // only pop after we finish checking a right side
            // s.pop()
            // --depth;

            if(curr->right){
                s.push(curr->right);
                ++depth;
            }
        }
        return max;
    }

};

// Recursive Solution
// class Solution {
// public:
//     int maxDepth(TreeNode* root) {
//         if(!root){
//             return 0;
//         }
//         int left = maxDepth(root->left)+1;
//         int right = maxDepth(root->right)+1;
//         return left > right ? left : right;
//     }
// };