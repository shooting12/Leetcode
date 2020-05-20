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
    typedef ListNode *(*SolutionFunction)(ListNode *);

    /* Brute-force: O(n)+S(1) */
    ListNode *returnKthToLast_1st(ListNode *head, int k)
    {
        printf("%s\n", __func__);

        int counter = 0;
        ListNode *currNode = head;
        while (currNode != nullptr)
        {
            currNode = currNode->next;
            counter++;
        }

        int index = counter - k;
        if (index < 0)
        {
            printf("Kth is out of length (%d > %d), return Head.\n", k, counter);
            return head;
        }

        currNode = head;
        while (currNode != nullptr && (index--) > 0)
        {
            currNode = currNode->next;
        }

        return currNode;
    }

    /* Refer to Textbook: O(n)+S(1) */
    ListNode *returnKthToLast_2nd(ListNode *head, int k)
    {
        printf("%s\n", __func__);

        // Left leftNodePtr and rightNodePtr have k distance
        ListNode *rightNode = head;
        for (int i = 0; i < k; i++)
        {
            rightNode = rightNode->next;
        }

        // Move both pointer at the same time until rightNodePtr reach the end.
        // Then leftNodePtr would have k distance to the end.
        ListNode *leftNode = head;
        while (rightNode != nullptr)
        {
            rightNode = rightNode->next;
            leftNode = leftNode->next;
        }

        return leftNode;
    }

    ListNode *returnKthToLast(ListNode *head, int k)
    {
        //ListNode *retNode = returnKthToLast_1st(head, k);
        ListNode *retNode = returnKthToLast_2nd(head, k);

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
    int rows = sizeof(numArray) / sizeof(numArray[0]);
    int cols = sizeof(numArray[0]) / sizeof(int);

    // Run solution
    Solution sol;
    for (int r = 0; r < rows; r++)
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
        //Utility::printNodeAddr(n1);

        int k = 3;
        ListNode *retNode = sol.returnKthToLast(n1, k);
        printf("Kth(%d) node from end is %p and value is %d.\n", k, retNode, retNode->val);
    }

    return 0;
}