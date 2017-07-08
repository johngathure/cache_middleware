# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid

# Create your models here.


class Todo(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    task = models.CharField(max_length=100)
    is_complete = models.BooleanField(default=False)

    def __unicode__(self):
        return "Task %s is complete %s" % (self.task, self.is_complete)

    def as_dict(self):
        return {
            "id": self._id,
            "task": self.task,
            "is_complete": self.is_complete
        }
