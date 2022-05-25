# Python Implementation of Moore's Algorithm :snake:
**Used in sequencing and scheduling**

The algorithm repeatedly adds jobs in the EDD order to the end of a partial schedule of on-time jobs.

If the addition of job ```j``` results in this job being completed after its due date ```dj```, then a job in the partial schedule with the largest processing time is removed and declared late. All late jobs are scheduled in an arbitrary order after on-time jobs.
## Example Input-Output
### **Input**

Number of jobs = ```5```

**Job 1:** due date and processing ```time=(9,7)```

**Job 2:** due date and processing ```time=(17,8)```

**Job 3:** due date and processing ```time=(18,4)```

**Job 4:** due date and processing ```time=(19,6)```

**Job 5:** due date and processing ```time=(21,6)```

### **output:**
```
1. -----> Job3 the lateness of the job is-14

2. -----> Job4 the lateness of the job is-9

3. -----> Job5 the lateness of the job is-5

4. -----> Job1 the lateness of the job is14

5. -----> Job2 the lateness of the job is14
total number of tardy jobs = 2
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
