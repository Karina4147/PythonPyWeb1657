from django.shortcuts import render
from django.views import View
from .models import Author, AuthorProfile, Entry, Tag
from django.db.models import Q, Max, Min, Avg, Count


class TrainView(View):
    def get(self, request):
        max_self_esteem = Author.objects.aggregate(max_self_esteem=Max('self_esteem'))
        self.answer1 = Author.objects.filter(self_esteem=max_self_esteem['max_self_esteem'])
        results = Entry.objects.raw(
            """
            Select id, author_id, Count(*) as articl_count
            from db_train_alternative_entry
            Group by author_id
            Order by articl_count DESC
            Limit 1;
            """
        )
        self.answer2 = results  # TODO Какой автор имеет наибольшее количество опубликованных статей?
        entries = Entry.objects.filter(Q(tags__name="Кино") | Q(tags__name="Музыка"))
        self.answer3 = entries  # TODO Какие статьи содержат тег 'Кино' или 'Музыка' ?
        count_author = Author.objects.count
        self.answer4 = count_author  # TODO Сколько авторов женского пола зарегистрировано в системе?
        self.answer5 = None  # TODO Какой процент авторов согласился с правилами при регистрации?
        self.answer6 = AuthorProfile.objects.filter(stage__range=(1, 5))  # TODO Какие авторы имеют стаж от 1 до 5 лет?
        max_age = Author.objects.aggregate(max_age=Max('age'))
        self.answer7 = max_age  # TODO Какой автор имеет наибольший возраст?
        self.answer8 = None  # TODO Сколько авторов указали свой номер телефона?
        self.answer9 = Author.objects.filter(age__lt=25)  # TODO Какие авторы имеют возраст младше 25 лет?
        self.answer10 = None  # TODO Сколько статей написано каждым автором?

        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1, 11)}

        return render(request, 'train_db/training_db.html', context=context)

