# -*- coding: utf-8 -*-

############################################################################
##
## Copyright (C) 2019 Luxoft Sweden AB
## Contact: https://www.qt.io/licensing/
##
## This file is part of the Neptune 3 UI.
##
## $QT_BEGIN_LICENSE:GPL-QTAS$
## Commercial License Usage
## Licensees holding valid commercial Qt Automotive Suite licenses may use
## this file in accordance with the commercial license agreement provided
## with the Software or, alternatively, in accordance with the terms
## contained in a written agreement between you and The Qt Company.  For
## licensing terms and conditions see https://www.qt.io/terms-conditions.
## For further information use the contact form at https://www.qt.io/contact-us.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 3 or (at your option) any later version
## approved by the KDE Free Qt Foundation. The licenses are as published by
## the Free Software Foundation and appearing in the file LICENSE.GPL3
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
## SPDX-License-Identifier: GPL-3.0
##
############################################################################

# squish dependent
import names
import common.app as app
import common.qml_names as qml
import __builtin__


# all variable ui elements in a single dict, though qml_names definitions
# look a bit useless now
variable_calendar_ui = {
        'events': {'button': names.events_ToolButton,
                   'view': qml.calendar_view['events']},
        'year': {'button': names.year_ToolButton,
                 'view': qml.calendar_view['year']},
        'next': {'button': names.next_ToolButton,
                 'view': qml.calendar_view['next']}
}

top_buttons_calendar_ui = {
        'previous': names.topCalendarMonthlyViewPreviousButton,
        'next':  names.topCalendarMonthlyViewNextButton
}


@OnFeatureStart
def hook(context):
    start_neptune_ui_app_w_focus("console")


@Given("tap '|word|' button")
def step(context, view_name):
    if view_name not in variable_calendar_ui.keys():
        app.fail("in calendar, this view button '"
                 + view_name
                 + "' is not known!")
        return

    view_object_name = variable_calendar_ui[view_name]['button']
    app.switch_to_app('calendar')
    squish.snooze(0.25)

    events_button = waitForObject(view_object_name)
    tapObject(events_button)


@Then("calendar view '|word|' should be displayed")
def step(context, view_name):
    if view_name not in variable_calendar_ui.keys():
        app.fail("in calendar, this view '"
                 + view_name
                 + "' is not known!")
        return

    compare_name = variable_calendar_ui[view_name]['view']

    app.switch_to_app('calendar')
    squish.snooze(0.25)

    view_stack_layout = squish.waitForObject(names.calendarViewContent)
    current_index = view_stack_layout.currentIndex
    stack_layouts = object.children(view_stack_layout)
    current_name = stack_layouts[current_index].objectName
    test.compare(current_name, compare_name, "calendar views")


@When("store current month viewed")
def step(context):
    if not context.userData:
        context.userData = {}

    app.switch_to_app('calendar')
    squish.snooze(0.25)

    grid_for_info = squish.waitForObject(names.topCalendarGrid)
    current_month = __builtin__.int(str(grid_for_info.month))
    context.userData['month'] = current_month


@Then("tap on '|word|' button in monthly view")
def step(context, button_name):
    if not context.userData:
        context.userData = {}

    if button_name not in top_buttons_calendar_ui.keys():
        app.fail("in calendar, the button '"
                 + button_name
                 + "' is not known!")
        return
    button = top_buttons_calendar_ui[button_name]
    month_delta = 1 if (top_buttons_calendar_ui.keys()[0]
                     == button_name) else -1

    app.switch_to_app('calendar')
    squish.snooze(0.25)

    squish.tapObject(button)

    squish.snooze(0.5)
    grid_for_info = squish.waitForObject(names.topCalendarGrid)

    month_now = __builtin__.int(str(grid_for_info.month))
    month_before = context.userData['month']

    month_change = (month_before + month_delta) % 12
    app.compare(str(month_change + 1), str(month_now + 1), " month changes")
