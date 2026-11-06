/*
 * Runtime method.
 *
 * Method that takes an array 'arr' and replaces every element in that array with
 * the value 'replacement'.
 */
method erase_array(arr: array<int>, replacement: int) returns () modifies arr
    requires arr.Length >= 0
    // Post-condition: every element in the array equals 'replacement'
    ensures forall k :: 0 <= k < arr.Length ==> arr[k] == replacement
{
    var i := 0;

    while i < arr.Length
        // Invariant 1: i stays within bounds (i == arr.Length when the loop ends)
        invariant 0 <= i <= arr.Length
        // Invariant 2: all elements before i have already been replaced
        invariant forall k :: 0 <= k < i ==> arr[k] == replacement
        // Variant: number of elements still to process, decreases by 1 each iteration
        decreases arr.Length - i
    {
        arr[i] := replacement;

        i := i + 1;
    }

    return;
}
