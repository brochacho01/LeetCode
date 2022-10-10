public class invertTree {
    public static void main(String[] args){
        TreeNode root = new TreeNode();
        InvertTree(root);
    }

    public static TreeNode InvertTree(TreeNode root) {
        if(root == null) {
            return root;
        }
        if(root.left != null){
            InvertTree(root.left);
        }
        if(root.right != null){
            InvertTree(root.right);
        }
        if ((root.left == null) && (root.right == null)) {
            return root;
        } else if ((root.left != null) && (root.right == null)) {
            root.right = root.left;
            root.left = null;
        } else if ((root.right != null) && (root.left == null)) {
            root.left = root.right;
            root.right = null;
        } else {
            TreeNode temp = root.left;
            root.left = root.right;
            root.right = temp;
        }
        return root;
    }
}