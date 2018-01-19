
from bottle import request, response, abort, redirect
from bottle import auth_basic, parse_auth, Bottle, run
from bottle import debug as set_debug
import json
import sys
import uuid

from github import Github

# XXX make these into a real config file
apitoken = "get-me-from-github"
orgName = "linked-art"
repoName = "linked.art"
userName = "azaroth42"

pwh = file("token.txt")
pw = pwh.read().strip()
pwh.close()
gh = Github(userName, pw)
repo = gh.get_repo("%s/%s" % (orgName, repoName))

class AuthApp(object):

    def __init__(self):
        pass

    def send(self, data, status=200, ct="text/plain"):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = "GET,OPTIONS"
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Authorization'
        response["content_type"] = ct
        response.status = status
        return data

    def not_implemented():
        abort(501)

    def dispatch_views(self):
        # Handle getting user to log in
        self.app.route('/', ["GET", "POST"], 
            getattr(self, "handler", self.not_implemented))               

    def get_bottle_app(self):
        """Returns bottle instance"""
        self.app = Bottle()
        self.dispatch_views()
        return self.app    

    def handler(self): 

        # receives data in params
        text = request.query['text']
        token = request.query['token']
        who = request.query['user_name']
        channel = request.query['channel_name']
        domain = request.query['team_domain']

        if token != apitoken or domain != orgName:
            return self.send("Only for %s slack sorry" % orgName, status=200)
        elif not text.isdigit():
            return self.send("Usage /mark <number> ; %s is not a number" % text, status=200)
        else:
            uu = uuid.uuid4().hex
            issue = repo.get_issue(int(text))
            uurl = "https://%s.slackarchive.io/-/search-%s/page-1" % (orgName, uu)
            comment = "%s marks this issue as being discussed in [slack](%s)" % (who, uurl)
            issue.create_comment(comment)
            message = "%s marks <https://github.com/%s/%s/issues/%s|issue %s> as being discussed: %s" % (who, orgName, repoName, text, text, uu)
            resp = {"response_type": "in_channel", "text": message}
            return self.send(json.dumps(resp), ct="application/json")

def main():
    host = "localhost"
    port = 8000
    authapp = AuthApp()
    app=authapp.get_bottle_app()

    set_debug(True)
    run(host=host, port=port, app=app)

if __name__ == "__main__":
    main()
else:
    app = AuthApp();
    application = app.get_bottle_app()
