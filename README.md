# Python implementation of Moore's algorithm
**Used in sequencing and scheduling**

The algorithm repeatedly adds jobs in the EDD order to the end of a partial schedule of on-time jobs.

If the addition of job j results in this job being completed after its due date dj, then a job in the partial schedule with the largest processing time is removed and declared late.

All late jobs are scheduled in an arbitrary order after on-time jobs.
