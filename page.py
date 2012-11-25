#codnig: utf-8
import webapp2

class InfoPage(webapp2.RequestHandler):
  def get(self):
      self.response.headers['Content-Type'] = 'text/plain'
      self.response.write('tweeted. see https://twitter.com/nozomi_miraha')
