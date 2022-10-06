public class addTwo {
    // https://leetcode.com/problems/add-two-numbers/
    public static void main(String[] args) {
        // ListNode l1 = new ListNode(2);
        // ListNode l12 = new ListNode(4);
        // ListNode l13 = new ListNode(3);
        // l1.next = l12;
        // l12.next = l13;
        // ListNode l2 = new ListNode(5);
        // ListNode l22 = new ListNode(6);
        // ListNode l23 = new ListNode(4);
        // l2.next = l22;
        // l22.next = l23;

        ListNode l1 = new ListNode(0, null);
        ListNode l2 = new ListNode(0, null);
        ListNode result = addTwoNumbers(l1, l2);
        System.out.print("");
    }

    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result = new ListNode(0, null);
        ListNode trail = new ListNode(0, null);
        int resultint;
        int carry;
        if (l1.val + l2.val > 9) {
            resultint = (l1.val + l2.val) - 10;
            carry = 1;
        } else {
            resultint = l1.val + l2.val;
            carry = 0;
        }
        result.val = resultint;
        // Iterate over the lists when they have same degree of values
        if ((l1.next != null) && (l2.next != null)) {
            result.next = trail;
            while ((l1.next != null) && (l2.next != null)) {
                l1 = l1.next;
                l2 = l2.next;
                if (l1.val + l2.val + carry > 9) {
                    resultint = (l1.val + l2.val + carry) - 10;
                    carry = 1;
                } else {
                    resultint = l1.val + l2.val + carry;
                    carry = 0;
                }
                trail.val = resultint;
                if ((l1.next != null) && (l2.next != null)) {
                    ListNode trail2 = new ListNode(0, null);
                    trail.next = trail2;
                    trail = trail.next;
                }
            }
        }
        if (l1.next != null) {
            while (l1.next != null) {
                l1 = l1.next;
                if(l1.val + carry > 9){
                    trail.val = 0;
                    carry = 1;
                } else {
                    trail.val = resultint + carry;
                    carry = 0;
                }
                if (l1.next != null) {
                    ListNode trail2 = new ListNode(0, null);
                    trail.next = trail2;
                    trail = trail.next;
                }
            }
        }
        if (l2.next != null) {
            while (l2.next != null) {
                l2 = l2.next;
                if(l2.val + carry > 9){
                    trail.val = 0;
                    carry = 1;
                } else {
                    trail.val = resultint + carry;
                    carry = 0;
                }
                if (l2.next != null) {
                    ListNode trail2 = new ListNode(0, null);
                    trail.next = trail2;
                    trail = trail.next;
                }
            }
        }
        return result;
    }
}
