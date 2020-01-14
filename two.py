
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def initList(self, data):
        # 创建头节点
        self.head = ListNode(data[0])
        r = self.head
        p = self.head
        # print(r == p)
        for i in data[1::]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r

    def printlist(self, head):
        if head is None:
            return
        node = head
        while node is not None:
            print(node.val, end=' ')
            node = node.next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummyHead = ListNode(0)
    curr = dummyHead  # 指针curr指向dummyHead
    carry = 0  # carry初始化为 0负责对位相加后进位
    while l1 or l2:  # 一直循环到l1或者l2全部为空
        sum = 0  # 对位相加数值之和
        if l1:  # 如果l1不为空
            sum += l1.val  # sum 将l1对位 和 l2 相加
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next
        sum += carry  # 考虑到上次相加进位
        carry = sum // 10  # 若sum>=10 则进位由carry带入下一个循环
        curr.next = ListNode(sum % 10)  # 将取余后的数字存入当前节点
        curr = curr.next  # 指向下一个节点
    if carry > 0:  # 全部加完后如果还有进位 再创建节点
        curr.next = ListNode(1)
    return dummyHead.next


list1 = [2, 4, 3]
list2 = [5, 6, 4]
link = LinkList()
l1 = link.initList(list1)
l2 = link.initList(list2)

res = addTwoNumbers(l1, l2)
link.printlist(res)

link.printlist(l1)
