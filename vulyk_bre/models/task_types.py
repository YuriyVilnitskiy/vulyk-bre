# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from vulyk.models.task_types import AbstractTaskType

from vulyk_bre.models.tasks import (
    BreAnswer, BreTask)


class BreTaskType(AbstractTaskType):
    """
    Names Task to work with Vulyk.
    """

    answer_model = BreAnswer
    task_model = BreTask

    name = "Аналіз імен та зв'язків між ними"
    description = ''

    template = 'base.html'
    helptext_template = 'help.html'
    type_name = 'bre_task'

    redundancy = 1

    JS_ASSETS = ['static/scripts/handlebars.js',
                 'static/scripts/jquery.serializejson.js',
                 'static/scripts/base.js', ]

    CSS_ASSETS = ['static/styles/bootstrap-social.css',
                  'static/styles/base.css', ]
