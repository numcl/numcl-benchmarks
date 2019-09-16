
(in-package :ros.script.benchmark)

(defconstant +trials+ 100)

(defparameter *header-width* 20)

(defun call-with-benchmark (trials fn &key (warmup 3))
  (let (user-run-time-us-s
        system-run-time-us-s
        real-time-ms-s
        gc-run-time-ms-s)
    (sb-ext:gc)
    (dotimes (i (+ warmup trials))
      (sb-ext:call-with-timing
       (lambda (&key
                  user-run-time-us
                  system-run-time-us
                  real-time-ms
                  gc-run-time-ms &allow-other-keys)
         (when (<= warmup i)
           (push user-run-time-us user-run-time-us-s)
           (push system-run-time-us system-run-time-us-s)
           (push real-time-ms real-time-ms-s)
           (push gc-run-time-ms gc-run-time-ms-s)))
       fn))
    (list (float (/ (reduce #'+ real-time-ms-s)       1000))
          (+ (float (/ (reduce #'+ user-run-time-us-s)   1000000))
             (float (/ (reduce #'+ system-run-time-us-s) 1000000)))
          (float (/ (reduce #'+ user-run-time-us-s)   1000000))
          (float (/ (reduce #'+ system-run-time-us-s) 1000000))
          (float (/ (reduce #'+ gc-run-time-ms-s)     1000))

          (float (/ (alexandria:median real-time-ms-s)       1000))
          (+ (float (/ (alexandria:median user-run-time-us-s)   1000000))
             (float (/ (alexandria:median system-run-time-us-s) 1000000)))
          (float (/ (alexandria:median user-run-time-us-s)   1000000))
          (float (/ (alexandria:median system-run-time-us-s) 1000000))
          (float (/ (alexandria:median gc-run-time-ms-s)     1000))

          (float (/ (reduce #'max real-time-ms-s :initial-value 0)       1000))
          (+ (float (/ (reduce #'max user-run-time-us-s :initial-value 0)   1000000))
             (float (/ (reduce #'max system-run-time-us-s :initial-value 0) 1000000)))
          (float (/ (reduce #'max user-run-time-us-s :initial-value 0)   1000000))
          (float (/ (reduce #'max system-run-time-us-s :initial-value 0) 1000000))
          (float (/ (reduce #'max gc-run-time-ms-s :initial-value 0)     1000)))))

(defmacro with-timing ((&key (trials +trials+) (name "N/A")) &body body)
  (when (< *header-width* (length name))
    (setf name (subseq name 0 *header-width*)))
  `(progn
     (format *trace-output* "~va ~{ ~6,4f  ~}~%"
             ,*header-width* ,name
             (call-with-benchmark ,trials (lambda () ,@body)))
     (finish-output *trace-output*)))

(defun banner ()
  (format *trace-output* "~va ~@{~22@a                      |~}~%"
          *header-width*
          "##"
          'sum
          'median
          'max)
  (format *trace-output* "~va ~@{ ~6a  ~}~%"
          *header-width*
          "##"
          'real 'total 'usr 'sys 'gc
          'real 'total 'usr 'sys 'gc
          'real 'total 'usr 'sys 'gc))
