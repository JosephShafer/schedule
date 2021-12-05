# need 29 to start
# 3 at end
# 8 10 12 hour shifts possible
# 1 FTE = 8 hours
# .75 of FTE in 0700 - 1500 (8)
# .25 of FTE in 1500 - 1700 (2)


# Questions to answer: why is 10 hours '8 hours of FTE'? hour lunch + 2 30 min breaks?
# start at 0700 or 0630 end at 1900 or end at 2300?
# working under assumptions:
# First 8 hours of any shift are cut up into .09375 discrete chunks
# any after that are in .125 chunks
# Timeblock is 0700 to 2300

class ShiftWorker:
    def __init__(self, worker_name, start_time=700):
        self.FTE_to_sum = 0.09375
        self.FTE_worked = 0
        self.hours_worked = 0
        self.start_time = start_time
        self.worker_name = worker_name
        self.available_for_work = True

    def work_hour(self):
        if self.available_for_work is False:
            return
        self.FTE_worked += self.FTE_to_sum
        self.hours_worked += 1
        if self.hours_worked == 8:
            self.FTE_value_increase()
        if self.hours_worked == 12:
            self.available_for_work = False

    def FTE_value_increase(self):
        self.FTE_to_sum = 0.125


class ShiftTracker:
    worker_id = 1
    worker_list = []
    shift_check_marks = {700: 29, 1500: 22, 1700: 14, 1900: 3}
    start_time = 700
    end_time = 2300
    current_time = start_time

    def create_worker(self):
        self.worker_list.append(ShiftWorker("Worker_" + str(self.worker_id)))
        self.worker_id += 1

    def count_active_workers(self):
        active_count = 0
        for i in self.worker_list:
            if i.available_for_work:
                active_count += 1
        return active_count

    def work_day(self):
        while self.current_time < 2300:
            print(self.current_time, self.count_active_workers())
            for i in self.worker_list:
                i.work_hour()

            self.current_time += 100
            while(self.current_time in self.shift_check_marks and self.count_active_workers() < self.shift_check_marks[self.current_time]):
                self.create_worker()

    def utility_get_total_FTE(self):
        FTE = 0.0
        for i in self.worker_list:
            FTE += i.FTE_worked
        print(FTE)
    
    def utility_print_total_hours_per_employee(self):
        for i in self.worker_list:
            print(i.hours_worked)


def driver():
    # Setup initial worker 29 worker set
    shift_tracker = ShiftTracker()
    for _0 in range(1, 30):
        shift_tracker.create_worker()

    shift_tracker.work_day()
    shift_tracker.utility_get_total_FTE()
    shift_tracker.utility_print_total_hours_per_employee()



driver()
