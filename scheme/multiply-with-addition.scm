(define (mult x y)
  (define (double x)
    (+ x x))
  (define (halve n)
	   (/ n 2))

  (cond ((= y 1) x)
	(else (if (not (odd? y))
		  (mult (double x) (halve y))
		  (+ (mult (double x) (halve (- y 1))) x)))))

; doesn't work with negetive value as y!
(mult -2 6)
