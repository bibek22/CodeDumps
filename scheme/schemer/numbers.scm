(define (add1 n)
  (+ n 1))

(define (sub1 n)
  (- n 1))

(define (+ m n)
  (cond ((zero? n) m)
	(else (+ (add1 m) (sub1 n)))))

(define (* m n)
  (cond ((zero? n) 0)
	(else (+ m (* m (sub1 n))))))
(* 2 22)

(define (tup+ tup1 tup2)
  ;; only takes tup of same length
  (cond ((and (null? tup1) (null? tup2)) '())
	((or (null? tup1) (null? tup2)) (error "Tups of unequal length given"))
	(else (cons (+ (car tup1) (car tup2))
		    (tup+ (cdr tup1) (cdr tup2))))))
(define tup1 '(1 2 5 6 8))
(define tup2 '(7 2 3 2 0 1))

(tup+ tup1 tup2)  ; reports error with above two tups

(define (tup++ tup1 tup2)
  ;; adds elements of tuple and cons the element
  ;; on either tup that doesn't have a pair to
  ;; the back or return tup
  
  (cond ((null? tup1) tup2)
	((null? tup2) tup1)	
	(else
	 (cons
	  (+ (car tup1) (car tup2))
	  (tup+ (cdr tup1) (cdr tup2))))))

(define (> n m)
  (cond ((zero? n) #f)
	  ((zero? m) #t)
	  (else (> (sub1 n) (sub1 m))))
  (define (compare n m)
    (cond ((zero? n) #f)
	  ((zero? m) #t)
	  (else (> (sub1 n) (sub1 m))))))

(define (< n m)
  (cond
   ((zero? m) #f)
   ((zero? n) #t)
   (else (< (sub1 n) (sub1 m)))))
(define (= n m)
  (cond
   ((eq? (- n m) 0) #t)
   (else #f)))
(= -2 -2) ; #t

(define (exp n m)
  (cond
   ((zero? m) 1)
   (else (* n (exp n (sub1 m)) ))))
(exp 2 4)

(define (% n m)
  (cond (( < n m) 0)
	((eq? m 0) (error "Division by zero not allowed !"))
	(else (add1 (% (- n m) m)))))

(% 9 1)

(define (length lat)
  (cond ((null? lat) 0)
	(else (add1 (length (cdr lat))))))
(length '(2 1 5 4))

(define num '(2 1 5 4))

(define (pick n lat)
  ;; count begins at 0
  (cond ((zero? n) (car lat))
	(else (pick (sub1 n) (cdr lat)))))

(pick 0 num)

(define  (rempick n lat)
  ;; n starts from 0
  (cond ((zero? n) (cdr lat))
	(else
	 (cons
	  (car lat) (rempick (sub1 n) (cdr lat))))))

(rempick 3 num)

(number? 3)

(define (no-nums lat)
  (cond
   ((null? lat) '())
   ((number? (car lat))(no-nums (cdr lat)) )
   (else
    (cons
     (car lat) (no-nums (cdr lat))))))

(define mix '(1 2 2 a 25 between two ferns))
(no-nums mix)

(define (all-nums lat)
  (cond ((null? lat) '())
	((not
	  (number? (car lat)))
	 (all-nums (cdr lat)))
	(else (cons (car lat) (all-nums (cdr lat))))))

(all-nums mix)

(define (eqan? a1 a2)
  ; takes two atoms only
  (cond ((and (number? a1) (number? a2))
	 (= a1 a2))
	((or (number? a1) (number? a2)) #f)
	(else (eq? a1 a2))))


(define (occur a lat)
  (cond ((null? lat) 0)
	((eqan? a lat))))

(define (one? a)
  (cond ((zero? a) #f)
	(else (zero? (sub1 a)))))


(define lat?
  (lambda (l)
    (cond
     ((null? l ) #t)
     ((atom? car ) (lat? (cdr l)))
     (else #f))))

(define (atom? x)
  (and (not (pair? x)) (not (null? x))))

(define multi '(that (is so) awesome (I can't ) even that))

(rember* 'that multi)

(lat? (car multi))

(define  (rember* a l)
  (cond ((null? l) '())
	((lat? (car l)) (rember* a (car l)))
	((eq? a (car l)) (rember* a (cdr l)))
	(else
	 (cons (car l) (rember* a (cdr l))))))

(define (numbered? exp)
  (cond
   (())))
