#!/usr/bin/env python
import jinja2
import logging
import os
import webapp2
import hootdata
import urllib2
import json

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
    template_values = {'dorm' : self.request.get('dorm'),
                    	'floor' : self.request.get('floor'),
                    }
    if self.request.get('name')=='':
        template_values['name'] = 'Mawrter'
    else:
        template_values['name'] = self.request.get('name')

    '''
    #bestbuy
    allstuffs = urllib2.urlopen('http://api.remix.bestbuy.com/v1/stores(area(19010,50))?format=json&apiKey=ucys5jzk78w4hjd6rsdfge24')
    allstuff = allstuffs.read()
    store = json.loads(allstuff)

    storeids = []
    storenames = []
    for store_ in store.get('stores'):
        storeids.append(store_.get('storeId'))
        storenames.append(store_.get('name'))

    template_values['storeids'] = storeids
    template_values['storenames'] = storenames
    '''

    customspeople = []
    customspeopleemails = []
    customspeoplerooms = []
    peermentors = []
    peermentorsemails = []
    peermentorsrooms = []

    #BRECON FIRST
    if self.request.get('dorm')=='Brecon' and self.request.get('floor')=='1':
        template_values['halladvisor'] = hootdata.BRECON_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.BRECON_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.BRECON_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.BRECON_C1)):
            customspeople.append(hootdata.BRECON_C1[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.BRECON_PM)):
            peermentors.append(hootdata.BRECON_PM[person])
        template_values['peermentors'] = peermentors

    #BRECON SECOND
    elif self.request.get('dorm')=='Brecon' and self.request.get('floor')=='2':
        template_values['halladvisor'] = hootdata.BRECON_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.BRECON_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.BRECON_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.BRECON_C2)):
            customspeople.append(hootdata.BRECON_C2[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.BRECON_PM)):
            peermentors.append(hootdata.BRECON_PM[person])
        template_values['peermentors'] = peermentors

    #BRECON THIRD
    elif self.request.get('dorm')=='Brecon' and self.request.get('floor')=='3':
        template_values['halladvisor'] = hootdata.BRECON_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.BRECON_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.BRECON_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.BRECON_C3)):
            customspeople.append(hootdata.BRECON_C3[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.BRECON_PM)):
            peermentors.append(hootdata.BRECON_PM[person])
        template_values['peermentors'] = peermentors

    #BRECON FOURTH
    elif self.request.get('dorm')=='Brecon' and self.request.get('floor')=='4':
        template_values['halladvisor'] = hootdata.BRECON_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.BRECON_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.BRECON_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.BRECON_C4)):
            customspeople.append(hootdata.BRECON_C4[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.BRECON_PM)):
            peermentors.append(hootdata.BRECON_PM[person])
        template_values['peermentors'] = peermentors
    
    #DENBIGH FIRST
    elif self.request.get('dorm')=='Denbigh' and self.request.get('floor')=='1':
        template_values['halladvisor'] = hootdata.DENBIGH_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.DENBIGH_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.DENBIGH_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.DENBIGH_C1)):
            customspeople.append(hootdata.DENBIGH_C1[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.DENBIGH_PM)):
            peermentors.append(hootdata.DENBIGH_PM[person])
        template_values['peermentors'] = peermentors

    #DENBIGH SECOND
    elif self.request.get('dorm')=='Denbigh' and self.request.get('floor')=='2':
        template_values['halladvisor'] = hootdata.DENBIGH_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.DENBIGH_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.DENBIGH_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.DENBIGH_C2)):
            customspeople.append(hootdata.DENBIGH_C2[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.DENBIGH_PM)):
            peermentors.append(hootdata.DENBIGH_PM[person])
        template_values['peermentors'] = peermentors

    #DENBIGH THIRD
    elif self.request.get('dorm')=='Denbigh' and self.request.get('floor')=='3':
        template_values['halladvisor'] = hootdata.DENBIGH_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.DENBIGH_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.DENBIGH_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.DENBIGH_C3)):
            customspeople.append(hootdata.DENBIGH_C3[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.DENBIGH_PM)):
            peermentors.append(hootdata.DENBIGH_PM[person])
        template_values['peermentors'] = peermentors

    #ERDMAN FIRST
    elif self.request.get('dorm')=='Erdman' and self.request.get('floor')=='1':
        template_values['halladvisor'] = hootdata.ERDMAN_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.ERDMAN_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.ERDMAN_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.ERDMAN_C)):
            customspeople.append(hootdata.ERDMAN_C[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.ERDMAN_PM)):
            peermentors.append(hootdata.ERDMAN_PM[person])
        template_values['peermentors'] = peermentors

    #ERDMAN SECOND
    elif self.request.get('dorm')=='Erdman' and self.request.get('floor')=='2':
        template_values['halladvisor'] = hootdata.ERDMAN_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.ERDMAN_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.ERDMAN_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.ERDMAN_C)):
            customspeople.append(hootdata.ERDMAN_C[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.ERDMAN_PM)):
            peermentors.append(hootdata.ERDMAN_PM[person])
        template_values['peermentors'] = peermentors

    #ERDMAN THIRD
    elif self.request.get('dorm')=='Erdman' and self.request.get('floor')=='3':
        template_values['halladvisor'] = hootdata.ERDMAN_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.ERDMAN_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.ERDMAN_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.ERDMAN_C)):
            customspeople.append(hootdata.ERDMAN_C[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.ERDMAN_PM)):
            peermentors.append(hootdata.ERDMAN_PM[person])
        template_values['peermentors'] = peermentors

    #MERION FIRST
    elif self.request.get('dorm')=='Merion' and self.request.get('floor')=='1':
        template_values['halladvisor'] = hootdata.MERION_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.MERION_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.MERION_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.MERION_C1)):
            customspeople.append(hootdata.MERION_C1[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.ERDMAN_PM)):
            peermentors.append(hootdata.ERDMAN_PM[person])
        template_values['peermentors'] = peermentors

    #MERION SECOND
    elif self.request.get('dorm')=='Merion' and self.request.get('floor')=='2':
        template_values['halladvisor'] = hootdata.MERION_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.MERION_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.MERION_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.MERION_C2)):
            customspeople.append(hootdata.MERION_C2[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.ERDMAN_PM)):
            peermentors.append(hootdata.ERDMAN_PM[person])
        template_values['peermentors'] = peermentors

    #MERION THIRD
    elif self.request.get('dorm')=='Merion' and self.request.get('floor')=='3':
        template_values['halladvisor'] = hootdata.MERION_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.MERION_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.MERION_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.MERION_C3)):
            customspeople.append(hootdata.MERION_C3[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.ERDMAN_PM)):
            peermentors.append(hootdata.ERDMAN_PM[person])
        template_values['peermentors'] = peermentors

    #MERION FOURTH
    elif self.request.get('dorm')=='Merion' and self.request.get('floor')=='4':
        template_values['halladvisor'] = hootdata.MERION_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.MERION_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.MERION_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.MERION_C4)):
            customspeople.append(hootdata.MERION_C4[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.ERDMAN_PM)):
            peermentors.append(hootdata.ERDMAN_PM[person])
        template_values['peermentors'] = peermentors

    #PEMEAST FIRST
    elif self.request.get('dorm')=='Pembroke East' and self.request.get('floor')=='1':
        template_values['halladvisor'] = hootdata.PEMEAST_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.PEMEAST_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.PEMEAST_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.PEMEAST_C1)):
        	customspeople.append(hootdata.PEMEAST_C1[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.PEMEAST_PM)):
        	peermentors.append(hootdata.PEMEAST_PM[person])
        template_values['peermentors'] = peermentors

    #PEMEAST SECOND
    elif self.request.get('dorm')=='Pembroke East' and self.request.get('floor')=='2':
        template_values['halladvisor'] = hootdata.PEMEAST_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.PEMEAST_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.PEMEAST_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.PEMEAST_C2)):
        	customspeople.append(hootdata.PEMEAST_C2[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.PEMEAST_PM)):
        	peermentors.append(hootdata.PEMEAST_PM[person])
        template_values['peermentors'] = peermentors

    #PEMEAST THIRD    	
    elif self.request.get('dorm')=='Pembroke East' and self.request.get('floor')=='3':
        template_values['halladvisor'] = hootdata.PEMEAST_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.PEMEAST_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.PEMEAST_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.PEMEAST_C3)):
        	customspeople.append(hootdata.PEMEAST_C3[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.PEMEAST_PM)):
        	peermentors.append(hootdata.PEMEAST_PM[person])
        template_values['peermentors'] = peermentors

    #PEMWEST FIRST
    elif self.request.get('dorm')=='Pembroke West' and self.request.get('floor')=='1':
        template_values['halladvisor'] = hootdata.PEMWEST_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.PEMWEST_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.PEMWEST_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.PEMWEST_C1)):
        	customspeople.append(hootdata.PEMWEST_C1[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.PEMWEST_PM)):
        	peermentors.append(hootdata.PEMWEST_PM[person])
        template_values['peermentors'] = peermentors

    #PEMWEST SECOND
    elif self.request.get('dorm')=='Pembroke West' and self.request.get('floor')=='2':
        template_values['halladvisor'] = hootdata.PEMWEST_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.PEMWEST_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.PEMWEST_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.PEMWEST_C2)):
        	customspeople.append(hootdata.PEMWEST_C2[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.PEMWEST_PM)):
        	peermentors.append(hootdata.PEMWEST_PM[person])
        template_values['peermentors'] = peermentors

    #PEMWEST THIRD
    elif self.request.get('dorm')=='Pembroke West' and self.request.get('floor')=='3':
        template_values['halladvisor'] = hootdata.PEMWEST_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.PEMWEST_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.PEMWEST_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.PEMWEST_C3)):
        	customspeople.append(hootdata.PEMWEST_C3[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.PEMWEST_PM)):
        	peermentors.append(hootdata.PEMWEST_PM[person])
        template_values['peermentors'] = peermentors

    #RADNOR FIRST
    elif self.request.get('dorm')=='Radnor' and self.request.get('floor')=='1':
        template_values['halladvisor'] = hootdata.RADNOR_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.RADNOR_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.RADNOR_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.RADNOR_C1)):
            customspeople.append(hootdata.RADNOR_C1[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.RADNOR_PM)):
            peermentors.append(hootdata.RADNOR_PM[person])
        template_values['peermentors'] = peermentors

    #RADNOR SECOND
    elif self.request.get('dorm')=='Radnor' and self.request.get('floor')=='2':
        template_values['halladvisor'] = hootdata.RADNOR_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.RADNOR_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.RADNOR_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.RADNOR_C2)):
            customspeople.append(hootdata.RADNOR_C2[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.RADNOR_PM)):
            peermentors.append(hootdata.RADNOR_PM[person])
        template_values['peermentors'] = peermentors

    #RADNOR THIRD
    elif self.request.get('dorm')=='Radnor' and self.request.get('floor')=='3':
        template_values['halladvisor'] = hootdata.RADNOR_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.RADNOR_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.RADNOR_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.RADNOR_C3)):
            customspeople.append(hootdata.RADNOR_C3[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.RADNOR_PM)):
            peermentors.append(hootdata.RADNOR_PM[person])
        template_values['peermentors'] = peermentors

    #RHOADSSOUTH FIRST
    elif self.request.get('dorm')=='Rhoads South' and self.request.get('floor')=='1':
        template_values['halladvisor'] = hootdata.ROCK_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.RHOADSSOUTH_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.RHOADSSOUTH_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.RHOADSSOUTH_C1)):
            customspeople.append(hootdata.RHOADSSOUTH_C1[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.RHOADSSOUTH_PM)):
            peermentors.append(hootdata.ROCK_PM[person])
        template_values['peermentors'] = peermentors

    #RHOADSSOUTH SECOND
    elif self.request.get('dorm')=='Rhoads South' and self.request.get('floor')=='2':
        template_values['halladvisor'] = hootdata.ROCK_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.RHOADSSOUTH_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.RHOADSSOUTH_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.RHOADSSOUTH_C2)):
            customspeople.append(hootdata.RHOADSSOUTH_C2[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.RHOADSSOUTH_PM)):
            peermentors.append(hootdata.ROCK_PM[person])
        template_values['peermentors'] = peermentors

    #RHOADSSOUTH THIRD
    elif self.request.get('dorm')=='Rhoads South' and self.request.get('floor')=='3':
        template_values['halladvisor'] = hootdata.ROCK_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.RHOADSSOUTH_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.RHOADSSOUTH_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.RHOADSSOUTH_C3)):
            customspeople.append(hootdata.RHOADSSOUTH_C3[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.RHOADSSOUTH_PM)):
            peermentors.append(hootdata.ROCK_PM[person])
        template_values['peermentors'] = peermentors

    #ROCK FIRST
    elif self.request.get('dorm')=='Rockefeller' and self.request.get('floor')=='1':
        template_values['halladvisor'] = hootdata.ROCK_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.ROCK_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.ROCK_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.ROCK_C1)):
            customspeople.append(hootdata.ROCK_C1[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.ROCK_PM)):
            peermentors.append(hootdata.ROCK_PM[person])
        template_values['peermentors'] = peermentors

    #ROCK SECOND
    elif self.request.get('dorm')=='Rockefeller' and self.request.get('floor')=='2':
        template_values['halladvisor'] = hootdata.ROCK_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.ROCK_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.ROCK_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.ROCK_C2)):
            customspeople.append(hootdata.ROCK_C2[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.ROCK_PM)):
            peermentors.append(hootdata.ROCK_PM[person])
        template_values['peermentors'] = peermentors

    #ROCK THIRD
    elif self.request.get('dorm')=='Rockefeller' and self.request.get('floor')=='3':
        template_values['halladvisor'] = hootdata.ROCK_HA[self.request.get('floor')]
        template_values['halladvisoremail'] = hootdata.EMAILS[hootdata.ROCK_HA[self.request.get('floor')]]
        template_values['halladvisorroom'] = hootdata.ROOMS[hootdata.ROCK_HA[self.request.get('floor')]]
        #Custom people
        for person in range(0,len(hootdata.ROCK_C3)):
            customspeople.append(hootdata.ROCK_C3[person])
        template_values['customspeople'] = customspeople
        #Peer mentors
        for person in range(0,len(hootdata.ROCK_PM)):
            peermentors.append(hootdata.ROCK_PM[person])
        template_values['peermentors'] = peermentors

    #Adding customs people and peer mentors to data store
    for person in customspeople:
        customspeopleemails.append(hootdata.EMAILS[person])
    template_values['customspeopleemails'] = customspeopleemails
    for person in customspeople:
        customspeoplerooms.append(hootdata.ROOMS[person])
    template_values['customspeoplerooms'] = customspeoplerooms

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