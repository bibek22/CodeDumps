(define (factorial n)
  (define (fact-iter product new)
    (if (> new n)
	product
      (fact-iter (* product new) (+ new 1))))
  fact-iter(1 1))
(factorial 4)
