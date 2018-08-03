
class SNode(object):
    def __init__(self, value, next = 0):
        self.value = value
        self.next = next

    def reverse(self, head, f, t):
        nCur = head.next
        for i in f-1:
            head = nCur
            nCur = nCur.next




if __name__ == '__main__':
    print('Started...')
    pHead = SNode(0)
    pNode1 = SNode(68)
    pNode2 = SNode(62)
    pHead.next = pNode1
    pNode1.next = pNode2

    i = 0
    while(i < 10):
        print(i)
        i+=1



