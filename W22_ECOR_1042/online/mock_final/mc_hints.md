# Hints for Mock Multiple Choice

1. Lecture 4, slide 6
2. PyTutor. Also, review the input function and the type it returns
3. PyTutor. Lists.
4. Lecture 1
5. Lecture 7 - run `merge_sort_example.py`. Also explanation below.
6. Not a great mc question since you'd probably need Wing. **Try doing it with numpy**. If you want to do it by hand, equations are [here](https://images.saymedia-content.com/.image/c_limit%2Ccs_srgb%2Cq_auto:eco%2Cw_700/MTc0NjM5MDEyNTAwNTQ3NTc0/how-to-create-a-simple-linear-regression-equation.webp) for y = Bx + A (I'm not sure if this is a requirement for the ECOR 1042 this term)
7. PyTutor. Tuples.
8. Lecture 7 - a pass means one insertion.
9. PyTutor.
10. PyTutor. Review the difference between [] and .get(). Also make sure you know what .append() returns.
11. Lecture 6, part 1, slide 8.
12. PyTutor. Review string slicing and dictionaries. Note that if `s = "hello"` then `s[0:3]` gives me indices 0 up to (3-1) of the string so `"hel"`.
13. 
    i)  Lecture 10. This is also a bad question - you'd need 5 iterations but that's too many for an exam. Instead, try doing golden-search twice and make sure that after the two iterations you can get a new search range of [0.5485, 1.2742]. \
    ii) Lecture 6, part 2. The answer is not e).

##### Explanation of 5.

First run `merge_sort_example.py` to see print statements of what's getting merged -> that shows you the answer.

Here's why, the key is in these lines:
```py
    mid = len(lst) // 2
    l = merge_sort(lst[:mid])
    r = merge_sort(lst[mid:])
```

Notice that before we even do `r = merge_sort(lst[mid:])`, we've already called `merge_sort()` on the left half `l = merge_sort(lst[:mid])`. This function call needs to return before we can get to the right half. In other words, we first split the list into a left half: `[18, 2, 9]` (make sure you know where that came from) - and this gets sorted FIRST before I even touch the right half since we called `merge_sort()` on it.

Now apply the same thinking to merge sorting `[18, 2, 9]` and hopefully it makes sense what the answer is.


##### Lists are mutable
Since lists are mutable, we can *modify* a list without reassigning its value.

For example, to update the values in a tuple, we need to do:
```py
    tupleA = (1, 2)

    # Add a three

    tupleA = (1, 2) + (3,)
```

But with a list,
```py
    listA = [1, 2]

    # Add a three
    listA.append(3) # There's no assignment sign => I modified the original list
```

The impliciation is that when you give a function a list, it can modify the original list (it doesn't create a new variable for the list parameter
in its new frame). This means, functions that modify lists do not need to return anything since they're already modifying the list you gave them.

To see this visually, run this in python tutor and pay attention to the arrows:
```python
    def example_function(list_parameter: list) -> None:
        list_parameter.append(1)
    
    lst = [1, 2, 3]
    example_function(lst)   # Look at where list_parameter is pointing, look at where lst is pointing.
    print(lst)              # This should have an extra 1
```