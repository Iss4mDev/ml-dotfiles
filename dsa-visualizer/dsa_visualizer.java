/* 
 * ---------------------------------------------------------
 * Sorting & Searching Logic
 * Author: Issam Soubra
 * ---------------------------------------------------------
 * Just some core algorithms I wrote in Java. I use these 
 * as the "brain" for my visualizer projects.
 * ---------------------------------------------------------
 */

import java.util.Arrays;

public class DSAVisualizer {

    // A simple bubble sort. It's slow but really easy to understand.
    public static void myBubbleSort(int[] stuff) {
        int n = stuff.length;
        for (int i = 0; i < n - 1; i++) {
            boolean didSwap = false;
            for (int j = 0; j < n - i - 1; j++) {
                if (stuff[j] > stuff[j + 1]) {
                    // Swap them around
                    int temp = stuff[j];
                    stuff[j] = stuff[j + 1];
                    stuff[j + 1] = temp;
                    didSwap = true;
                    
                    // Print it out so we can see what's happening
                    System.out.println("Swapping: " + Arrays.toString(stuff));
                }
            }
            // If we didn't swap anything, it's already sorted!
            if (!didSwap) break;
        }
    }

    // Binary search is way faster than looking through everything one by one.
    public static int findMe(int[] sortedStuff, int target) {
        int low = 0;
        int high = sortedStuff.length - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (sortedStuff[mid] == target) {
                return mid; // Found it!
            }

            if (sortedStuff[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return -1; // Not in the list
    }

    public static void main(String[] args) {
        int[] myNumbers = {64, 34, 25, 12, 22, 11, 90};
        
        System.out.println("Starting with: " + Arrays.toString(myNumbers));
        myBubbleSort(myNumbers);
        System.out.println("All sorted: " + Arrays.toString(myNumbers));

        int lookFor = 22;
        int pos = findMe(myNumbers, lookFor);
        
        if (pos != -1) {
            System.out.println("Nice! Found " + lookFor + " at index " + pos);
        } else {
            System.out.println("Bummer, " + lookFor + " isn't in there.");
        }
    }
}
