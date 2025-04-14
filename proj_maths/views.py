from django.shortcuts import render
from django.views.generic import ListView
from django.core.cache import cache
from trainer.models import Animal, AnimalClass
from . import terms_work


class AnimalListView(ListView):
    model = Animal
    template_name = "animal_list.html"
    context_object_name = "animals"


def index(request):
    return render(request, "index.html")


def terms_list(request):
    terms = terms_work.get_terms_for_table()
    return render(request, "term_list.html", context={"terms": terms})


def add_term(request):
    return render(request, "term_add.html")


def send_term(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_term = request.POST.get("new_term", "")
        new_definition = request.POST.get("new_definition", "").replace(";", ",")
        context = {"user": user_name}

        if not new_definition:
            context["success"] = False
            context["comment"] = "Описание должно быть не пустым"
        elif not new_term:
            context["success"] = False
            context["comment"] = "Термин должен быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Ваш термин принят"
            terms_work.write_term(new_term, new_definition)

        if context.get("success"):
            context["success-title"] = ""

        return render(request, "term_request.html", context)

    return add_term(request)


def show_stats(request):
    stats = terms_work.get_terms_stats()
    return render(request, "stats.html", stats)


# 🔥 Новая страница — тест на определение класса животного
def test_view(request):
    animals = Animal.objects.all()[:5]
    animal_classes = AnimalClass.objects.all()
    results = {}

    if request.method == "POST":
        for animal in animals:
            user_class_id = request.POST.get(f'class_{animal.id}')
            if user_class_id:
                correct = str(animal.animal_class.id) == user_class_id
                results[animal.id] = correct

    return render(request, "test.html", {
        "animals": animals,
        "animal_classes": animal_classes,
        "results": results if request.method == "POST" else None
    })
