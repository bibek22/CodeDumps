(define (f n)
  (cond ((< n 3) n)
	(else (+ (f (- n 1)) (* (f (- n 2)) 2) (* (f (- n 3)) 3)))))

(define (f n)
  (define (counter a b c n)
    (if (= n 0)
	a
	(counter a (
)
