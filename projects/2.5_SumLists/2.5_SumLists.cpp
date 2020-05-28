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

    /* Brute-force: O(n)+S(1): Only get sum instead of a list nodes of sum. */
    int addTwoNumbers_1st(ListNode *l1, ListNode *l2)
    {
        printf("%s\n", __func__);

        int v1 = 0;
        int v2 = 0;
        int base = 1;

        while (l1 != nullptr)
        {
            v1 += base * l1->val;
            base *= 10;
            l1 = l1->next;
        }

        base = 1;
        while (l2 != nullptr)
        {
            v2 += base * l2->val;
            base *= 10;
            l2 = l2->next;
        }

        int sum = v1 + v2;

        return sum;
    }

    /* Brute-force: O(A+B)+S(1) */
    ListNode *addTwoNumbers_2nd(ListNode *l1, ListNode *l2)
    {
        printf("%s\n", __func__);

        int v1 = 0;
        int v2 = 0;
        int sum = 0;
        int additional = 0;
        ListNode *retNode = nullptr;
        ListNode *currNode = nullptr;

        while ((l1 != nullptr) || (l2 != nullptr) || (additional != 0))
        {
            if (l1 != nullptr)
            {
                v1 = l1->val;
                l1 = l1->next;
            }

            if (l2 != nullptr)
            {
                v2 = l2->val;
                l2 = l2->next;
            }

            sum = v1 + v2 + additional;
            additional = sum / 10;
            v1 = v2 = 0;

            if (retNode == nullptr)
            {
                retNode = new ListNode(sum % 10);
                currNode = retNode;
            }
            else
            {
                ListNode *nextNode = new ListNode(sum % 10);
                currNode->next = nextNode;
                currNode = currNode->next;
            }
        }

        return retNode;
    }

    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        int sum = addTwoNumbers_1st(l1, l2);
        ListNode *retNode = addTwoNumbers_2nd(l1, l2);

        printf("Sum is %d.\n", sum);

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
    int numArray[][5] = {{1, 2, 3, 4, 5}, {1, 2, 3, 4, 2}, {5, 4, 3, 2, 1}, {6, 6, 6, 6, 6}};
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

        n6->val = numArray[r + 1][0];
        n7->val = numArray[r + 1][1];
        n8->val = numArray[r + 1][2];
        n9->val = numArray[r + 1][3];
        n10->val = numArray[r + 1][4];
        n6->next = n7;
        n7->next = n8;
        n8->next = n9;
        n9->next = n10;
        Utility::printNode(n6);

        ListNode *retNode = sol.addTwoNumbers(n1, n6);
        Utility::printNode(retNode);
    }

    return 0;
}