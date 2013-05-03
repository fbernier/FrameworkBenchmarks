
import subprocess
import sys
import setup_util

def start(args):
  setup_util.replace_text("ruby/resin-web.xml", "mysql:\/\/.*:3306", "mysql://" + args.database_host + ":3306")

  try:
    subprocess.check_call("rvm jruby-1.7.3 do bundle install --gemfile=Gemfile-jruby", shell=True, cwd="ruby")
    subprocess.check_call("cp Gemfile-jruby Gemfile", shell=True, cwd="ruby")
    subprocess.check_call("cp Gemfile-jruby.lock Gemfile.lock", shell=True, cwd="ruby")
    subprocess.check_call("rvm jruby-1.7.3 do warble war", shell=True, cwd="ruby")
    subprocess.check_call("rm -rf $RESIN_HOME/webapps/*", shell=True)
    subprocess.check_call("cp ruby.war $RESIN_HOME/webapps/ruby.war", shell=True, cwd="ruby")
    subprocess.check_call("$RESIN_HOME/bin/resinctl start", shell=True)
    return 0
  except subprocess.CalledProcessError:
    return 1
def stop():
  try:
    subprocess.check_call("$RESIN_HOME/bin/resinctl shutdown", shell=True)
    subprocess.check_call("rm Gemfile", shell=True, cwd="ruby")
    subprocess.check_call("rm Gemfile.lock", shell=True, cwd="ruby")
    return 0
  except subprocess.CalledProcessError:
    return 1
