(define lat?
  (lambda (l)
    (cond
     ((null? l ) #t)
     ((atom? car) (lat? (cdr l)))
     (else #f)))
  )
(define (atom? x)
  (and (not (pair? x)) (not (null? x))))

(define new '(just another list))
(lat? '(that is awesome))
(lat? new)
(lat? nw)

(define (member? l a)
  (cond ((null? l) #f)
	((eq? (car l) a) #t)
	(else (member? (cdr l) a))))
(member? new 'jus)

(define (rember a l)
  (cond
   ((null? l) '())
   ((eq? a (car l)) (cdr l))
   (else (cons (car l)
	       (rember a
		       (cdr l))))))

(rember 'list new)

(define firsts
  (lambda (l)
    (cond ((eq? l '()) '())
	  (else (cons (caar l) (firsts (cdr l)))))))

(define newlist '((that is) (also)))
(firsts newlist)
(cdr (cdr newlist))
(atom? (cdr newlist))


(define (replace new old lat)
  (cond
   ((null? lat) '())
   ((eq? (car lat) old) (cons new
			      (cdr lat)))
   (else
    (cons
     (car lat) (replace new old
			(cdr lat))))))

(define (replace2 new o1 o2 lat)
  (cond
   ((null? lat) '())
   ((or
     (eq? (car lat) o1)
     (eq? (car lat) o2)) (cons
			  new
			  (cdr lat)))
   (else
    (cons
     (car lat)
     (replace2 new o1 o2 (cdr lat))))))



(define (insertR new old lat)
  (cond
   ((null? lat) '())
   ((eq? (car lat) old) (cons
			 old (cons
			      new (cdr lat))))
   (else
    (cons (car lat) (insertR new old (cdr lat))))))

(insertR '(new one) 'another new)

(define (insertL new old lat)
  (cond
   ((null? lat) '())
   ((eq? old (car lat)) (cons new
			      lat))
   (else
    (cons
     (car lat)
     (insertL new old (cdr lat))))))
(insertL '(new one) 'another new)

(replace2 '(inteligente) 'another 'list new)


(define (multirember a l)
  (cond
   ((null? l) '())
   ((eq? a (car l)) (multirember a (cdr l)))
   (else (cons (car l)
	       (multirember a
		       (cdr l))))))
(set! new '(ba dum dum tss))
(multirember 'dum new)



(define (multiinsertR new old lat)
  (cond
   ((null? lat) '())
   ((eq? (car lat)
	 old)
    (cons
     old (cons
	  new
	  (multiinsertR new old (cdr lat)))))
   (else
    (cons
     (car lat)
     (multiinsertR new old (cdr lat))))))


(define (multiinsertL new old lat)
  (cond
   ((null? lat) '())
   ((eq? old (car lat)) (cons new (cons old 
					(multiinsertL new old (cdr lat)))))
   (else
    (cons
     (car lat)
     (multiinsertL new old (cdr lat))))))



(define (multireplace new old lat)
  (cond
   ((null? lat) '())
   ((eq? (car lat) old)
    (cons new
	  (multireplace new old (cdr lat))))
   (else
    (cons
     (car lat) (multireplace new old
			     (cdr lat))))))

(define multi '(that that and that is worthless))
(multiinsertL 'this 'that multi)


