from django.shortcuts import render
from django.core.cache import cache
from . import terms_work


def index(request):
    return render(request, "index.html")


def terms_list(request):
    terms = terms_work.get_terms_for_table()
    return render(request, "term_list.html", context={"terms": terms})

def lesson_list(request):
    lessons = terms_work.get_lesson_for_table()
    return render(request, "lesson_list.html", context={"terms": lessons})


def add_term(request):
    return render(request, "term_add.html")

def add_lesson(request):
    return render(request, "lesson_add.html")


def send_term(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_term = request.POST.get("new_term", "")
        new_definition = request.POST.get("new_definition", "").replace(";", ",")
        context = {"user": user_name}
        if len(new_definition) == 0:
            context["success"] = False
            context["comment"] = "Описание должно быть не пустым"
        elif len(new_term) == 0:
            context["success"] = False
            context["comment"] = "Термин должен быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Ваш термин принят"
            terms_work.write_term(new_term, new_definition)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "term_request.html", context)
    else:
        add_term(request)

def send_lesson(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_term = request.POST.get("new_term", "")
        new_definition = request.POST.get("new_definition", "").replace(";", ",")
        context = {"user": user_name}
        if len(new_definition) == 0:
            context["success"] = False
            context["comment"] = "Тема урока должна быть обозначена"
        elif len(new_term) == 0:
            context["success"] = False
            context["comment"] = "Дата урока должна быть назначена"
        else:
            context["success"] = True
            context["comment"] = "Отметьте занятие у себя в календаре"
            terms_work.write_lesson(new_term, new_definition)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "lesson_request.html", context)
    else:
        add_term(request)


def show_stats(request):
    stats = terms_work.get_terms_stats()
    return render(request, "stats.html", stats)
