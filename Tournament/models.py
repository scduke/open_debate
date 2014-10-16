from django.db import models
from django.contrib.auth.models import User

#These constants map the events to a two letter abbreviation

ORIGINAL_ORATORY = 'OO'
STANDARD_ORATORY = 'SO'
PROSE = 'PR'
DRAMATIC_INTERP = 'DI'
HUMOROUS_INTERP = 'HI'
FOREIGN_EXTEMP = 'FX'
DOMESTIC_EXTEMP = 'DX'
MONOLOGUE = 'MO'
LD_DEBATE = 'LD'
POETRY = 'PO'
CROSS_EXAM_DEBATE = 'CX'
HUMOROUS_DUET = 'HD'
DRAMATIC_DUET = 'DD'
PUBLIC_FORUM = 'PF'

EVENT_CHOICES = (
    (ORIGINAL_ORATORY, 'OO'),
    (STANDARD_ORATORY, 'SO'),
    (PROSE, 'PR'),
    (DRAMATIC_INTERP, 'DI'),
    (HUMOROUS_INTERP, 'HI'),
    (FOREIGN_EXTEMP, 'FX'),
    (DOMESTIC_EXTEMP, 'DI'),
    (MONOLOGUE, 'MO'),
    (LD_DEBATE, 'LD'),
    (POETRY, 'PO'),
    (CROSS_EXAM_DEBATE, 'CX'),
    (HUMOROUS_DUET, 'HD'),
    (DRAMATIC_DUET, 'DD'),
    (PUBLIC_FORUM, 'PF') )


class School(models.Model):
    """
    Model representation of a school. Maps a one-to-many relationship with
    students, coaches, and judges.
    """
    ONE_A = '1A'
    TWO_A = '2A'
    THREE_A = '3A'
    FOUR_A = '4A'
    FIVE_A = '5A'
    SIX_A = '6A'
    SCHOOL_CLASS_CHOICES = (
        (ONE_A, '1A'),
        (TWO_A, '2A'),
        (THREE_A, '3A'),
        (FOUR_A, '4A'),
        (FIVE_A, '5A'),
        (SIX_A, '6A') )

    name = models.CharField(max_length=50)
    competition_class = models.CharField(max_length=2, choices=SCHOOL_CLASS_CHOICES)
    registration_date = models.DateTimeField()
    coach = models.ForeignKey(Coach)


class Student(models.Model):
    """
    Model representation of a student/competitor in the tournament.
    """
    #constants that record the possible grade levels
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior') )

    user = models.OneToOneField(User)   #associates user with a student
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    school = models.ForeignKey(School)
    registration_date = models.DateTimeField()
    year_in_school = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES)
    events = models.CharField(max_length=2, choices=EVENT_CHOICES)

    def is_underclassman(self):
        return self.year_in_school in (self.FRESHMAN, self.SOPHOMORE)


class Coach(models.Model):
    """
    Model representation of a coach.
    """
    user = models.OneToOneField(User)       #maps user to a Coach
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    school = models.ForeignKey(School)
    registration_date = models.DateTimeField()
    tournament_director = models.BooleanField(default=False)


class Building(models.Model):
    """
    Representation of the tournament venue. Maintains a one-to-many relationship with
    room objects.
    """
    school = models.OneToOneField(School)
    street_address = models.CharField(max_length=40)
    city = models.CharField(max_length=30)
    state = models.CharField()
    zip_code = models.CharField(max_length=15)
    rooms = models.ForeignKey(Room)


class Room(models.Model):
    """
    Representation of individual rooms at a tournament venue. Maintains a many-to-one relationship
    with Building objects.
    """
    school = models.OneToOneField(School)
    capacity = models.IntegerField()
    designation = models.CharField(max_length=50)   #meant to record room numbers/letters


class Judge(models.Model):
    """
    Model representation of a Judge.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    coach = models.OneToOneField(Coach)        #maps the Judge to a coach if they're the same person
    events = models.CharField(max_length=2, choices=EVENT_CHOICES)