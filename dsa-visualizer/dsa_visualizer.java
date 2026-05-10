/**
 * Algorithm Logic Playground
 * Author: Issam Soubra
 * 
 * This file contains the core logic for the sorting and searching algorithms.
 * I've implemented these to serve as the backend for the visualizer.
 */

import java.util.Arrays;

public class DSAVisualizer {

    /**
     * A classic Bubble Sort. It's not the fastest, but it's great for 
     * visualizing how elements "bubble up" to their correct positions.
     */
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        boolean swapped;
        for (int i = 0; i < n - 1; i++) {
            swapped = false;
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // Swap the elements
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                    System.out.println("Swapping " + arr[j+1] + " and " + arr[j] + ": " + Arrays.toString(arr));
                }
            }
            // If no two elements were swapped by inner loop, then break
            if (!swapped) break;
        }
    }

    /**
     * Binary Search: A much faster way to find an item in a sorted list.
     * It keeps splitting the search area in half until it finds the target.
     */
    public static int binarySearch(int[] arr, int target) {
        int low = 0;
        int high = arr.length - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (arr[mid] == target) {
                return mid;
            }

            if (arr[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return -1; // Target not found
    }

    public static void main(String[] args) {
        int[] myData = {64, 34, 25, 12, 22, 11, 90};
        
        System.out.println("Starting with: " + Arrays.toString(myData));
        bubbleSort(myData);
        System.out.println("Sorted result: " + Arrays.toString(myData));

        int targetValue = 22;
        int foundIndex = binarySearch(myData, targetValue);
        
        if (foundIndex != -1) {
            System.out.println("Found " + targetValue + " at index " + foundIndex + ".");
        } else {
            System.out.println("Could not find " + targetValue + " in the list.");
        }
    }
}
