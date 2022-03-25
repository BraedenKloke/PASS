"""
Author: Braeden Kloke
Version: March 25, 2022

Week: 5
Activity: 2 & 3

This Python code was designed for a "ECOR 1042: Data Management" PASS workshop.

Core concepts covered include:

* Sorting Algorithms

* Documentation


Activity 2: Commenting on Sorting Algorithms
------------------------------------------------
In your own words, write comments describing what the code does for the following sorting algorithms:

* [ ] Bubble Sort

* [ ] Selection Sort

* [ ] Insertion Sort

* [ ] Merge Sort


Activity 3: Visualizing Sorting Algorithms
------------------------------------------------
Copy and paste the 'blocks' below into Python Tutor to visualize how each sorting algorithm works.
Then, go back to the worksheet and perform the sorting algorithms by hand!

* [ ] Bubble Sort:
https://pythontutor.com/visualize.html#code=def%20bubble_sort%28arr%3A%20list%29%20-%3E%20None%3A%0A%20%20%20%20%22%22%22As%20presented%20in%20Lecture%207,%20Winter%202022%22%22%22%0A%20%20%20%20%23%20COMMENTS%0A%20%20%20%20n%20%3D%20len%28arr%29%0A%0A%20%20%20%20%23COMMENTS%0A%20%20%20%20for%20i%20in%20range%28n%29%3A%0A%0A%20%20%20%20%20%20%20%20%23%20COMMENTS%0A%20%20%20%20%20%20%20%20for%20j%20in%20range%280,%20n%20-%20i%20-%201%29%3A%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20COMMENTS%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20COMMENTS%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20COMMENTS%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20arr%5Bj%5D%20%3E%20arr%5Bj%20%2B%201%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20arr%5Bj%5D,%20arr%5Bj%20%2B%201%5D%20%3D%20arr%5Bj%20%2B%201%5D,%20arr%5Bj%5D%0A%0A%23%20Code%20to%20test%20above%0Alst%20%3D%20%5B7,%204,%203,%201,%205,%202,%208,%206%5D%0Abubble_sort%28lst%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

* [ ] Selection Sort:
https://pythontutor.com/visualize.html#code=def%20selection_sort%28arr%3A%20list%29%20-%3E%20None%3A%0A%20%20%20%20%22%22%22As%20presented%20in%20Lecture%207,%20Winter%202022%22%22%22%0A%20%20%20%20%23%20COMMENTS%0A%20%20%20%20n%20%3D%20len%28arr%29%0A%0A%20%20%20%20%23%20COMMENTS%0A%20%20%20%20for%20i%20in%20range%28n%29%3A%0A%0A%20%20%20%20%20%20%20%20%23%20COMMENTS%0A%20%20%20%20%20%20%20%20%23%20COMMENTS%0A%20%20%20%20%20%20%20%20min_idx%20%3D%20i%0A%20%20%20%20%20%20%20%20for%20j%20in%20range%28i%20%2B%201,%20n%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20arr%5Bmin_idx%5D%20%3E%20arr%5Bj%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20min_idx%20%3D%20j%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%23%20COMMENTS%0A%20%20%20%20%20%20%20%20%23%20COMMENTS%0A%20%20%20%20%20%20%20%20arr%5Bi%5D,%20arr%5Bmin_idx%5D%20%3D%20arr%5Bmin_idx%5D,%20arr%5Bi%5D%0A%0A%23%20Code%20to%20test%20above%0Alst%20%3D%20%5B7,%204,%203,%201,%205,%202,%208,%206%5D%0Aselection_sort%28lst%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

* [ ] Insertion Sort:
https://pythontutor.com/visualize.html#code=def%20insertion_sort%28arr%3A%20list%29%20-%3E%20None%3A%0A%20%20%20%20%22%22%22As%20presented%20in%20Lecture%207,%20Winter%202022%22%22%22%0A%20%20%20%20%23%20COMMENTS%0A%20%20%20%20n%20%3D%20len%28arr%29%0A%0A%20%20%20%20%23%20COMMENTS%0A%20%20%20%20for%20i%20in%20range%281,%20n%29%3A%0A%0A%20%20%20%20%20%20%20%20key%20%3D%20arr%5Bi%5D%0A%0A%20%20%20%20%20%20%20%20%23%20COMMENTS%0A%20%20%20%20%20%20%20%20%23%20COMMENTS%0A%20%20%20%20%20%20%20%20%23%20COMMENTS%0A%20%20%20%20%20%20%20%20j%20%3D%20i%20-%201%0A%20%20%20%20%20%20%20%20while%20j%20%3E%3D%200%20and%20key%20%3C%20arr%5Bj%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20arr%5Bj%20%2B%201%5D%20%3D%20arr%5Bj%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20j%20-%3D%201%0A%20%20%20%20%20%20%20%20arr%5Bj%20%2B%201%5D%20%3D%20key%0A%0A%23%20Code%20to%20test%20above%0Alst%20%3D%20%5B7,%204,%203,%201,%205,%202,%208,%206%5D%0Ainsertion_sort%28lst%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

* [ ] Merge Sort:
https://pythontutor.com/visualize.html#code=def%20merge_sort%28arr%3A%20list%29%20-%3E%20None%3A%0A%20%20%20%20%22%22%22As%20presented%20in%20Lecture%207,%20Winter%202022%22%22%22%0A%20%20%20%20%23%20COMMENTS%0A%20%20%20%20if%20len%28arr%29%20%3E%201%3A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%23%20COMMENTS%0A%20%20%20%20%20%20%20%20%23%20COMMENTS%0A%20%20%20%20%20%20%20%20mid%20%3D%20len%28arr%29%20//%202%0A%20%20%20%20%20%20%20%20L%20%3D%20arr%5B%3Amid%5D%0A%20%20%20%20%20%20%20%20R%20%3D%20arr%5Bmid%3A%5D%0A%0A%20%20%20%20%20%20%20%20%23%20COMMENTS%0A%20%20%20%20%20%20%20%20%23%20COMMENTS%0A%20%20%20%20%20%20%20%20merge_sort%28L%29%0A%20%20%20%20%20%20%20%20merge_sort%28R%29%0A%0A%20%20%20%20%20%20%20%20i%20%3D%20j%20%3D%20k%20%3D%200%0A%0A%20%20%20%20%20%20%20%20%23%20COMMENTS%0A%20%20%20%20%20%20%20%20while%20i%20%3C%20len%28L%29%20and%20j%20%3C%20len%28R%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20L%5Bi%5D%20%3C%20R%5Bj%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20arr%5Bk%5D%20%3D%20L%5Bi%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20i%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20arr%5Bk%5D%20%3D%20R%5Bj%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20j%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20k%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%23%20COMMENTS%0A%20%20%20%20%20%20%20%20while%20i%20%3C%20len%28L%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20arr%5Bk%5D%20%3D%20L%5Bi%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20i%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20k%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20while%20j%20%3C%20len%28R%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20arr%5Bk%5D%20%3D%20R%5Bj%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20j%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20k%20%2B%3D%201%0A%0A%23%20Code%20to%20test%20above%0Alst%20%3D%20%5B7,%204,%203,%201,%205,%202,%208,%206%5D%0Amerge_sort%28lst%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

"""

