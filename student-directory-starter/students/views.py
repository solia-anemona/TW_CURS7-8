from django.http import JsonResponse
from django.views.decorators.http import require_GET

STUDENTS = [
    {"id": 1, "name": "Ana Popescu", "year": 3},
    {"id": 2, "name": "Radu Ionescu", "year": 3},
]


@require_GET
def student_list(request):
    return JsonResponse({"items": STUDENTS})


def student_detail(request, student_id):
    for student in STUDENTS:
        if student["id"] == student_id:
            return JsonResponse(student)
    return JsonResponse({"detail": "Student inexistent"}, status=404)


def health(request):
    return JsonResponse({"status": "ok"})