(print? "this")

(define (null? l)
  (cond ((eq? l ()) #t)
	(else #f)))

(define (firsts l)
  (cond ((null? l (quote ()))
	(else (cons (car l) (firsts (cdr l)))))))

(null? (this,and,that))


(define (square x)
  (* x x))

(square 4)
