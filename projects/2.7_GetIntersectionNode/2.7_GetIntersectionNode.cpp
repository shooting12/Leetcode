#include <stdio.h>
#include <map>

using namespace std;

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

/**
 * Solution
 */
class Solution
{
public:
    typedef bool *(*SolutionFunction)(ListNode *);

    /* Brute-force: O(A or B)+S(c) */
    ListNode *getIntersectionNode_1st(ListNode *headA, ListNode *headB)
    {
        ListNode *currA = headA;
        ListNode *currB = headB;

        int lenA = 0;
        while (currA != nullptr)
        {
            currA = currA->next;
            lenA++;
        }

        int lenB = 0;
        while (currB != nullptr)
        {
            currB = currB->next;
            lenB++;
        }

        currA = headA;
        currB = headB;

        if (lenA > lenB)
        {
            int diff = lenA - lenB;
            while (diff-- > 0)
            {
                currA = currA->next;
            }
        }
        else
        {
            int diff = lenB - lenA;
            while (diff-- > 0)
            {
                currB = currB->next;
            }
        }

        while (currA != nullptr)
        {
            if (currA == currB)
            {
                return currA;
            }

            currA = currA->next;
            currB = currB->next;
        }

        return nullptr;
    }

    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB)
    {
        ListNode *retNode = getIntersectionNode_1st(headA, headB);

        return retNode;
    }
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

int main()
{
    printf("*** Run mian flow ***\n");

    // Declare node list
    int numArray[][5] = {{1, 2, 3, 4, 5}, {1, 2, 3, 4, 2}, {1, 2, 2, 2, 3}, {1, 2, 2, 2, 2}};
    ListNode *n5 = new ListNode(5);
    ListNode *n4 = new ListNode(4, n5);
    ListNode *n3 = new ListNode(3, n4);
    ListNode *n2 = new ListNode(2, n3);
    ListNode *n1 = new ListNode(1, n2);

    ListNode *n9 = new ListNode(9, n3);
    ListNode *n8 = new ListNode(8, n9);
    ListNode *n7 = new ListNode(7, n8);
    ListNode *n6 = new ListNode(6, n7);

    ListNode *n11 = new ListNode(11, n3);
    ListNode *n10 = new ListNode(10, n11);

    int rows = sizeof(numArray) / sizeof(numArray[0]);
    int cols = sizeof(numArray[0]) / sizeof(int);

    // Run solution
    Solution sol;
    ListNode *retNode = sol.getIntersectionNode(n1, n10);
    Utility::printNode(n1);
    Utility::printNode(n10);
    Utility::printNode(retNode);

    ListNode *retNode2 = sol.getIntersectionNode(n1, n6);
    Utility::printNode(n1);
    Utility::printNode(n6);
    Utility::printNode(retNode2);

    return 0;
}