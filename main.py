import webapp2
from google.appengine.ext import ndb


class BaseModel:
	created = ndb.DateTimeProperty(auto_now = True)
	updated = ndb.DateTimeProperty(auto_now_add = True)

class Users(ndb.Model, BaseModel):
	email = ndb.StringProperty()
	password_hash = ndb.StringProperty()

class Categories(ndb.Model):
	name = ndb.StringProperty()
	
class UserToCategory(ndb.Model, BaseModel):
	user = ndb.KeyProperty(Users)
	category = ndb.KeyProperty(Categories)

class Questions(ndb.Model, BaseModel):
	text = ndb.StringProperty()
	yes_count = ndb.IntegerProperty()
	no_count = ndb.IntegerProperty()

class UserToQuestion(ndb.Model, BaseModel):
	user = ndb.KeyProperty(Users)
	question = ndb.KeyProperty(Questions)		

class FavouritedQuestions(ndb.Model, BaseModel):
	user = ndb.KeyProperty(Users)
	question = ndb.KeyProperty(Questions)

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	# question = Questions(text = "Do I look fat?", yes_count = 1023, no_count = 45)
    	# question.put()
    	# user = Users(email = "krisv@gmail.com", password_hash = "password")
    	# user.put()
    	user = Users.get_by_id(5275456790069248)
    	# question = Questions.get_by_id(4993981813358592)
    	# userToQuestion = UserToQuestion(user = user.key, question = question.key)
    	# userToQuestion.put()
    	q = UserToQuestion.query()
    	q.filter(UserToQuestion.user = user)
        self.response.write(question.yes_count)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
