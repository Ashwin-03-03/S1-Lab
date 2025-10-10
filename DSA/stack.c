#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 50

int stack[MAX_SIZE];
int top = -1;

int push(int data)
{
    if (top >= MAX_SIZE - 1)
    {
        printf("Overflow error");
    }
    else
    {
        top++;
        stack[top] = data;
        printf("The data is pushed to stack");
    }
}

int pop()
{
    if (top < 0)
    {
        printf("Underflow error");
    }
    else
    {
        int popped = stack[top];
        top--;
        printf("%d is popped", popped);
    }
}

int display()
{
    if (top < 0)
    {
        printf("The stack is empty");
    }
    else
    {
        for (int i = top; i >= 0; i--)
        {
            printf("%d\t", stack[i]);
        }
    }
}

int main()
{
    int choice, value;

    while (1)
    {
        printf("Enter the option to perform:\n");
        printf("1.PUSH\n2.POP\n3.DISPLAY\n4.EXIT");

        printf("Enter your choice:");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            printf("Enter the value to push");
            scanf("%d", &value);
            push(value);
            break;
        case 2:
            pop();
            break;
        case 3:
            display();
            break;
        case 4:
            return 0;

        default:
            printf("Invalid choice");
            break;
        }
    }
    return 0;
}