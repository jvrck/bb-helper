from bbhelper import bbhelper
import os

r = bbhelper.BBRepo.GetWorkspaceRepos(os.environ['BB_WORKSPACE'])

print('workspace count {0}'.format(len(r)))

# pip3 install requests
