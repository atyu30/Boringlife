#!/usr/bin/env python
# encoding: utf-8

# author: Atyu30 <ipostfix (at) gmail.com>
# description: 
#

import getpass

import os
import time

import ConfigParser

class Browser():

    def __init__(self):
        self.home = os.path.expanduser('~')

    def check_path(self,path):
        if not os.path.exists(path) :
            print 'No such file', path
            path = None
        return path

    def check_file(self,bookmark):
        if not os.path.isfile(bookmark) :
            print 'Favorite not found', bookmark
            bookmark = None
        return bookmark

    def firefox_check(self):
        firefox_path = self.home + os.sep + ".mozilla/firefox/"
        firefox_path = self.check_path(firefox_path)
        if firefox_path == None:
            print 'Firefox No such file', firefox_path
            firefox_bookmark = None
            return firefox_bookmark
        else:
            firefox_home_config = firefox_path + "profiles.ini"
            config = ConfigParser.ConfigParser()
            config.readfp(open(firefox_home_config))
            firefox_home = config.get("Profile0","Path")
            firefox_bookmark = firefox_path + firefox_home + os.sep + "places.sqlite"
            firefox_bookmark = self.check_file(firefox_bookmark)
            if firefox_bookmark == None:
                print 'Firefox favorite not found', firefox_bookmark
                firefox_bookmark = None

            return firefox_bookmark

        def backup_bookmark(self):
            firefox_bookmark = self.firefox_check()
            source = []
            if firefox_bookmark == None:
                print 'Backup FAILED'
            else:
                source.append(firefox_bookmark)

                target_dir = '/opt/backup/favorite/'

                today = target_dir + time.strftime('%Y%m%d')
                now = time.strftime('%H%M%S')
                if not os.path.exists(target_dir) :
                    os.makedirs(target_dir)
                    print 'Successfully created directory', target_dir

                if not os.path.exists(today) :
                    os.mkdir(today)
                    print 'Successfully created directory', today

                target = today + os.sep + now + '.zip'

                zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

                if os.system(zip_command) == 0 :
                    print 'Sucessful backup to', target
                else:
                    print 'Backup FAILED'


if __name__ == '__main__':
    b = Browser()
    b.backup_bookmark()
