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
                name: gettext("通天塔"),
                placeholder: gettext("可为空"),
                hookable: true
            },
        },
    ]
})();