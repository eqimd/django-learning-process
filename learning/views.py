from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

from learning.logic.analytics import (
    count_students_listened_lectures,
    count_lectures_views,
    lectures_in_current_year,
    lectures_popular_than_avg,
    students_year_avg_by_courses,
    mails_students_notviewed_unpopular_lecture,
    cnt_lectures_with_viewers_gt_than_two,
)

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    """
    Main (or index) view.

    Returns rendered default page to the user.
    Typed with the help of ``django-stubs`` project.
    """

    return render(
        request,
        'learning/index.html',
        {
            'students_lectures_counts': count_students_listened_lectures(),
            'most_popular_lectures': {
                'number': 3,
                'lectures': count_lectures_views()[:3],
            },
            'most_unpopular_lectures': {
                'number': 3,
                'lectures': count_lectures_views()[-1:-4:-1],
            },
            'lectures_in_current_year': lectures_in_current_year(),
            'lectures_popular_than_avg': lectures_popular_than_avg(),
            'students_year_avg_by_courses': students_year_avg_by_courses(),
            'mails_students_notviewed_unpopular_lecture': mails_students_notviewed_unpopular_lecture(),
            'cnt_lectures_with_viewers_gt_than_two': cnt_lectures_with_viewers_gt_than_two(),
        }
    )