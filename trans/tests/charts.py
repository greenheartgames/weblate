# -*- coding: utf-8 -*-
#
# Copyright © 2012 - 2013 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <http://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

"""
Tests for charts and widgets.
"""

from trans.tests.views import ViewTestCase
from trans.views.widgets import WIDGETS
from django.core.urlresolvers import reverse


class ChartsTest(ViewTestCase):
    '''
    Testing of charts.
    '''
    def test_activity_html(self):
        '''
        Test of html for activity charts.
        '''
        response = self.client.get(
            reverse('view_activity')
        )
        self.assertContains(response, 'img src="/activity')

        response = self.client.get(
            reverse('view_activity_project', kwargs=self.kw_project)
        )
        self.assertContains(response, 'img src="/activity')

        response = self.client.get(
            reverse('view_activity_subproject', kwargs=self.kw_subproject)
        )
        self.assertContains(response, 'img src="/activity')

        response = self.client.get(
            reverse('view_activity_translation', kwargs=self.kw_translation)
        )
        self.assertContains(response, 'img src="/activity')

        response = self.client.get(
            reverse('view_language_activity', kwargs={'lang': 'cs'})
        )
        self.assertContains(response, 'img src="/activity')

    def test_activity_monthly(self):
        '''
        Test of monthly activity charts.
        '''
        response = self.client.get(
            reverse('monthly_activity')
        )
        self.assertContains(response, 'PNG')

        response = self.client.get(
            reverse('monthly_activity_project', kwargs=self.kw_project)
        )
        self.assertContains(response, 'PNG')

        response = self.client.get(
            reverse('monthly_activity_subproject', kwargs=self.kw_subproject)
        )
        self.assertContains(response, 'PNG')

        response = self.client.get(
            reverse('monthly_activity_translation', kwargs=self.kw_translation)
        )
        self.assertContains(response, 'PNG')

        response = self.client.get(
            reverse('monthly_language_activity', kwargs={'lang': 'cs'})
        )
        self.assertContains(response, 'PNG')

        response = self.client.get(
            reverse(
                'monthly_user_activity',
                kwargs={'user': self.user.username}
            )
        )
        self.assertContains(response, 'PNG')

    def test_activity_yearly(self):
        '''
        Test of yearly activity charts.
        '''
        response = self.client.get(
            reverse('yearly_activity')
        )
        self.assertContains(response, 'PNG')

        response = self.client.get(
            reverse('yearly_activity_project', kwargs=self.kw_project)
        )
        self.assertContains(response, 'PNG')

        response = self.client.get(
            reverse('yearly_activity_subproject', kwargs=self.kw_subproject)
        )
        self.assertContains(response, 'PNG')

        response = self.client.get(
            reverse('yearly_activity_translation', kwargs=self.kw_translation)
        )
        self.assertContains(response, 'PNG')

        response = self.client.get(
            reverse('yearly_language_activity', kwargs={'lang': 'cs'})
        )
        self.assertContains(response, 'PNG')

        response = self.client.get(
            reverse(
                'yearly_user_activity',
                kwargs={'user': self.user.username}
            )
        )
        self.assertContains(response, 'PNG')


class WidgetsTest(ViewTestCase):
    '''
    Testing of widgets.
    '''
    def test_view_widgets_root(self):
        response = self.client.get(
            reverse('widgets_root')
        )
        self.assertContains(response, 'Test')

    def test_view_widgets(self):
        response = self.client.get(
            reverse('widgets', kwargs=self.kw_project)
        )
        self.assertContains(response, 'Test')

    def test_view_widgets_lang(self):
        response = self.client.get(
            reverse('widgets', kwargs=self.kw_project),
            lang='cs'
        )
        self.assertContains(response, 'Test')

    def test_view_engage(self):
        response = self.client.get(
            reverse('engage', kwargs=self.kw_project)
        )
        self.assertContains(response, 'Test')

    def test_view_engage_lang(self):
        response = self.client.get(
            reverse('engage-lang', kwargs=self.kw_lang_project)
        )
        self.assertContains(response, 'Test')

    def test_view_widget_image(self):
        for widget in WIDGETS:
            for color in WIDGETS[widget]['colors']:
                response = self.client.get(
                    reverse(
                        'widget-image',
                        kwargs={
                            'project': self.project.slug,
                            'widget': widget,
                            'color': color,
                        }
                    )
                )
                # This is pretty stupid test for PNG image
                self.assertContains(response, 'PNG')

    def test_view_widget_image_lang(self):
        for widget in WIDGETS:
            for color in WIDGETS[widget]['colors']:
                response = self.client.get(
                    reverse(
                        'widget-image-lang',
                        kwargs={
                            'project': self.project.slug,
                            'widget': widget,
                            'color': color,
                            'lang': 'cs',
                        }
                    )
                )
                # This is pretty stupid test for PNG image
                self.assertContains(response, 'PNG')
