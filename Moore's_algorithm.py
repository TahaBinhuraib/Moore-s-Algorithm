"""
Moore's algorithm
example question:
Number of jobs = 5
Job 1: due date and processing time=(9,7)
Job 2: due date and processing time=(17,8)
Job 3: due date and processing time=(18,4)
Job 4: due date and processing time=(19,6)
Job 5: due date and processing time=(21,6)
output:
1. -----> Job3 the lateness of the job is-14
2. -----> Job4 the lateness of the job is-9
3. -----> Job5 the lateness of the job is-5
4. -----> Job1 the lateness of the job is14
5. -----> Job2 the lateness of the job is14
total number of tardy jobs = 2
---------------------------------------------------------------
Minimize the total number of tardy jobs
first index is due date, the second index is the processing time, third index is the number of job
author: Taha Osama A Binhuraib
"""

jobs = []
n = int(input("Enter number of Jobs : "))

for i in range(0, n):
    temp = [
        int(input(f"please enter the due date for job({i+1}): ")),
        int(input(f"processing time for job({i+1}) : ")),
        int(i + 1),
    ]
    jobs.append(temp)
# i used this function to find the maximum processing time
def largest(arr, n):
    max = 0
    finalarr = []
    for i in range(0, n):
        if arr[i][1] > max:
            max = arr[i][1]
            finalarr = arr[i]

    return finalarr


j = []
jc = []
jd = []
total_processing = 0

no_of_jobs = len(jobs)
k = 0
# sort the jobs in ascending order according to their due dates
jobs.sort()
# to decide on first Job
if k == 0 and jobs[0][0] >= jobs[0][1]:
    jc.append(jobs[0])
    k += 1
    total_processing += jobs[0][1]
else:
    jd.append(jobs[0])
    k += 1

# updating the size of the Jc array
n = len(jc)
x = 0
# variable to keep track of processing times removed from Js
xtime_removal = 0
while k <= no_of_jobs - 1:
    if float(jobs[k][1] + total_processing) <= float(jobs[k][0]):
        jc.append(jobs[k])
        total_processing += jobs[k][1]
        k += 1
        n = len(jc)

    else:
        jc.append(jobs[k])
        n = len(jc)
        jd.append(largest(jc, n))

        xtime_removal = x = largest(jc, n)
        total_processing -= x[1]
        total_processing += jobs[k][1]
        jc.remove(largest(jc, n))
        n = len(jc)
        k += 1

jd.reverse()
final = jc + jd
# a variable to keep track of the loop while iterating through the elements of the final schedueled array
q = len(final)
print("the sequence of the job is as following: ")
processing = 0


for i in range(q):
    print(
        f"{i+1}. -----> Job{final[i][2]} the lateness of the job is {(processing + final[i][1]) - final[i][0]} "
    )
    processing += final[i][1]
    i += 1

print(f"total number of tardy jobs = {len(jd)}")
