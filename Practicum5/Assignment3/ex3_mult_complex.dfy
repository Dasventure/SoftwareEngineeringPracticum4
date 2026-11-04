
/**
 * Compile-time function.
 *
 * Given a natural number (i.e. x >= 0), this will return the number of bits required to represent the number.
 */
function num_bits(x: nat): nat
{
    if x / 2 == 0 then 1 else 1 + num_bits(x / 2)
}

/**
 * Runtime method.
 *
 * This multiplies two positive numbers.
 */
method Mult(a: int, b: int) returns (result: int)
    // Pre-conditions: the algorithm only supports non-negative numbers.
    // This satisfies the condition of the assignment (“only non-negative numbers”).
    // This is necessary for ensuring that result >= 0 and for the invariant result >= 0.
    requires a >= 0
    // This is required because, without it, the invariant b_current >= 0 is not satisfied at the start of the loop.
    requires b >= 0

    // Post-conditions:
    // The result of the method is a product.
    ensures result == a * b
    // (and therefore non-negative)
    ensures result >= 0
{
    result := 0;

    // That variable isn't used anywhere.
    var a_current := a;
    var b_current := b;

    var g := 1;

    while(b_current > 0 || num_bits(b_current)-1 > 0)
        // The right-hand side of the expression can be simplified to b_current >= 2, and it does not contain any additional logic.

        // A --- left-hand side; B --- right-hand side.
        // Two reasons why B has no effect.
        // The first reason is logical:
        // If B is true, then b_current >= 2, and therefore A is also true. B is never true when A is false. Therefore, A || B is always equal to A.

        // The second reason is due to the order of evaluation.
        // || It is evaluated by “short-circuit evaluation”: B is evaluated only if A is false.
        // Since b_current never becomes negative, this happens only once—when b_current = 0 and the loop is about to terminate.
        // And then B = 1 - 1 > 0 = false.

        // ----------

        // Invariant:

        // Bounds of the variables:
        // Fixes a bug in nat: this way, Dafny knows that num_bits(b_current) is called correctly.
        invariant b_current >= 0
        invariant g >= 1
        invariant result >= 0

        // Main Invariant: "what is already computed" + "what is still left" == a * b

        // 1. If it is executed at the beginning of the loop. result = 0, g = 1, b_current = b, so 0 + a*1*b = a*b.

        // 2. And it is stored at each iteration.
        // Let q = b_current / 2 and r = b_current % 2. Then b_current = 2q + r. After the loop body:
        // result' + a*g'*b' = (result + a*g*r) + a*(2g)*q
        // = result + a*g*(r + 2q)
        // = result + a*g*b_current
        // = a*b

        // 3. After exiting, it returns a result.
        // The loop has ended, so the condition is false: b_current <= 0.
        // Together with the invariant b_current >= 0, this implies b_current = 0.
        // Then result + a*g*0 = a*b, that is, result = a*b.

        invariant result + a * g * b_current == a * b

        // ----------

        // Variant:
        // b_current is halved every iteration.
        // Dafny itself won't be able to figure this one out: because of the unusual condition with ||, it won't find a matching expression.
        decreases b_current

        // num_bits(b_current) is not a variant option.
        // num_bits(1) = num_bits(0) = 1, so this value does not decrease during the last iteration.
    {
        // Follow directly from point 2 of the Main Invariant.
        assert b_current == 2 * (b_current / 2) + b_current % 2;
        assert a * g * b_current == a * g * (b_current % 2) + a * (g * 2) * (b_current / 2);

        result := result + a * g * (b_current % 2);

        b_current := b_current / 2;
        g := g * 2;
    }

    // After the loop: b_current >= 0 and the guard is false, so b_current == 0
    assert b_current == 0;

    return result;
}
