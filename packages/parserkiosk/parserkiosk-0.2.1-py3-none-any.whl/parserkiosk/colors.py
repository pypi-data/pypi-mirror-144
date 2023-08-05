''''
Copyright (C) 2022 Aarnav Bos

This program is free software: you can redistribute it and/or modify

it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
CRED = '\033[91m'
CEND = '\033[0m'
CGREEN = '\033[32m'


def print_error(text):
    print(f'{CRED}{text}{CEND}')


def print_success(text):
    print(f'{CGREEN}{text}{CEND}')
