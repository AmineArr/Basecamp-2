more_inp = input("More Letters?").lower()
if more_inp != "yes" and more_inp != "no":
    print("Input error")
    exit()
elif more_inp == "no":
    exit()
else:
    option_inp = input("Job Offer or Rejection?").lower()
    if option_inp != "job offer" and option_inp != "rejection":
        print("Input error")
        exit()

if option_inp == "job offer":
    first_inp = input("First Name?")
    last_inp = input("Last Name?")
    job_inp = input("Job Title?")
    salary_inp = input("Annual Salary?")
    date_inp = input("Start Date?(YYYY-MM-DD)")

    def is_name_valid(first_inp, last_inp)->bool:
        if first_inp >= 2 and first_inp <= 10 and first_inp[0].isupper() and last_inp >= 2 and last_inp <= 10 and last_inp[0].isupper():
            print("input error")


    def is_title_valid(job_inp)->bool:
        if len(job_inp) > 10 and job_inp.isalpha():
            print("input error")
    def is_salary_valid(salary_inp)->bool:
        pass

    def is_date_valid(date_inp)->bool:
        if date_inp[0:5] != ["2021", "2022"] and date_inp[6:8] != ['1', "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
            print("Input error")

    print(f"""Here is the final letter to send: Dear {first_inp} {last_inp},
After careful evaluation of your application for the position of {job_inp},
we are glad to offer you the job. Your salary will be {salary_inp} euro annually.
Your start date will be on {date_inp}. Please do not hesitate to contact us with any questions.
Sincerely,
HR Department of XYZ""")
    