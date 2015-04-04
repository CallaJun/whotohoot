#!/usr/bin/env python
import jinja2
import logging
import os
import webapp2
import hootdata
import urllib2

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class HomeHandler(webapp2.RequestHandler):
    def get(self):
    	template_values = {
            'name' : '',
            'dorm' : '',
            'floor' : ''
        }

        template = jinja_environment.get_template('views/home.html')
        self.response.out.write(template.render(template_values))

class HootHandler(webapp2.RequestHandler):
  def get(self):  
    template_values = {'dorm' : self.request.get('dorm'),
                    	'floor' : self.request.get('floor'),
                    }

    #name
    if self.request.get('name')=='':
        template_values['name'] = 'Mawrter'
    else:
        template_values['name'] = self.request.get('name')
    
    template = jinja_environment.get_template('views/home.html')
    self.response.out.write(template.render(template_values))

routes = [('/', HomeHandler),('/hoot', HootHandler)]
app = webapp2.WSGIApplication(routes, debug=True) 