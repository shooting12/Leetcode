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

    /* Brute-force: O(n)+S(c) */
    bool hasCycle_1st(ListNode *head)
    {
        printf("%s\n", __func__);

        map<std::intptr_t, bool> myMap;

        while (head != nullptr)
        {
            std::intptr_t addr = reinterpret_cast<std::intptr_t>(head);
            if (myMap.find(addr) != myMap.end())
            {
                return true;
            }
            else
            {
                myMap[addr] = true;
            }

            head = head->next;
        }

        return false;
    }

    bool hasCycle(ListNode *head)
    {
        bool ret = hasCycle_1st(head);

        return ret;
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
    ListNode *n3 = n5;
    n3->next = n4;
    ListNode *n2 = new ListNode(2, n3);
    ListNode *n1 = new ListNode(1, n2);
    int rows = sizeof(numArray) / sizeof(numArray[0]);
    int cols = sizeof(numArray[0]) / sizeof(int);

    //Utility::printNode(n1);
    //Utility::printNodeAddr(n1);

    // Run solution
    Solution sol;
    bool ret = sol.hasCycle(n3);
    printf("This linked list has cycle: %d.\n", ret);

    return 0;
}