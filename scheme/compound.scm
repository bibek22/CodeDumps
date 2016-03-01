(define rate .02)
(define member 8)
(define (newmonth current-worth)
  (+ current-worth (* rate current-worth) (* 100 member)))

(define (newyear current-worth n)
  (cond ((zero? n) current-worth)
	(else (newyear (newmonth current-worth) (- n 1)))))

(define (calculate iw y m)
  (cond ((zero? y)
	 (cond ((zero? m) iw)
	       (else (calculate (newmonth iw) y (- m 1)))))
	(else (calculate (newyear iw 12) (- y 1) m))))
(calculate 37869 0 18)


;; (define (at-time start year [month 0])
;;   (cond ((zero? year)
;; 	 (cond ((zero? month) start)
;; 	       (else
;; 		(at-time (newmonth start) year (-  month 1)))))
;; 	(else (at-time (newyear start 12) (- year 1) month))))
