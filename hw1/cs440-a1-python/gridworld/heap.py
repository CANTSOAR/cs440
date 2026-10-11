"""Part 2: implement a binary min-heap. YOU EDIT THIS FILE.

Store (priority, item) pairs in an array. Compare priorities, not items.
For index i, the children are 2*i + 1 and 2*i + 2, and the parent is
(i - 1) // 2. Each parent's priority must be at most its children's priorities.

Use your own heap; ready-made priority queues are not allowed. The autograder
checks correctness and the number of priority comparisons.
"""
from __future__ import annotations


class BinaryHeap:
    """A min-heap of ``(priority, item)`` pairs.

    TODO (Part 2a). Implement :meth:`push`, :meth:`pop` and :meth:`__len__`,
    keeping the pairs in ``self.data`` with the smallest priority at index 0.

    The autograder reads ``self.data`` directly and checks the invariant after
    every operation on long random sequences. It also counts comparisons and
    expects the amortised count to stay within a small multiple of ``log2 n``,
    so a re-sorted list is correct but will not fit the budget.
    """

    __slots__ = ("data",)

    def __init__(self):
        #: the heap array: a list of ``(priority, item)`` pairs
        self.data: list[tuple] = []

    def __len__(self) -> int:
        """TODO (Part 2a).  How many pairs are in the heap."""
        return len(self.data)

    def __bool__(self) -> bool:
        return len(self) > 0

    def push(self, priority, item) -> None:
        """Insert one pair.

        TODO (Part 2a). Append, then sift up: while it is smaller than its
        parent, swap the two.
        """
        data = self.data
        data.append((priority, item))
        i = len(data) - 1
        while i > 0:
            p = (i - 1) // 2
            if data[i][0] < data[p][0]:
                data[i], data[p] = data[p], data[i]
                i = p
            else:
                break

    def pop(self):
        """Remove and return the ``item`` with the smallest priority.

        TODO (Part 2a). Save ``data[0]``, move the last element into its
        place, shrink the list, then sift that element down past its smaller
        child.

        Raise ``IndexError`` on an empty heap: that is how your search notices
        the open list has run dry and reports the target unreachable.
        """
        data = self.data
        if not data:
            raise IndexError("pop from an empty heap")
        top = data[0]
        last = data.pop()
        n = len(data)
        if n:
            data[0] = last
            i = 0
            while True:
                l = 2 * i + 1
                if l >= n:
                    break
                r = l + 1
                c = r if r < n and data[r][0] < data[l][0] else l
                if data[c][0] < data[i][0]:
                    data[i], data[c] = data[c], data[i]
                    i = c
                else:
                    break
        return top[1]

    # -- optional --------------------------------------------------------
    def peek(self):
        """The smallest priority without removing it.  Provided."""
        if not self.data:
            raise IndexError("peek from an empty heap")
        return self.data[0][0]
