/**
 * Data Structures & Algorithms Visualizer (Core Logic)
 * Author: Issam Soubra
 * Description: A Java-based implementation of core data structures and algorithms, 
 * designed to be integrated with a web-based visualization interface.
 */

import java.util.Arrays;

public class DSAVisualizer {

    /**
     * Bubble Sort implementation with step-by-step logging for visualization.
     */
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // Swap elements
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    System.out.println("Swapped: " + Arrays.toString(arr));
                }
            }
        }
    }

    /**
     * Binary Search implementation.
     */
    public static int binarySearch(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == target) {
                return mid;
            }
            if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] data = {64, 34, 25, 12, 22, 11, 90};
        System.out.println("Original array: " + Arrays.toString(data));
        bubbleSort(data);
        System.out.println("Sorted array: " + Arrays.toString(data));

        int target = 22;
        int result = binarySearch(data, target);
        if (result != -1) {
            System.out.println("Element " + target + " found at index " + result);
        } else {
            System.out.println("Element " + target + " not found");
        }
    }
}
