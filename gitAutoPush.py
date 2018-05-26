import os

class Dinosar(object):
    def __init__(self):
        self._cachedStamp = 0
        self.filename = 'tes_file.txt'
        self.git_repo_name = 'gitAutomatePush' #Do not include .git extension
        self.git_user_name = 'syedjafer'
        self.git_oauth_token = '<Your Auth Token>'
        self.git_commit_msg = 'Update the file'

    def gitAuth(self):
        timeStamp = os.stat(self.filename).st_mtime
        if timeStamp != self._cachedStamp:
            self._cachedStamp = timeStamp
            os.system("git add %s"%(self.filename))
            os.system("git commit -m '%s'"%(self.git_commit_msg))
            os.system("git push https://%s:%s@github.com/%s/%s.git"%(self.git_user_name,
            												self.git_oauth_token,
            												self.git_user_name,
            												self.git_repo_name))

if __name__ == '__main__':
	x = Dinosar()
	x.gitAuth();