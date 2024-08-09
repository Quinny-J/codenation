class Person():
    
    def __init__(self, person_name, person_age, person_height):
        self.name = person_name
        self.age = person_age
        self.height = person_height

    def set_new_name(self, person_name):
        self.name = person_name

    def set_hair_colour(self, hair_colour):
        self.set_hair_colour = hair_colour

    def set_job(self, job_title):
        allowed_jobs = ["developer", "admin", "compliance", "insutrctor", "hr", "finance"]
        while job_title not in allowed_jobs:
            print("Job does not exists")
            job_title = input("Please try again : ")
        else:
            self.job = job_title
            print("Job updated properly")