### Block 1 Starts

def bubble_sort(arr: list) -> None:
    """As presented in Lecture 7, Winter 2022"""
    # COMMENTS
    n = len(arr)

    #COMMENTS
    for i in range(n):

        # COMMENTS
        for j in range(0, n - i - 1):

            # COMMENTS
            # COMMENTS
            # COMMENTS
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Code to test above
lst = [7, 4, 3, 1, 5, 2, 8, 6]
bubble_sort(lst)

### Block 1 Ends


### Block 2 Starts

def selection_sort(arr: list) -> None:
    """As presented in Lecture 7, Winter 2022"""
    # COMMENTS
    n = len(arr)

    # COMMENTS
    for i in range(n):

        # COMMENTS
        # COMMENTS
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        
        # COMMENTS
        # COMMENTS
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Code to test above
lst = [7, 4, 3, 1, 5, 2, 8, 6]
selection_sort(lst)

### Block 2 Ends


### Block 3 Starts

def insertion_sort(arr: list) -> None:
    """As presented in Lecture 7, Winter 2022"""
    # COMMENTS
    n = len(arr)

    # COMMENTS
    for i in range(1, n):

        key = arr[i]

        # COMMENTS
        # COMMENTS
        # COMMENTS
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Code to test above
lst = [7, 4, 3, 1, 5, 2, 8, 6]
insertion_sort(lst)

### Block 3 Ends



### Block 4 Starts

def merge_sort(arr: list) -> None:
    """As presented in Lecture 7, Winter 2022"""
    # COMMENTS
    if len(arr) > 1:
        
        # COMMENTS
        # COMMENTS
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        # COMMENTS
        # COMMENTS
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # COMMENTS
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        # COMMENTS
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Code to test above
lst = [7, 4, 3, 1, 5, 2, 8, 6]
merge_sort(lst)

### Block 4 Ends
