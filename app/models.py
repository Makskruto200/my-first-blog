from django.db import models


class Apps(models.Model):
    name = models.CharField("Название", max_length=50)
    author = models.CharField("Автор", max_length=50)
    text = models.TextField("Описание")
    file = models.FileField("Фаил")
    date = models.DateTimeField("Дата публикации", auto_now_add=True)
    img = models.ImageField("Иконка", upload_to='images')
    video = models.FileField("Видео")
    Editor_Choice = models.BooleanField("Выбор редакции", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Приложение'
        verbose_name_plural = 'Приложения'


class Comment(models.Model):
    app = models.ForeignKey(Apps, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.app)


class Applications(models.Model):
    name = models.CharField("Название", max_length=50)
    author = models.CharField("Автор", max_length=50)
    text = models.TextField("Описание")
    file = models.FileField("Фаил")
    date = models.DateTimeField("Дата публикации", auto_now_add=True)
    img = models.ImageField("Иконка", upload_to='images')
    video = models.FileField("Видео")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
