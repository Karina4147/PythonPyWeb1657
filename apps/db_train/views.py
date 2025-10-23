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
        self.answer4 = Author.objects.filter(gender='ж').count()
        self.answer5 = None  # TODO Какой процент авторов согласился с правилами при регистрации?
        self.answer6 = AuthorProfile.objects.filter(stage__range=(1, 5))
        self.answer7 = Author.objects.aggregate(max_age=Max('age'))  # TODO Какой автор имеет наибольший возраст?
        self.answer8 = Author.objects.filter(phone_number=True).count()  # TODO Сколько авторов указали свой номер телефона?
        self.answer9 = Author.objects.filter(age__lt=25)  # TODO Какие авторы имеют возраст младше 25 лет?
        self.answer10 = Author.objects.annotate(entries_count=Count('entries')).values('username', 'entries_count')  # TODO Сколько статей написано каждым автором?

        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1, 11)}

        return render(request, 'train_db/training_db.html', context=context)

