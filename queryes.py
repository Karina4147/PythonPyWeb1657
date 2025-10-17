import django
import os
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train_alternative.models import Blog, Author, AuthorProfile, Entry, Tag

    obj = Entry.objects.filter(author__name__contains='author')
    print(obj)

    obj = Entry.objects.filter(author__authorprofile__city=None)
    print(obj)

    print(Entry.objects.get(id__exact=4))
    print(Entry.objects.get(id=4))  # Аналогично exact
    print(Blog.objects.get(name__iexact="Путешествия по миру"))

    print(Entry.objects.filter(headline__contains='мод'))

    print(Entry.objects.filter(id__in=[1, 3, 4]))


    print(Entry.objects.filter(number_of_comments__in='123'))  # число комментариев 1 или 2 или 3
    inner_qs = Blog.objects.filter(name__contains='Путешествия')
    entries = Entry.objects.filter(blog__in=inner_qs)
    print(entries)

    print(Entry.objects.filter(number_of_comments__gt=10))


    print(Entry.objects.filter(pub_date__gte=datetime.date(2023, 6, 1)))
    print(Entry.objects.filter(number_of_comments__gt=10).filter(rating__lt=4))
    print(Entry.objects.filter(headline__lte="Зя"))

    print(Entry.objects.filter(headline__startswith='Как'))
    # <QuerySet [<Entry: Как правильно заниматься йогой>, <Entry: Как создать стильный образ на каждый день>]>
    print(Entry.objects.filter(headline__endswith='ния'))
    # <QuerySet [<Entry: Топ-10 фитнес-тренеров для вдохновения>, <Entry: Секреты успешного похудения>]>

    # obj = Entry.objects.filter(author__name__contains='author')
    # print(obj)













