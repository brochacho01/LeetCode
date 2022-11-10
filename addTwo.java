

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

        // ListNode l1 = new ListNode(0, null);
        // ListNode l2 = new ListNode(0, null);

        // ListNode l1 = new ListNode(9, null);
        // ListNode l12 = new ListNode(9, null);
        // ListNode l13 = new ListNode(1, null);
        // l1.next = l12;
        // l12.next = l13;
        // ListNode l2 = new ListNode(1, null);

        ListNode l1 = new ListNode(3, null);
        ListNode l12 = new ListNode(7, null);
        ListNode l2 = new ListNode(9);
        ListNode l22 = new ListNode(2);
        l1.next = l12;
        l2.next = l22;
        ListNode result = addTwoNumbers(l1, l2);
        System.out.print("");
    }

    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result = new ListNode(0, null);
        ListNode trail = new ListNode(0, null);
        int resultint;
        int carry = 0;
        // Need to assign value to result as it is guaranteed to exist
        if ((l1.val + l2.val) > 9) {
            resultint = l1.val + l2.val - 10;
            carry = 1;
        } else {
            resultint = l1.val + l2.val;
        }
        result.val = resultint;
        l1 = l1.next;
        l2 = l2.next;
        // Iterate over the lists when they have same degree of values
        if ((l1 != null) || (l2 != null) || (carry == 1)) {
            // If we have more than one node, attach result to trail
            result.next = trail;
        }
        // Loop over the parallel linked lists
        while ((l1 != null) && (l2 != null)) {
            if ((l1.val + l2.val + carry) > 9) {
                resultint = (l1.val + l2.val + carry) - 10;
                carry = 1;
            } else {
                resultint = l1.val + l2.val + carry;
                carry = 0;
            }
            trail.val = resultint;
            if ((l1.next != null) || (l2.next != null) || (carry == 1)) {
                ListNode trail2 = new ListNode(0, null);
                trail.next = trail2;
                trail = trail.next;
            }
            l1 = l1.next;
            l2 = l2.next;
        }
        if (l1 != null) {
            while (l1 != null) {
                if (l1.val + carry > 9) {
                    resultint = l1.val + carry - 10;
                    carry = 1;
                } else {
                    resultint = l1.val + carry;
                    carry = 0;
                }
                trail.val = resultint;
                if ((l1.next != null) || (carry == 1)) {
                    ListNode trail2 = new ListNode(0, null);
                    trail.next = trail2;
                    trail = trail.next;
                }
                l1 = l1.next;
            }
        }
        if (l2 != null) {
            while (l2 != null) {
                if (l2.val + carry > 9) {
                    resultint = l2.val + carry - 10;
                    carry = 1;
                } else {
                    resultint = l2.val + carry;
                    carry = 0;
                }
                trail.val = resultint;
                if ((l2.next != null) || (carry == 1)) {
                    ListNode trail2 = new ListNode(0, null);
                    trail.next = trail2;
                    trail = trail.next;
                }
                l2 = l2.next;
            }
        }
        if (carry == 1) {
            trail.val = 1;
        }
        return result;
    }
}
