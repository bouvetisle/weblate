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

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission, User
import json


class Command(BaseCommand):
    help = 'imports users from JSON dump of database'

    def handle(self, *args, **options):
        '''
        Creates default set of groups and optionally updates them and moves
        users around to default group.
        '''
        if len(args) != 1:
            raise CommandError('Please specify JSON file to import!')

        data = json.load(open(args[0]))

        for line in data:
            if User.objects.filter(username=line['username']).exists():
                print 'Skipping %s' % line['username']
                continue
            User.objects.create(
                username=line['username'],
                first_name=line['first_name'],
                last_name=line['last_name'],
                password=line['password'],
                email=line['email']
            )
