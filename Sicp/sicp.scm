(define (square x) (* x x))
(square 2)
(square (+ 2 5))
(square (square 3))
(+ (square 3) (square 3))

(define (sum-of-squares x y)
 (+ (square x) (square y)))
(sum-of-squares 3 4)
()