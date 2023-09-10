from django.db import models
from django.contrib.auth.models import User



class Author(models.Model):
    name = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    is_subscriber = models.BooleanField(
        verbose_name='Подписчик',
        default=False
    )

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f'{self.name.username}'


class Post(models.Model):
    author = models.ForeignKey(
        'Author',
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    title = models.CharField(
        max_length=128,
        verbose_name='Заголовок'
    )
    content = models.TextField(
        verbose_name='Объявление'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        verbose_name='Категория'
    )
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    video = models.FileField(upload_to='video/', null=True, blank=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'posts/{self.pk}'


class Category(models.Model):
    categories = [('tank', 'Танки'),
                  ('healer', 'Хилы'),
                  ('dd', 'ДД'),
                  ('trader', 'Торговцы'),
                  ('master', 'Гилдмастеры'),
                  ('quest', 'Квестгиверы'),
                  ('smith', 'Кузнецы'),
                  ('skinner', 'Кожевники'),
                  ('potion', 'Зельевары'),
                  ('caster', 'Мастера заклинаний'),
                  ]

    name = models.CharField(
        max_length=8,
        choices=categories,
        verbose_name='Категория',
        default='tank',
        unique=True
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.get_name_display()


class Reply(models.Model):
    author = models.ForeignKey(
        'Author',
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        verbose_name='Объявление'
    )
    content = models.TextField(verbose_name='Отклик')
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'

    def __str__(self):
        return f'{self.content[0:32]}'


class UserProfile(models.Model):
    user = models.OneToOneField(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'