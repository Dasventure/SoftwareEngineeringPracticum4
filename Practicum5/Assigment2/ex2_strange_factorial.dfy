
/**
 * Compile-time function.
 *
 * Returns the factorial of n such that n! = n * (n-1) * ... * 1
 */
function fact_recursive(n: nat): nat {
    if n == 0 || n == 1 then 1 else n * fact_recursive(n-1)
}

/**
 * Runtime method.
 *
 * Returns the factorial of n such that n! = n * (n-1) * ... * 1
 */
method strange_factorial(n: nat) returns (retval: nat)
    ensures retval == fact_recursive(n)
    // A straightforward post-condition: the return value should be equal to the factorial of n
    // That is what this function promises
{
    var R := 0;
    retval := 1;

    while (R < n || retval != fact_recursive(n))
        invariant n - R >= 0 && retval == fact_recursive(R)
        // PROOF (n - R >= 0): Initially R = 0, retval = 1 = 0!. Inside the body R < n: if R == n then is retval == n! And the guard would be false (loop stops).
        
        // PROOF (retval == fact_recursive(R)):
        // The loop body will update retval and R, R gets incremented by 1, and retval gets updated to (R+1) * V, where V is the value of retval before the loop body. 
        // The invariant states that retval is equal to fact_recursive(R), which is true because after the loop body, retval will be equal to (R+1) * fact_recursive(R) = fact_recursive(R+1). 
        decreases n - R 
        // As R gets incremented, n - R decreases strictly, we choose n because it is a constant and the loop teminates when R == n && retval == fact_recursive(n) (Then n - R == 0, so zero is a lower-bound)
    {   
        var V := retval;

        var S := 1;
        while (S <= R || retval != (R+1) * V)
            invariant R + 1 - S >= 0 && retval == S * V
            // PROOF (R + 1 - S >= 0): Initially S = 1 and retval = V = 1 * V. Inside the body S <= R (otherwise S == R+1, but then retval == (R+1)*V and the guard would be false)
            // PROOF (retval == S * V): The body adds V, so S*V+V = (S+1)*V.
            decreases R + 1 - S 
            // As S gets incremented, R + 1 - S decreases, we choose R + 1 because it is a constant in this specific loop and the loop teminates when S == R + 1 (Then R + 1 - S == 0, so zero is a lower-bound)
        {
            retval := retval + V;
            S := S + 1;
        }

        R := R + 1;
        
    }

    return retval;
}
