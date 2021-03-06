#coding=utf-8

from admin import alive, AdminCtrl
import re

class Admin_CacheCtrl(AdminCtrl):
    @alive
    def get(self):
        self.render('admin/cache.html')

class Admin_CacheDeleteCtrl(AdminCtrl):
    @alive
    def get(self):
        self.post()

    @alive
    def post(self):
        try:
            self.cache().delete(self.input('exp'), exp = True)
            self.flash(1)
        except:
            self.flash(0)
