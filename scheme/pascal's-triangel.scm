;; (define l '(1))
;; (define new (cons 2 l))
;; (cdr new)
;; (define (maker previous new)
;;   (if (null? '(cdr previous ))
;;       (cons 

(define (pascal-triangle row col)
  (cond ((= row 0) 0)
	((= col 1) 1)
	((= col row) 1)
	((> col row) 0)
	(else (+ (pascal-triangle (- row 1) (- col 1)) (pascal-triangle (- row 1) col) ) )))
(pascal-triangle 7 4)

