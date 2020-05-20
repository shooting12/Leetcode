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

    // O(n) and S(c)
    ListNode *deleteDuplicates_1st(ListNode *head)
    {
        // Todo: Not using lastNode (reduce one extra ListNode pointer)
        printf("%s\n", __func__);

        map<int, bool> myMap;
        ListNode *currNode = head;
        ListNode *lastNode = head;
        while (currNode != nullptr)
        {
            if (myMap.find(currNode->val) != myMap.end())
            {
                lastNode->next = currNode->next;
            }
            else
            {
                lastNode = currNode;
                myMap[currNode->val] = true;
            }

            currNode = currNode->next;
        }

        return head;
    }

    // O(n^2) and S(1)
    ListNode *deleteDuplicates_2nd(ListNode *head)
    {
        printf("%s\n", __func__);

        map<int, bool> myMap;
        ListNode *index1 = head;
        ListNode *index2 = head;
        ListNode *lastNode = head;

        while (index1 != nullptr)
        {
            index2 = index1->next;
            lastNode = index1;
            while (index2 != nullptr)
            {
                if (index1->val == index2->val)
                {
                    lastNode->next = index2->next;
                    lastNode = lastNode->next;
                }
                lastNode = index2;
                index2 = index2->next;
            }
            index1 = index1->next;
        }

        return head;
    }

    ListNode *deleteDuplicates(ListNode *head)
    {
        //static Solution::SolutionFunction funcs[] = {deleteDuplicates_1st, deleteDuplicates_2nd};

        //ListNode *retNode = deleteDuplicates_1st(head);
        ListNode *retNode2 = deleteDuplicates_2nd(head);

        return head;
    }
};

/**
 * Function pointer example - Simple
 */
typedef void (*MYFUNC)();
void func1()
{
    printf("%s\n", __func__);
}

void func2()
{
    printf("%s\n", __func__);
}

/**
 * Function pointer example - Mine
 */
typedef ListNode *(*SolutionFunctionOut)(ListNode *);

ListNode *deleteDuplicates_1(ListNode *head)
{
    printf("%s\n", __func__);
    return head;
}

ListNode *deleteDuplicates_2(ListNode *head)
{
    printf("%s\n", __func__);
    return head;
}

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
};

int main()
{
    // Function pointer example - Simple
    printf("Run functoin pointer example - simple.\n");
    static MYFUNC funcs[] = {&func1, &func2};
    int functionSize = sizeof(funcs) / sizeof(MYFUNC);
    for (int i = 0; i < functionSize; i++)
    {
        funcs[i]();
    }

    // Function pointer example - Mine
    printf("Run functoin pointer example - mine.\n");
    static SolutionFunctionOut solFuncs[] = {deleteDuplicates_1, deleteDuplicates_2};
    int solFunctionSize = sizeof(solFuncs) / sizeof(MYFUNC);
    ListNode *node = new ListNode(1);
    for (int i = 0; i < solFunctionSize; i++)
    {
        solFuncs[i](node);
    }

    printf("*** Run mian flow ***\n");

    // Declare node list
    int numArray[][5] = {{1, 2, 3, 2, 5}, {1, 2, 3, 4, 2}, {1, 2, 2, 2, 3}, {1, 2, 2, 2, 2}};
    ListNode *n5 = new ListNode(5);
    ListNode *n4 = new ListNode(4, n5);
    ListNode *n3 = new ListNode(3, n4);
    ListNode *n2 = new ListNode(2, n3);
    ListNode *n1 = new ListNode(1, n2);
    int rows = sizeof(numArray) / sizeof(numArray[0]);
    int cols = sizeof(numArray[0]) / sizeof(int);

    /*
    ListNode **myNodes = new ListNode *[rows];
    for (int r = 0; r < rows; r++)
    {
        for (int c = 0; c < cols - 1; c++)
        {
            myNodes[c]->val = numArray[r][c];
            myNodes[c]->next = myNodes[c + 1];
        }
        myNodes[cols - 1]->val = numArray[r][cols - 1];
        Utility::printNode(myNodes[0]);
    }
    */

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

        ListNode *retNode = sol.deleteDuplicates(n1);
        Utility::printNode(retNode);
    }

    return 0;
}