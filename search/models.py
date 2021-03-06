from __future__ import unicode_literals

from django.db import models


class Board(models.Model):
    board_name = models.CharField(max_length=250)
    like = models.BooleanField(default=False)
    board_icon = models.FileField(default="none")

    def __str__(self):
        return self.board_name


class Response(models.Model):
    response_text = models.CharField(max_length=1000, default='default')
    like = models.BooleanField(default=False)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    image = models.FileField(default="none")

    def __str__(self):
        return self.response_text


class Phrase(models.Model):
    phrase_title = models.CharField(max_length=250)
    phrase_votes = models.IntegerField(default=0)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    response = models.OneToOneField(Response, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.phrase_title


class Tag(models.Model):
    tag_name = models.CharField(max_length=250)
    like = models.BooleanField(default=False)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag_name


