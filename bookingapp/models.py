from django.db import models

# Create your models here.
my_choice = (
    ('S1','s1'),
    ('S2','s2'),
    ('S3','s3'),
    ('S4','s4'), 
)
S1, S2, S3, S4 = (
    ('U', 'upper'),
    ('L', 'lower'),
    ('M', 'middle'),
    ('S', 'side'),
)

ticket_choice = (
    ('upper', 'upper'),
    ('lower','lower'),
    ('middle','middle'),
    ('side','side'),
)

class Portions(models.Model):
    upper = models.CharField(max_length = 2, choices = ticket_choice, blank = False, null = False)
    lower = models.CharField(max_length = 2, choices = ticket_choice, blank = False, null = False)
    middle = models.CharField(max_length = 2, choices = ticket_choice, blank = False, null = False)
    side = models.CharField(max_length = 2, choices = ticket_choice, blank = False, null = False)

class Coaches(models.Model):
    S1 = models.ForeignKey(Portions,max_length = 8, related_name='S1', on_delete= models.CASCADE)
    S2 = models.ForeignKey(Portions,max_length = 8, related_name='S2', on_delete= models.CASCADE)
    S3 = models.ForeignKey(Portions,max_length = 8, related_name='S3', on_delete= models.CASCADE)
    S4 = models.ForeignKey(Portions,max_length = 8, related_name='S4', on_delete= models.CASCADE)

class Tickets(models.Model):
    confmd_tkts = models.IntegerField(Coaches, editable= False, default= 24)
    rac_tickets = models.PositiveIntegerField(Coaches, default= 3)
    waiting_list = models.PositiveIntegerField(Coaches, default= 5)

    def __str__(self):
        return self.waiting_list

    def inc_waiting_list(self):
        self.waiting_list -= 1
        self.save()    

    def inc_rac_tickets(self):
        self.rac_tickets -= 1
        self.save()

class Passenger(models.Model):
    gender_choice = (
        ('M', 'Male'),
        ('F','Female')
    )
    Name = models.CharField(max_length = 30, blank = False, null = False)
    Gender = models.CharField(max_length = 20, choices = gender_choice, blank = False, null = False)
    Age = models.IntegerField(default= 100)
    select_coach = models.ForeignKey(Coaches, on_delete= models.CASCADE, null = False)