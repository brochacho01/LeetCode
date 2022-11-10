class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def addTwoNumbers(self, l1, l2):
    carry = int(0)
    result = ListNode(self)
    resultIterator = ListNode(self)
    resultIterator = result
    while (l1.next != None) and (l2.next != None):
        resultIterator.val = l1.val + l2.val + carry
        if carry == 1:
            carry = 0
        if resultIterator.val >= 10:
            carry = 1
            resultIterator.val -= 10
        resNext = ListNode(self)
        resultIterator.next = resNext
        resultIterator = resultIterator.next
        l1 = l1.next
        l2 = l2.next
    # Both the lists still have a val, just no next
    resultIterator.val = l1.val + l2.val + carry
    if carry == 1:
        carry = 0
    if resultIterator.val >= 10:
        carry = 1
        resultIterator.val -= 10
    if (l1.next != None) or (l2.next != None):
        resNext = ListNode(self)
        resultIterator.next = resNext
        resultIterator = resultIterator.next
    elif carry == 1:
        resNext = ListNode(self)
        resNext.val = carry
        resultIterator.next = resNext
    # we've caught the last nodes that are adjacent
    if l1.next != None:
        l1 = l1.next
        while l1.next != None:
            resultIterator.val = l1.val + carry
            if carry == 1:
                carry = 0
            if resultIterator.val >= 10:
                carry = 1
                resultIterator.val -= 10
            resNext = ListNode(self)
            resultIterator.next = resNext
            resultIterator = resultIterator.next
            l1 = l1.next
        # catch last val
        resultIterator.val = l1.val + carry
        if resultIterator.val >= 10:
            resNext = ListNode(self)
            resultIterator.val -= 10
            resNext.val = 1
            resultIterator.next = resNext
    if l2.next != None:
        l2 = l2.next
        while l2.next != None:
            resultIterator.val = l2.val + carry
            if carry == 1:
                carry = 0
            if resultIterator.val >= 10:
                carry = 1
                resultIterator.val -= 10
            resNext = ListNode(self)
            resultIterator.next = resNext
            resultIterator = resultIterator.next
            l2 = l2.next
        resultIterator.val = l2.val + carry
        if resultIterator.val >= 10:
            resNext = ListNode(self)
            resultIterator.val -= 10
            resNext.val = 1
            resultIterator.next = resNext
    return result

def main():
    # l1 = ListNode(2)
    # l12 = ListNode(4)
    # l1.next = l12
    # l13 = ListNode(3)
    # l12.next = l13
    # l2 = ListNode(5)
    # l22 = ListNode(6)
    # l2.next = l22
    # l23 = ListNode(4)
    # l22.next = l23
    l1 = ListNode(9)
    l2 = ListNode(9)
    l22 = ListNode(9)
    l2.next = l22
    l23 = ListNode(9)
    l22.next = l23
    addTwoNumbers(None, l1, l2)

if __name__ == "__main__":
    main()
