(cons '(l) '(new shit))
(define l '())
(null? 'l)
(define (lat? x)
  (cond ((not (and  (null? x) (not (eq? x '())))) '#t)
	(else '#f)))
(lat? l)