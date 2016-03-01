(define (count-change amount)
  (cc amount 5))

(define (cc amount coin-type)
  (cond ((= amount 0) 1)
	((or (< amount 0) (= coin-type 0)) 0)
	(else (+ (cc (- amount (denomination coin-type)) coin-type)
		 (cc amount (- coin-type 1))))))

(define (denomination type)
  (cond ((= type 1) 1)
	((= type 2) 5)
	((= type 3) 10)
	((= type 4) 25)
	((= type 5) 50)))

(count-change 100)
(denomination 3)
