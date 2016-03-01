
(define (sqrt x guess )
  (define (average x y)
  (/ (+ x y) 2))

  (define (goodenough? x guess)
  (< (abs (- (square guess) x)) .001))

  (if (goodenough? x guess)
      guess
      (sqrt  x (average guess (/ x guess)))))

(define (square x)
  (* x x))


(sqrt 4 1.0)


(define (sqrt x guess )
  (if (goodenough? x guess)
      guess
      (sqrt  x (average guess (/ x guess)))))
