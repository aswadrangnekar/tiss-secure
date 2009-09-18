#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configuration as config
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from utils import render_template, dec

class IndexHandler(webapp.RequestHandler):
    def get(self):
        response = render_template('index.html')
        self.response.out.write(response)

class RecruitersPage(webapp.RequestHandler):
    def get(self):
        response = render_template('recruiters.html')
        self.response.out.write(response)
        
class ContactUsPage(webapp.RequestHandler):
    def get(self):
        response = render_template('contact_us.html')
        self.response.out.write(response)

class AlumniPage(webapp.RequestHandler):
    def get(self):
        response = render_template('achievements.html')
        self.response.out.write(response)

class IndrelPage(webapp.RequestHandler):
    def get(self):
        response = render_template('indrel.html')
        self.response.out.write(response)

class TrndevPage(webapp.RequestHandler):
    def get(self):
        response = render_template('trndev.html')
        self.response.out.write(response)
        
class CombenPage(webapp.RequestHandler):
    def get(self):
        response = render_template('comben.html')
        self.response.out.write(response)

class HipmsPage(webapp.RequestHandler):
    def get(self):
        response = render_template('hipms.html')
        self.response.out.write(response)
        
class OddevPage(webapp.RequestHandler):
    def get(self):
        response = render_template('oddev.html')
        self.response.out.write(response)
urls = (
    ('/', IndexHandler),
    ('/placements/recruiters/?', RecruitersPage),
    ('/contactus/?', ContactUsPage),
    
    ('/alumni/achievements/?', AlumniPage),
    ('/forum/indrel/?', IndrelPage),
    ('/forum/trndev/?', TrndevPage),
    ('/forum/comben/?', CombenPage),
    ('/forum/hipms/?', HipmsPage),
    ('/forum/oddev/?', OddevPage)
)

application = webapp.WSGIApplication(urls, debug=config.DEBUG)


def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()

