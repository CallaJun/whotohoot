#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import jinja2
import logging
import os
import webapp2
import hootdata

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class HomeHandler(webapp2.RequestHandler):
    def get(self):
    	template_values = {
        }
        template = jinja_environment.get_template('views/home.html')
        self.response.out.write(template.render(template_values))

class HootHandler(webapp2.RequestHandler):
  def get(self):  
    template_values = {'name' : self.request.get('name'),
    					'dorm' : self.request.get('dorm'),
                    	'floor' : self.request.get('floor'),
                       }

    #BRECON FIRST
    if self.request.get('dorm')=='Brecon' and self.request.get('floor')=='1':
        template_values['halladvisor'] = hootdata.BRECON_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.BRECON_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.BRECON_HA[self.request.get('floor')]]
        customspeople = []
        customspeopleemails = []
        customspeoplerooms = []
        peermentors = []
        peermentorsemails = []
        peermentorsrooms = []
        #Custom people
        for person in range(0,len(hootdata.BRECON_C1)):
            customspeople.append(hootdata.BRECON_C1[person])
        template_values['customspeople'] = customspeople
        for person in customspeople:
            customspeopleemails.append(hootdata.EMAILS[person])
        template_values['customspeopleemails'] = customspeopleemails
        for person in customspeople:
            customspeoplerooms.append(hootdata.ROOMS[person])
        template_values['customspeoplerooms'] = customspeoplerooms
        #Peer mentors
        for person in range(0,len(hootdata.BRECON_PM)):
            peermentors.append(hootdata.BRECON_PM[person])
        template_values['peermentors'] = peermentors
        for person in peermentors:
            peermentorsemails.append(hootdata.EMAILS[person])
        template_values['peermentorsemails'] = peermentorsemails
        for person in peermentors:
            peermentorsrooms.append(hootdata.ROOMS[person])

    #BRECON SECOND
    elif self.request.get('dorm')=='Brecon' and self.request.get('floor')=='2':
        template_values['halladvisor'] = hootdata.BRECON_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.BRECON_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.BRECON_HA[self.request.get('floor')]]
        customspeople = []
        customspeopleemails = []
        customspeoplerooms = []
        peermentors = []
        peermentorsemails = []
        peermentorsrooms = []
        #Custom people
        for person in range(0,len(hootdata.BRECON_C2)):
            customspeople.append(hootdata.BRECON_C2[person])
        template_values['customspeople'] = customspeople
        for person in customspeople:
            customspeopleemails.append(hootdata.EMAILS[person])
        template_values['customspeopleemails'] = customspeopleemails
        for person in customspeople:
            customspeoplerooms.append(hootdata.ROOMS[person])
        template_values['customspeoplerooms'] = customspeoplerooms
        #Peer mentors
        for person in range(0,len(hootdata.BRECON_PM)):
            peermentors.append(hootdata.BRECON_PM[person])
        template_values['peermentors'] = peermentors
        for person in peermentors:
            peermentorsemails.append(hootdata.EMAILS[person])
        template_values['peermentorsemails'] = peermentorsemails
        for person in peermentors:
            peermentorsrooms.append(hootdata.ROOMS[person])

    #BRECON THIRD
    elif self.request.get('dorm')=='Brecon' and self.request.get('floor')=='3':
        template_values['halladvisor'] = hootdata.BRECON_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.BRECON_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.BRECON_HA[self.request.get('floor')]]
        customspeople = []
        customspeopleemails = []
        customspeoplerooms = []
        peermentors = []
        peermentorsemails = []
        peermentorsrooms = []
        #Custom people
        for person in range(0,len(hootdata.BRECON_C3)):
            customspeople.append(hootdata.BRECON_C3[person])
        template_values['customspeople'] = customspeople
        for person in customspeople:
            customspeopleemails.append(hootdata.EMAILS[person])
        template_values['customspeopleemails'] = customspeopleemails
        for person in customspeople:
            customspeoplerooms.append(hootdata.ROOMS[person])
        template_values['customspeoplerooms'] = customspeoplerooms
        #Peer mentors
        for person in range(0,len(hootdata.BRECON_PM)):
            peermentors.append(hootdata.BRECON_PM[person])
        template_values['peermentors'] = peermentors
        for person in peermentors:
            peermentorsemails.append(hootdata.EMAILS[person])
        template_values['peermentorsemails'] = peermentorsemails
        for person in peermentors:
            peermentorsrooms.append(hootdata.ROOMS[person])

    #BRECON FOURTH
    elif self.request.get('dorm')=='Brecon' and self.request.get('floor')=='4':
        template_values['halladvisor'] = hootdata.BRECON_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.BRECON_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.BRECON_HA[self.request.get('floor')]]
        customspeople = []
        customspeopleemails = []
        customspeoplerooms = []
        peermentors = []
        peermentorsemails = []
        peermentorsrooms = []
        #Custom people
        for person in range(0,len(hootdata.BRECON_C4)):
            customspeople.append(hootdata.BRECON_C4[person])
        template_values['customspeople'] = customspeople
        for person in customspeople:
            customspeopleemails.append(hootdata.EMAILS[person])
        template_values['customspeopleemails'] = customspeopleemails
        for person in customspeople:
            customspeoplerooms.append(hootdata.ROOMS[person])
        template_values['customspeoplerooms'] = customspeoplerooms
        #Peer mentors
        for person in range(0,len(hootdata.BRECON_PM)):
            peermentors.append(hootdata.BRECON_PM[person])
        template_values['peermentors'] = peermentors
        for person in peermentors:
            peermentorsemails.append(hootdata.EMAILS[person])
        template_values['peermentorsemails'] = peermentorsemails
        for person in peermentors:
            peermentorsrooms.append(hootdata.ROOMS[person])
    
    #DENBIGH FIRST
    elif self.request.get('dorm')=='Denbigh' and self.request.get('floor')=='1':
        template_values['halladvisor'] = hootdata.DENBIGH_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.DENBIGH_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.DENBIGH_HA[self.request.get('floor')]]
        customspeople = []
        customspeopleemails = []
        customspeoplerooms = []
        peermentors = []
        peermentorsemails = []
        peermentorsrooms = []
        #Custom people
        for person in range(0,len(hootdata.DENBIGH_C1)):
            customspeople.append(hootdata.DENBIGH_C1[person])
        template_values['customspeople'] = customspeople
        for person in customspeople:
            customspeopleemails.append(hootdata.EMAILS[person])
        template_values['customspeopleemails'] = customspeopleemails
        for person in customspeople:
            customspeoplerooms.append(hootdata.ROOMS[person])
        template_values['customspeoplerooms'] = customspeoplerooms
        #Peer mentors
        for person in range(0,len(hootdata.DENBIGH_PM)):
            peermentors.append(hootdata.DENBIGH_PM[person])
        template_values['peermentors'] = peermentors
        for person in peermentors:
            peermentorsemails.append(hootdata.EMAILS[person])
        template_values['peermentorsemails'] = peermentorsemails
        for person in peermentors:
            peermentorsrooms.append(hootdata.ROOMS[person])

    #DENBIGH SECOND
    elif self.request.get('dorm')=='Denbigh' and self.request.get('floor')=='2':
        template_values['halladvisor'] = hootdata.DENBIGH_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.DENBIGH_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.DENBIGH_HA[self.request.get('floor')]]
        customspeople = []
        customspeopleemails = []
        customspeoplerooms = []
        peermentors = []
        peermentorsemails = []
        peermentorsrooms = []
        #Custom people
        for person in range(0,len(hootdata.DENBIGH_C2)):
            customspeople.append(hootdata.DENBIGH_C2[person])
        template_values['customspeople'] = customspeople
        for person in customspeople:
            customspeopleemails.append(hootdata.EMAILS[person])
        template_values['customspeopleemails'] = customspeopleemails
        for person in customspeople:
            customspeoplerooms.append(hootdata.ROOMS[person])
        template_values['customspeoplerooms'] = customspeoplerooms
        #Peer mentors
        for person in range(0,len(hootdata.DENBIGH_PM)):
            peermentors.append(hootdata.DENBIGH_PM[person])
        template_values['peermentors'] = peermentors
        for person in peermentors:
            peermentorsemails.append(hootdata.EMAILS[person])
        template_values['peermentorsemails'] = peermentorsemails
        for person in peermentors:
            peermentorsrooms.append(hootdata.ROOMS[person])

    #DENBIGH THIRD
    elif self.request.get('dorm')=='Denbigh' and self.request.get('floor')=='3':
        template_values['halladvisor'] = hootdata.DENBIGH_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.DENBIGH_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.DENBIGH_HA[self.request.get('floor')]]
        customspeople = []
        customspeopleemails = []
        customspeoplerooms = []
        peermentors = []
        peermentorsemails = []
        peermentorsrooms = []
        #Custom people
        for person in range(0,len(hootdata.DENBIGH_C3)):
            customspeople.append(hootdata.DENBIGH_C3[person])
        template_values['customspeople'] = customspeople
        for person in customspeople:
            customspeopleemails.append(hootdata.EMAILS[person])
        template_values['customspeopleemails'] = customspeopleemails
        for person in customspeople:
            customspeoplerooms.append(hootdata.ROOMS[person])
        template_values['customspeoplerooms'] = customspeoplerooms
        #Peer mentors
        for person in range(0,len(hootdata.DENBIGH_PM)):
            peermentors.append(hootdata.DENBIGH_PM[person])
        template_values['peermentors'] = peermentors
        for person in peermentors:
            peermentorsemails.append(hootdata.EMAILS[person])
        template_values['peermentorsemails'] = peermentorsemails
        for person in peermentors:
            peermentorsrooms.append(hootdata.ROOMS[person])

    #PEMEAST FIRST
    elif self.request.get('dorm')=='Pembroke East' and self.request.get('floor')=='1':
        template_values['halladvisor'] = hootdata.PEMEAST_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.PEMEAST_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.PEMEAST_HA[self.request.get('floor')]]
        customspeople = []
        customspeopleemails = []
        customspeoplerooms = []
        peermentors = []
        peermentorsemails = []
        peermentorsrooms = []
        #Custom people
        for person in range(0,len(hootdata.PEMEAST_C1)):
        	customspeople.append(hootdata.PEMEAST_C1[person])
        template_values['customspeople'] = customspeople
        for person in customspeople:
        	customspeopleemails.append(hootdata.EMAILS[person])
        template_values['customspeopleemails'] = customspeopleemails
        for person in customspeople:
        	customspeoplerooms.append(hootdata.ROOMS[person])
        template_values['customspeoplerooms'] = customspeoplerooms
        #Peer mentors
        for person in range(0,len(hootdata.PEMEAST_PM)):
        	peermentors.append(hootdata.PEMEAST_PM[person])
        template_values['peermentors'] = peermentors
        for person in peermentors:
        	peermentorsemails.append(hootdata.EMAILS[person])
        template_values['peermentorsemails'] = peermentorsemails
        for person in peermentors:
        	peermentorsrooms.append(hootdata.ROOMS[person])

    #PEMEAST SECOND
    elif self.request.get('dorm')=='Pembroke East' and self.request.get('floor')=='2':
        template_values['halladvisor'] = hootdata.PEMEAST_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.PEMEAST_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.PEMEAST_HA[self.request.get('floor')]]
        customspeople = []
        customspeopleemails = []
        customspeoplerooms = []
        peermentors = []
        peermentorsemails = []
        peermentorsrooms = []
        #Custom people
        for person in range(0,len(hootdata.PEMEAST_C2)):
        	customspeople.append(hootdata.PEMEAST_C2[person])
        template_values['customspeople'] = customspeople
        for person in customspeople:
        	customspeopleemails.append(hootdata.EMAILS[person])
        template_values['customspeopleemails'] = customspeopleemails
        for person in customspeople:
        	customspeoplerooms.append(hootdata.ROOMS[person])
        template_values['customspeoplerooms'] = customspeoplerooms
        #Peer mentors
        for person in range(0,len(hootdata.PEMEAST_PM)):
        	peermentors.append(hootdata.PEMEAST_PM[person])
        template_values['peermentors'] = peermentors
        for person in peermentors:
        	peermentorsemails.append(hootdata.EMAILS[person])
        template_values['peermentorsemails'] = peermentorsemails
        for person in peermentors:
        	peermentorsrooms.append(hootdata.ROOMS[person])

    #PEMEAST THIRD    	
    elif self.request.get('dorm')=='Pembroke East' and self.request.get('floor')=='3':
        template_values['halladvisor'] = hootdata.PEMEAST_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.PEMEAST_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.PEMEAST_HA[self.request.get('floor')]]
        customspeople = []
        customspeopleemails = []
        customspeoplerooms = []
        peermentors = []
        peermentorsemails = []
        peermentorsrooms = []
        #Custom people
        for person in range(0,len(hootdata.PEMEAST_C3)):
        	customspeople.append(hootdata.PEMEAST_C3[person])
        template_values['customspeople'] = customspeople
        for person in customspeople:
        	customspeopleemails.append(hootdata.EMAILS[person])
        template_values['customspeopleemails'] = customspeopleemails
        for person in customspeople:
        	customspeoplerooms.append(hootdata.ROOMS[person])
        template_values['customspeoplerooms'] = customspeoplerooms
        #Peer mentors
        for person in range(0,len(hootdata.PEMEAST_PM)):
        	peermentors.append(hootdata.PEMEAST_PM[person])
        template_values['peermentors'] = peermentors
        for person in peermentors:
        	peermentorsemails.append(hootdata.EMAILS[person])
        template_values['peermentorsemails'] = peermentorsemails
        for person in peermentors:
        	peermentorsrooms.append(hootdata.ROOMS[person])

    #PEMWEST FIRST
    elif self.request.get('dorm')=='Pembroke West' and self.request.get('floor')=='1':
        template_values['halladvisor'] = hootdata.PEMWEST_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.PEMWEST_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.PEMWEST_HA[self.request.get('floor')]]
        customspeople = []
        customspeopleemails = []
        customspeoplerooms = []
        peermentors = []
        peermentorsemails = []
        peermentorsrooms = []
        #Custom people
        for person in range(0,len(hootdata.PEMWEST_C1)):
        	customspeople.append(hootdata.PEMWEST_C1[person])
        template_values['customspeople'] = customspeople
        for person in customspeople:
        	customspeopleemails.append(hootdata.EMAILS[person])
        template_values['customspeopleemails'] = customspeopleemails
        for person in customspeople:
        	customspeoplerooms.append(hootdata.ROOMS[person])
        template_values['customspeoplerooms'] = customspeoplerooms
        #Peer mentors
        for person in range(0,len(hootdata.PEMWEST_PM)):
        	peermentors.append(hootdata.PEMWEST_PM[person])
        template_values['peermentors'] = peermentors
        for person in peermentors:
        	peermentorsemails.append(hootdata.EMAILS[person])
        template_values['peermentorsemails'] = peermentorsemails
        for person in peermentors:
        	peermentorsrooms.append(hootdata.ROOMS[person])

    #PEMWEST SECOND
    elif self.request.get('dorm')=='Pembroke West' and self.request.get('floor')=='2':
        template_values['halladvisor'] = hootdata.PEMWEST_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.PEMWEST_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.PEMWEST_HA[self.request.get('floor')]]
        customspeople = []
        customspeopleemails = []
        customspeoplerooms = []
        peermentors = []
        peermentorsemails = []
        peermentorsrooms = []
        #Custom people
        for person in range(0,len(hootdata.PEMWEST_C2)):
        	customspeople.append(hootdata.PEMWEST_C2[person])
        template_values['customspeople'] = customspeople
        for person in customspeople:
        	customspeopleemails.append(hootdata.EMAILS[person])
        template_values['customspeopleemails'] = customspeopleemails
        for person in customspeople:
        	customspeoplerooms.append(hootdata.ROOMS[person])
        template_values['customspeoplerooms'] = customspeoplerooms
        #Peer mentors
        for person in range(0,len(hootdata.PEMWEST_PM)):
        	peermentors.append(hootdata.PEMWEST_PM[person])
        template_values['peermentors'] = peermentors
        for person in peermentors:
        	peermentorsemails.append(hootdata.EMAILS[person])
        template_values['peermentorsemails'] = peermentorsemails
        for person in peermentors:
        	peermentorsrooms.append(hootdata.ROOMS[person])

    #PEMWEST THIRD
    elif self.request.get('dorm')=='Pembroke West' and self.request.get('floor')=='3':
        template_values['halladvisor'] = hootdata.PEMWEST_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.PEMWEST_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.PEMWEST_HA[self.request.get('floor')]]
        customspeople = []
        customspeopleemails = []
        customspeoplerooms = []
        peermentors = []
        peermentorsemails = []
        peermentorsrooms = []
        #Custom people
        for person in range(0,len(hootdata.PEMWEST_C3)):
        	customspeople.append(hootdata.PEMWEST_C3[person])
        template_values['customspeople'] = customspeople
        for person in customspeople:
        	customspeopleemails.append(hootdata.EMAILS[person])
        template_values['customspeopleemails'] = customspeopleemails
        for person in customspeople:
        	customspeoplerooms.append(hootdata.ROOMS[person])
        template_values['customspeoplerooms'] = customspeoplerooms
        #Peer mentors
        for person in range(0,len(hootdata.PEMWEST_PM)):
        	peermentors.append(hootdata.PEMWEST_PM[person])
        template_values['peermentors'] = peermentors
        for person in peermentors:
        	peermentorsemails.append(hootdata.EMAILS[person])
        template_values['peermentorsemails'] = peermentorsemails
        for person in peermentors:
        	peermentorsrooms.append(hootdata.ROOMS[person])

        template_values['peermentorsrooms'] = peermentorsrooms
    template = jinja_environment.get_template('views/hoot.html')
    self.response.out.write(template.render(template_values))

routes = [('/', HomeHandler),('/hoot', HootHandler)]
app = webapp2.WSGIApplication(routes, debug=True) 