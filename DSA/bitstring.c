#include <stdio.h>
#include <stdlib.h>

// Function to check if an element exists in array arr of given size
int exists(int arr[], int size, int val) {
    for(int i = 0; i < size; i++) {
        if(arr[i] == val) return 1;
    }
    return 0;
}

// Function to find index of a value in array arr of given size
int findIndex(int arr[], int size, int val) {
    for(int i = 0; i < size; i++) {
        if(arr[i] == val) return i;
    }
    return -1;
}

// Function to print a bit-string of given size
void printBitString(int bitStr[], int size) {
    for(int i = 0; i < size; i++) {
        printf("%d", bitStr[i]);
    }
    printf("\n");
}

// Function to print set elements from bit-string using universal set U
void printSetFromBitString(int bitStr[], int size, int U[]) {
    printf("{ ");
    int first = 1;
    for(int i = 0; i < size; i++) {
        if(bitStr[i] == 1) {
            if(!first) printf(", ");
            printf("%d", U[i]);
            first = 0;
        }
    }
    printf(" }\n");
}

int main() {
    int max;

    // 1) Initialize Universal Set
    printf("Enter size of universal set (max): ");
    scanf("%d", &max);
    if(max <= 0) {
        printf("Size must be positive.\n");
        return 1;
    }

    int U[max];
    printf("Enter elements of universal set U:\n");
    for(int i = 0; i < max; i++) {
        int val;
        while(1) {
            printf("U[%d]: ", i);
            scanf("%d", &val);
            if(exists(U, i, val)) {
                printf("Duplicate value! Please re-enter.\n");
            } else {
                U[i] = val;
                break;
            }
        }
    }

    // 2) Initialize sets A and B
    int sa, sb;
    printf("Enter size of set A (<= %d): ", max);
    scanf("%d", &sa);
    if(sa < 0 || sa > max) {
        printf("Invalid size for set A.\n");
        return 1;
    }

    int A[sa];
    printf("Enter elements of set A:\n");
    for(int i = 0; i < sa; i++) {
        int val;
        while(1) {
            printf("A[%d]: ", i);
            scanf("%d", &val);
            if(exists(A, i, val)) {
                printf("Duplicate in set A! Please re-enter.\n");
                continue;
            }
            if(!exists(U, max, val)) {
                printf("Value not in universal set! Please re-enter.\n");
                continue;
            }
            A[i] = val;
            break;
        }
    }

    printf("Enter size of set B (<= %d): ", max);
    scanf("%d", &sb);
    if(sb < 0 || sb > max) {
        printf("Invalid size for set B.\n");
        return 1;
    }

    int B[sb];
    printf("Enter elements of set B:\n");
    for(int i = 0; i < sb; i++) {
        int val;
        while(1) {
            printf("B[%d]: ", i);
            scanf("%d", &val);
            if(exists(B, i, val)) {
                printf("Duplicate in set B! Please re-enter.\n");
                continue;
            }
            if(!exists(U, max, val)) {
                printf("Value not in universal set! Please re-enter.\n");
                continue;
            }
            B[i] = val;
            break;
        }
    }

    // 3) Convert sets to bit-strings
    int BA[max];
    int BB[max];

    // Initialize bit-strings to 0
    for(int i = 0; i < max; i++) {
        BA[i] = 0;
        BB[i] = 0;
    }

    for(int i = 0; i < sa; i++) {
        int idx = findIndex(U, max, A[i]);
        if(idx != -1) BA[idx] = 1;
    }
    for(int i = 0; i < sb; i++) {
        int idx = findIndex(U, max, B[i]);
        if(idx != -1) BB[idx] = 1;
    }

    // 4) Perform set operations
    int union_set[max];
    int intersection[max];
    int diff_A_B[max];
    int diff_B_A[max];

    for(int i = 0; i < max; i++) {
        union_set[i] = BA[i] | BB[i];
        intersection[i] = BA[i] & BB[i];
        diff_A_B[i] = BA[i] & (~BB[i]);
        diff_B_A[i] = BB[i] & (~BA[i]);
    }

    // Display results
    printf("\nSet A bit-string: ");
    printBitString(BA, max);
    printf("Set B bit-string: ");
    printBitString(BB, max);

    printf("\nSet A elements: ");
    printSetFromBitString(BA, max, U);
    printf("Set B elements: ");
    printSetFromBitString(BB, max, U);

    printf("\nUnion (A ∪ B): ");
    printSetFromBitString(union_set, max, U);
    printf("Union bit-string: ");
    printBitString(union_set, max);

    printf("\nIntersection (A ∩ B): ");
    printSetFromBitString(intersection, max, U);
    printf("Intersection bit-string: ");
    printBitString(intersection, max);

    printf("\nDifference (A - B): ");
    printSetFromBitString(diff_A_B, max, U);
    printf("Difference (A - B) bit-string: ");
    printBitString(diff_A_B, max);

    printf("\nDifference (B - A): ");
    printSetFromBitString(diff_B_A, max, U);
    printf("Difference (B - A) bit-string: ");
    printBitString(diff_B_A, max);

    return 0;
}