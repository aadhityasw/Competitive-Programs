// Initial Template for Java

import java.util.*;
import java.io.*;

class GfG {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int a = sc.nextInt();
            MinHeap h = new MinHeap(a);
            for (int i = 0; i < a; i++) {
                int c = sc.nextInt();
                int n;
                if (c == 1) {
                    n = sc.nextInt();

                    h.insertKey(n);
                }
                if (c == 2) {
                    n = sc.nextInt();
                    h.deleteKey(n);
                }
                if (c == 3) {
                    System.out.print(h.extractMin() + " ");
                }
            }
            System.out.println();
        }
    }
}


// User function Template for Java
class MinHeap {
    int[] harr;
    int capacity; int heap_size;
    MinHeap(int cap) {
        heap_size = 0;
        capacity = cap;
        harr = new int[cap];
    }
    int parent(int i) { return (i - 1) / 2; }
    int left(int i) { return (2 * i + 1); }
    int right(int i) { return (2 * i + 2); }

    // You need to write code for below three functions
    int extractMin() {
        if(heap_size == 0){
            return -1 ;
        }else if(heap_size == 1){
            heap_size--;
            return harr[0] ;
        }
        
        heap_size--;
        swap(0, heap_size) ;
        MinHeapify(0) ;
        
        return harr[heap_size] ;
    }
    
    void swap(int index1, int index2){
        int temp = harr[index1] ;
        harr[index1] = harr[index2] ;
        harr[index2] = temp ;
    }

    void insertKey(int k) {
        if(heap_size == capacity)return ;
        heap_size++ ;
        harr[heap_size-1] = k ;
        
        int current = heap_size-1 ;
        while(current != 0 && harr[current] < harr[parent(current)]){
            swap(current, parent(current)) ;
            current = parent(current) ;
        }
    }

    void deleteKey(int i) {
        if(heap_size == 0)return ;
        
        if(i < 0 || i >= heap_size)return ;
        
        decreaseKey(i, -1) ;
        extractMin() ;
    }

    // Decrease key operation, helps in deleting the element
    void decreaseKey(int i, int new_val) {
        harr[i] = new_val;
        while (i != 0 && harr[parent(i)] > harr[i]) {
            int temp = harr[i];
            harr[i] = harr[parent(i)];
            harr[parent(i)] = temp;
            i = parent(i);
        }
    }

    /* You may call below MinHeapify function in
      above codes. Please do not delete this code
      if you are not writing your own MinHeapify */
    void MinHeapify(int i) {
        int l = left(i);
        int r = right(i);
        int smallest = i;
        if (l < heap_size && harr[l] < harr[i]) smallest = l;
        if (r < heap_size && harr[r] < harr[smallest]) smallest = r;
        if (smallest != i) {
            int temp = harr[i];
            harr[i] = harr[smallest];
            harr[smallest] = temp;
            MinHeapify(smallest);
        }
    }
}
