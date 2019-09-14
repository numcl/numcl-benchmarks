
(in-package :ros.script.benchmark)

(defconstant +trials+ 100)

(defun call-with-benchmark (trials fn)
  (let (user-run-time-us-s
        system-run-time-us-s
        real-time-ms-s
        gc-run-time-ms-s)
    (sb-ext:gc)
    (dotimes (i (+ 3 trials))
      (sb-ext:call-with-timing
       (lambda (&key
                  user-run-time-us
                  system-run-time-us
                  real-time-ms
                  gc-run-time-ms &allow-other-keys)
         (when (<= 3 i)
           (push user-run-time-us user-run-time-us-s)
           (push system-run-time-us system-run-time-us-s)
           (push real-time-ms real-time-ms-s)
           (push gc-run-time-ms gc-run-time-ms-s)))
       fn))
    (values (float (/ (alexandria:mean user-run-time-us-s)   1000000))
            (float (/ (alexandria:mean system-run-time-us-s) 1000000))
            (float (/ (alexandria:mean real-time-ms-s)       1000))
            (float (/ (alexandria:mean gc-run-time-ms-s)     1000)))))

(defmacro with-timing ((&key (trials +trials+) (name "N/A")) &body body)
  `(multiple-value-bind (usr sys real gc)
       (call-with-benchmark ,trials (lambda () ,@body))
     (format *trace-output* "~20a ~@{~6,4f~^    ~}~%" ,name real (+ usr sys) usr sys gc)
     (finish-output *trace-output*)))

(defun banner ()
  (format *trace-output* "~20a ~@{~6a~^    ~}~%" "##" 'real 'total 'usr 'sys 'gc))
