def reverseList(head):
    prev = None;
    curr = head;
    while (curr != null):
        nextTemp = curr.next
        curr.next = prev
        prev = curr
        curr = nextTemp
    return prev

def hasLoop (startNode):
		slowNode = fastNode1 = fastNode2 = startNode
		while slowNode and fastNode1 = fastNode2.next and fastNode2 = fastNode1.next:
			if slowNode == fastNode1 || slowNode == fastNode2:
				return true
			slowNode = slowNode.next
		return false

def findLoopBeginning(head):
	slow = head
	fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
		if slow == fast: # Collision
			break
	# no meeting point, therefore no loop
	if fast == null || fast.next == null:
		return None

	slow = head
	# move slow to head. keep fast at meeting collision point
	# each are k steps from the loop start. If the move at the same pace,
	# they must meet at loop start
	while slow != fast:
		slow = slow.next
		fast = fast.next

	return fast