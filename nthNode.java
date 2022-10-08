public class nthNode {
    public static void main(String[] args) {
        ListNode a = new ListNode(1);
        ListNode b = new ListNode(2);
        ListNode c = new ListNode(3);
        ListNode d = new ListNode(4);
        ListNode e = new ListNode(5);
        a.next = b;
        b.next = c;
        c.next = d;
        d.next = e;
        ListNode result = removeNthFromEnd(a, 2);
        System.out.println("Test");
    }
    
    public static ListNode removeNthFromEnd(ListNode head, int n) {
        if(head.next == null){
            return null;
        }
        int i = 1;
        ListNode ptr = head;
        ListNode tmp = head;
        while(ptr.next != null) {
            i++;
            ptr = ptr.next;
        }
        if(i == n) {
            return head.next;
        }
        ptr = head;
        while(i != (n + 1)) {
            ptr = ptr.next;
            i--;
        }
        tmp = ptr;
        ptr = ptr.next;
        tmp.next = ptr.next;
        return head;
    }
}
