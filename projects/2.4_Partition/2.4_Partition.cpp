#include <stdio.h>
#include <map>

using namespace std;

class Utility;

/**
 * Definition for singly-linked list.
 */
class ListNode
{
public:
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Utility
{
public:
    static void printNode(ListNode *head)
    {
        ListNode *currNode = head;
        while (currNode != nullptr)
        {
            printf("%d ", currNode->val);
            currNode = currNode->next;
        }
        printf("\n");
    }

    static void printNodeAddr(ListNode *head)
    {
        ListNode *currNode = head;
        while (currNode != nullptr)
        {
            printf("%p ", currNode);
            currNode = currNode->next;
        }
        printf("\n");
    }
};

/**
 * Solution
 */
class Solution
{
public:
    typedef ListNode *(*SolutionFunction)(ListNode *);

    /* Brute-force: O(n)+S(1) */
    ListNode *getPartition_1st(ListNode *head, int partition)
    {
        printf("%s\n", __func__);

        ListNode *leftPtr = head;
        ListNode *rightPtr = head;
        ListNode *tmpNode = nullptr;

        while (leftPtr->next != nullptr)
        {
            while (leftPtr->next != nullptr && leftPtr->next->val < partition)
            {
                leftPtr = leftPtr->next;
            }

            rightPtr = leftPtr;

            while (rightPtr->next != nullptr && rightPtr->next->val >= partition)
            {
                rightPtr = rightPtr->next;
            }

            // Swap leftPtr's next node and rightPtr's next node
            tmpNode = rightPtr->next;
            rightPtr->next = leftPtr->next;
            leftPtr->next = tmpNode;
            tmpNode->next = leftPtr;

            Utility::printNode(head);
        }

        return head;
    }

    ListNode *getPartition(ListNode *head, int partition)
    {
        ListNode *retNode = getPartition_1st(head, partition);

        return retNode;
    }
};

int main()
{
    printf("*** Run mian flow ***\n");

    // Declare node list
    int numArray[][5] = {{1, 5, 3, 9, 1}, {1, 2, 3, 4, 2}, {5, 4, 3, 2, 1}, {6, 6, 6, 6, 6}};
    ListNode *n5 = new ListNode(5);
    ListNode *n4 = new ListNode(4, n5);
    ListNode *n3 = new ListNode(3, n4);
    ListNode *n2 = new ListNode(2, n3);
    ListNode *n1 = new ListNode(1, n2);

    ListNode *n10 = new ListNode(5);
    ListNode *n9 = new ListNode(4, n10);
    ListNode *n8 = new ListNode(3, n9);
    ListNode *n7 = new ListNode(2, n8);
    ListNode *n6 = new ListNode(1, n7);

    int rows = sizeof(numArray) / sizeof(numArray[0]);
    int cols = sizeof(numArray[0]) / sizeof(int);

    // Run solution
    Solution sol;
    for (int r = 0; r < rows; r += 2)
    {
        printf("Processing data group %d...\n", r);
        n1->val = numArray[r][0];
        n2->val = numArray[r][1];
        n3->val = numArray[r][2];
        n4->val = numArray[r][3];
        n5->val = numArray[r][4];
        n1->next = n2;
        n2->next = n3;
        n3->next = n4;
        n4->next = n5;
        Utility::printNode(n1);

        int partition = 5;
        ListNode *retNode = sol.getPartition(n1, partition);
        Utility::printNode(retNode);
    }

    return 0;
}