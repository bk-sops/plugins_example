# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from pipeline.conf import settings
from pipeline.core.flow.activity import Service, StaticIntervalGenerator
from pipeline.component_framework.component import Component

__group_name__ = _(u"自定义插件(CUS)")


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
    embedded_form = True
    form = """
(function(){
    $.atoms.pause1_node = [
        {
            tag_code: "test_radio",
            type: "radio",
            attrs: {
                name: gettext("测试RADIO"),
                items: [
                    {value: "1", name: "选项1"},
                    {value: "2", name: "选项2"},
                    {value: "3", name: "选项3"},
                ],
                default: "2",
                hookable: true,
                validation: [
                    {
                        type: "required"
                    }
                ]
            }
        },
        {
            tag_code: "test_testarea",
            type: "textarea",
            attrs: {
                name: gettext("测试文本框"),
                placeholder: gettext("提示"),
                hookable: true,
                validation: [
                    {
                        type: "required"
                    }
                ],
                default: "2",
            }
        },
        {
            tag_code: "test_input",
            type: "input",
            attrs: {
                name: gettext("测试输入框"),
                placeholder: gettext("可为空"),
                hookable: true
            },
        },
    ]
})();
"""

