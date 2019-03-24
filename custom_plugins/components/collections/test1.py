# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from pipeline.conf import settings
from pipeline.core.flow.activity import Service, StaticIntervalGenerator
from pipeline.component_framework.component import Component

__group_name__ = _(u"自定义原子(CUS)")


class Pause1Service(Service):
    __need_schedule__ = False

    def execute(self, data, parent_data):
        test_input = data.get_one_of_inputs('test_input')
        test_testarea = data.get_one_of_inputs('test_testarea')
        test_radio = data.get_one_of_inputs('test_radio')

        if int(test_input) + int(test_testarea) + int(test_radio) == 10:
            return True
        else:
            return False

    # def schedule(self, data, parent_data, callback_data=None):
    #     return True

    def outputs_format(self):
        return []


class Pause1Component(Component):
    name = _(u'测试1')
    code = 'pause1_node'
    bound_service = Pause1Service
    form = settings.STATIC_URL + 'custom_plugins/test/test_pause1.js'

