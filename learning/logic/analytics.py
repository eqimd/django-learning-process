from django.db.models.aggregates import Avg
from django.db.models.expressions import F, Subquery
from django.db.models.query import Prefetch, prefetch_related_objects
from django.db.models.query_utils import select_related_descend
from ..models import Student, Lecture, Course

from datetime import datetime

from django.db.models import Count, Sum
from django.db.models.functions import Length


def count_students_listened_lectures():
    students_with_views = Student.objects.annotate(views_sum=Count('followed_courses__lecture'))
    return list(zip(
        students_with_views,
        [views[0] for views in students_with_views.values_list('views_sum')]
    ))


def count_lectures_views():
    lecs_with_views = Lecture.objects.annotate(stud_cnt=Count('related_course__student')).order_by('-stud_cnt')
    return list(zip(
        lecs_with_views,
        [views[0] for views in lecs_with_views.values_list('stud_cnt')]
    ))



def lectures_in_current_year():
    return Lecture.objects.filter(related_course__start_time__year=datetime.now().year)


def lectures_popular_than_avg():
    lecs_with_views = Lecture.objects.annotate(stud_cnt=Count('related_course__student'))

    return lecs_with_views.filter(stud_cnt__gt=lecs_with_views.aggregate(avg=Avg('stud_cnt'))['avg'])
    


def students_year_avg_by_courses():
    return list(zip(
        Course.objects.all(),
        [year[0] for year in Course.objects.annotate(stud_year_avg=Avg('student__birthday__year')).values_list('stud_year_avg')]
    ))
    
    
def mails_students_notviewed_unpopular_lecture():
    most_unpop_lec = Lecture.objects.select_related('related_course').annotate(stud_cnt=Count('related_course__student')).order_by('stud_cnt').first()
    mails = [
        mail[0] for mail in most_unpop_lec.related_course.student_set.values_list('email')
    ]

    return mails


def cnt_lectures_with_viewers_gt_than_two():
    return len(Lecture.objects.annotate(stud_cnt=Count('related_course__student')).filter(stud_cnt__gt=2))
